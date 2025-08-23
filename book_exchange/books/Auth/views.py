from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import PhoneVerification
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from BookStore.models import Book


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def forgot_password(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            phone_verification = PhoneVerification.objects.get(phone_number=phone_number)
            return redirect('reset_password', phone_number=phone_number)
        except PhoneVerification.DoesNotExist:
            messages.error(request, 'No account is associated with this phone number.')

    return render(request, 'forgot_password.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get('phone_number')

            # Check if username or phone number already exists
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Email already exists.')
            elif PhoneVerification.objects.filter(phone_number=phone_number).exists():
                form.add_error('phone_number', 'Phone number already exists.')
            else:
                # Create user and phone verification record
                user = User.objects.create_user(username=username, password=password)
                phone_verification = PhoneVerification.objects.create(
                    phone_number=phone_number,
                    username=username,
                    is_verified=True  # Mark as verified since no OTP is needed
                )
                phone_verification.save()
                login(request, user)
                return redirect('landing_page')
        else:
            print("Form errors:", form.errors)  # Debugging

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def landing_page(request):
    user = request.user
    books_sorted = Book.objects.filter(is_sold=False)

    try:
        phone_verification = PhoneVerification.objects.get(username=user.username)
        phone_number = phone_verification.phone_number
    except PhoneVerification.DoesNotExist:
        phone_number = "Phone number not found"

    context = {
        'books': books_sorted,
        'username': user.username,
        'phone_number': phone_number,
        'book_list_url': 'book_list',
        'sell_book_url': 'sell_book',
    }
    return render(request, 'landing_page.html', context)


def reset_password(request, phone_number):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        try:
            phone_verification = PhoneVerification.objects.get(phone_number=phone_number)
            user = User.objects.get(username=phone_verification.username)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password has been reset. Please log in.')
            return redirect('login')
        except (PhoneVerification.DoesNotExist, User.DoesNotExist):
            messages.error(request, 'User not found.')

    return render(request, 'reset_password.html')


def logout_view(request):
    logout(request)
    return redirect('login')