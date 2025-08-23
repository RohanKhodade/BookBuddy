# Book Buddy

Book Buddy is a Django-based web application designed for college students to exchange second-hand books at affordable prices. With a simple and intuitive user interface, students can buy, sell, and browse books, manage their cart, and connect with others interested in their listings. The app uses Django and Django templates for a seamless experience.

## Features
- **Sell Books**: List your second-hand books for sale with details like price and condition.
- **Buy Books**: Browse and purchase affordable second-hand books from other students.
- **Browse Available Books**: View a catalog of all books available for exchange.
- **Add to Cart**: Select books and add them to your cart for easy checkout.
- **Track Interest**: See which users are interested in the books you’ve listed.
- **User Authentication**:
  - Register using a phone number.
  - Log in with a username and password.
- **Simple UI**: Clean and user-friendly interface for easy navigation.

## Tech Stack
- **Framework**: Django
- **Frontend**: Django templates
- **Database**: SQLite (default, can be configured for other databases)
- **Authentication**: Django’s built-in authentication system

## Getting Started

### Prerequisites
- Python 3.8
- Django 4.x
- Git
- Virtualenv (recommended)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RohanKhodade/BookBuddy.git
   cd book_exchange
   cd books
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit `http://127.0.0.1:8000` to access the app.

### Project Structure
```
book-buddy/
├── book_buddy/          # Main app directory
├── templates/           # Django templates for the frontend
├── static/             # Static files (CSS, JS, images)
├── manage.py           # Django management script
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Usage
- **Register**: Create an account using your phone number.
- **Log In**: Use your username and password to access the platform.
- **Sell a Book**: Add a book with details like title, price, and condition.
- **Buy a Book**: Browse available books and add them to your cart.
- **Track Interest**: Check notifications to see who’s interested in your listed books.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, reach out via [your-email@example.com](mailto:rohankhodade883@gmail.com) or open an issue on GitHub.