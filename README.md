 Vehicles Management System - Django Enterprise 🚀
Vehicles Management System is a sophisticated web application built with Django 5.x, designed to manage automotive inventories, user interactions, and car showcases. The project follows best practices in web development, providing a clean interface for both admins and visitors.

 Core Modules & Features
Car Catalog (cars app): A complete system to manage vehicle listings, including detailed specifications and categorized views.

User Authentication (accounts app): Secure system for user registration, login, and advanced account management (including password reset logic).

Dynamic Content Management: Fully integrated with Django Admin for easy management of vehicles, brands, and user data.

Frontend Architecture: Uses a centralized templates/ structure with a base.html master layout for a consistent and professional UI/UX.

Modern Styling: Integrated custom CSS and static assets to ensure a visually appealing experience for the end-user.

 Technical Implementation
Backend: Python / Django.

Database: SQLite (with a clean relational schema).

Security: CSRF protection, secure session handling, and encrypted password storage.

Asset Management: Configured to handle static files and media (images) efficiently.

 Project Roadmap (Current Files)
cars/: Core logic for vehicle listings and car-specific views.

accounts/: Comprehensive user authentication and profile management.

templates/car/: Specific layouts for the home page, about us, and contact sections.

vehicles/: Central configuration, settings, and URL routing.

 Setup & Installation
Clone the Repo:

Bash
git clone https://github.com/kholoudtr/Vehicles.git
cd Vehicles
Database Setup:

Bash
python manage.py migrate
Create Admin User:

Bash
python manage.py createsuperuser
Run Server:

Bash
python manage.py runserver
Visit: http://127.0.0.1:8000/