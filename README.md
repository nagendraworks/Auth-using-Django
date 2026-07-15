# Django Role-Based Authentication System

A secure and modular authentication system built with Django. This project implements a **custom user model**, **role-based authentication**, isolated dashboards, and an **OTP-based password recovery system via email**.

The project follows Django best practices by keeping sensitive credentials outside the codebase using environment variables.

---

## 🚀 Features

### 🔐 Custom User Model
- Extends Django's default authentication system.
- Supports multiple user roles:
  - Admin
  - Distributor

### 👥 Role-Based Authentication
- Users are redirected automatically based on their assigned role after login.
- Separate dashboards for different user types.
- Role-based access control.

### 📧 OTP Password Recovery
- Secure password reset workflow.
- Generates a random **6-digit OTP**.
- OTP expires after **10 minutes**.
- OTP verification through email.
- Allows users to securely reset their password.

### 🎨 Modern UI
- Responsive user interface.
- Styled using Tailwind CSS.

### 🔒 Security Practices
- Environment variables for sensitive credentials.
- Django password hashing.
- CSRF protection.
- Session-based authentication.

---

# 🛠️ Tech Stack

- **Backend:** Django
- **Language:** Python
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (Default)
- **Email Service:** SMTP (Gmail)
- **Authentication:** Django Authentication Framework

---

# 📋 Prerequisites

Make sure you have:

- Python 3.10+
- Django 5.0+
- pip

Check Python version:

```bash
python --version
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <repository-url>

cd auth_project
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# 🔑 4. Configure Environment Variables

Create a `.env` file in the project root (same location as `manage.py`):

```
auth_project/
│
├── manage.py
├── .env
└── requirements.txt
```

Add your email configuration:

```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_google_app_password
```

### Creating Google App Password

1. Enable **2-Step Verification** on your Google Account.
2. Generate an **App Password**.
3. Use that password in `.env`.

> Never upload `.env` to GitHub.

A sample file is provided:

```
.env.example
```

Copy it:

```bash
cp .env.example .env
```

and update the values.

---

# 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# 👤 Create Admin Account

Create a superuser:

```bash
python manage.py createsuperuser
```

Enter:

- Username
- Email
- Password

---

# ▶️ Run the Application

Start the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🧪 Testing

## Role-Based Login Testing

1. Open Django admin panel:

```
http://127.0.0.1:8000/django-admin/
```

2. Create users.

3. Assign roles:
   - Admin
   - Distributor

4. Login from:

```
http://127.0.0.1:8000/
```

5. Verify:

| User Role | Redirect Dashboard |
|---|---|
| Admin | Admin Dashboard |
| Distributor | Distributor Dashboard |

---

## OTP Password Reset Testing

1. Ensure a user has a valid email address.

2. Click:

```
Forgot Password
```

3. Enter username.

4. Check registered email.

5. Enter the received 6-digit OTP.

6. Create a new password.

---

# 📁 Project Structure

```
auth_project/

│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── templates/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

---

# 📦 Dependencies

Main dependencies:

```
Django
python-dotenv
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔒 Environment Files

Tracked by Git:

```
.env.example ✅
```

Ignored by Git:

```
.env ❌
```

The `.env` file contains private credentials and should never be committed.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Steps:

1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Submit a pull request.

---

# 📜 License

This project is available for educational and personal learning purposes.

---

# 👨‍💻 Author

Nagendra

Built with Django ❤️