# Django Authentication System
## https://giving-charm-production-d03a.up.railway.app/
A complete user authentication system built with Django, featuring a modern and responsive interface. Includes login, registration, password recovery, and a profile dashboard.
The verification code is not working yet! Please enter any 6 numbers.

## Features
+ Login — email and password authentication with secure hashing
+ Registration — account creation with unique email validation and password confirmation
+ Password recovery — 3-step flow: email → verification code → new password
+ Dashboard — profile overview and password change while logged in
+ Logout — with confirmation modal
+ Password strength indicator — real-time visual feedback
+ Feedback messages — inline error and success notifications

## Tech Stack
| Layer | Technology |
| ----- | ---------- |
| Backend | Python 3 / Django 6 |
| Database | PostgreSQL / SQLite (local) |
| Authentication | django.contrib.auth.hashers (PBKDF2) |
| Static Files | WhiteNoise |
| Deploy | Railway |
| Frontend | HTML5, CSS3, Vanilla JavaScript |

## Running Locally
Prerequisites
+ Python 3.10+
+ pip

1. Clone the repository
```
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
2. Create and activate a virtual environment
```
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Set up environment variables
Create a .env file at the project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: use PostgreSQL locally
# DATABASE_URL=postgres://user:password@localhost:5432/db_name
```
5. Run migrations
```
python manage.py migrate
```
6. Start the development server
```
python manage.py runserver
```

## Deployment (Railway)
The project is configured for deployment on Railway. The following environment variables are required:
| Variable | Description |
| -------- | ----------- |
| `SECRET_KEY` | Django Secret Key |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Allowed domain(s) |
| `DATABASE_URL` | PostgreSQL connection URL (provided by Railway) |
Remember to update `CSRF_TRUSTED_ORIGINS` in `settings.py` with your deployment domain.

## Routes
| URL | View | Description |
| --- | ---- | ----------- |
| `/` | `telaLogin` | Login and registration page |
| `/sistema` | `sistema` | User dashboard |
| `new-password` | `newPassword` | Password recovery flow |

## Security

+ Passwords stored with PBKDF2 hashing via Django's `make_password` / `check_password`
+ CSRF protection enabled on all forms
+ Session-based authentication to keep users logged in
+ WhiteNoise with `CompressedManifestStaticFilesStorage` for secure static file caching

## License
This project is licensed under the **MIT License.** See the LICENSE file for details.
