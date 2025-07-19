# Django CRM Application 🧑‍💼💻

## Overview 📝

This is a **Customer Relationship Management (CRM)** web application built with **Django** and **Bootstrap**. It enables users to register, log in, and manage customer records intuitively with a clean, modern interface using a custom color palette.

The app features:

- User authentication (registration, login, logout)
- Adding, viewing, updating, and deleting customer records
- Responsive UI with Bootstrap 5
- Flash messages for user feedback

---

## System Architecture and Workflow ⚙️

1. **User Authentication and Session Management**

   - Users can register and log in securely.
   - Django’s built-in authentication system manages sessions and user access.

2. **Customer Record Management**

   - Authenticated users can add new customer records through forms.
   - Records can be viewed in a paginated table.
   - Users can update or delete existing records.
   - Detailed record pages show full information.

3. **Frontend and Styling**

   - Bootstrap is used for layout and components.
   - Flash messages use Bootstrap alerts for user notifications.

4. **Template Rendering and Static Files**

   - Django templates organize reusable components (e.g., navbar, base).
   - Forms use CSRF protection automatically via Django.

---

## Dependencies 📦

- **Django==5.2.4** — web framework for backend and templating  
- **Bootstrap 5** — CSS framework for responsive UI  
- **MySQL** — database for development  
- **Python 3.13.4** — programming language  

---

## Installation ⚡

```bash
# Clone repository
git clone https://github.com/yourusername/DjangoCRM.git
cd DjangoCRM

# Create and activate virtual environment (optional but recommended)
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin panel (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver

Once the server is running, open your web browser and navigate to the address shown in the terminal
```

## Usage 🚀

- Register a new user or log in to access the CRM features.
- Add new customer records using the **Add Record** page.
- Browse customers on the home page, with pagination support.
- Click on a customer ID to view detailed information about that customer.
- Update or delete customer records from the detail page.
- Use the navigation bar to easily switch between pages and to log out.
