# TeachRate

TeachRate is a professional web application designed to facilitate student feedback and rating for university faculty members. It provides a structured platform for students to review their teachers based on their academic performance, helping maintain transparency and academic excellence within institutions.

# 🚀 Features

- Teacher Profiles**: Comprehensive profiles for faculty members including designation, department, and university affiliation.
- Rating System**: Integrated 1-5 star rating system for students to provide feedback.
- Dynamic Search & Filter**: Easily find teachers by university or department.
- Average Rating Calculation**: Automatic calculation of faculty ratings to provide a quick overview of performance.
- User Authentication**: Secure sign-up and sign-in functionality for students.
- Media Management**: Centralized handling of teacher profile pictures.

# 🛠️ Tech Stack

- Backend**: Python, Django
- Database**: MySQL 
- Frontend**: HTML5, CSS3, JavaScript
- Styling**: Custom Vanilla CSS
- Media Handling: Django File Storage

# 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server
- `pip` (Python package manager)

# ⚙️ Installation & Setup

1. Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TeachRate-main
   ```

2. Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:**
   ```bash
   pip install django mysqlclient
   ```

4. Database Configuration:**
   - Create a MySQL database named `Teacher_Rating`.
   - Update the `DATABASES` setting in `User/settings.py` with your MySQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'Teacher_Rating',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': '127.0.0.1',
             'PORT': '3306',
         }
     }
     ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (to access the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:**
   ```bash
   python manage.py runserver
   ```

Access the application at `http://127.0.0.1:8000/`.

# 📂 Project Structure

- `TeachRate/`: Main application logic (Models, Views, Templates).
- `User/`: Project configuration and settings.
- `static/`: CSS and JavaScript assets.
- `images/`: Directory for uploaded teacher profile pictures.
- `templates/`: HTML templates for the UI.

# 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

# 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
