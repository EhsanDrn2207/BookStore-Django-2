
# 📚 Personal Library

A **Django-based web application** for managing your personal book collection with ease. Organize, categorize, and review your books in a user-friendly interface.

---

## 🌟 Features

- **User Authentication**: 
  - Sign up and log in to securely manage your personal library.
  
- **Book Management**: 
  - Add, edit, and delete books in your collection.
  
- **Image Uploads**: 
  - Upload book cover images for better organization and visualization.
  
- **Categorization**: 
  - Organize books by publisher, author, and genre for quick access.
  
- **User Reviews**: 
  - Rate and leave reviews for books in your library.

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- **Python 3.x** installed on your system.
- **Docker** (optional, if you wish to containerize the app).
- **PostgreSQL** (or any other database you prefer).

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EhsanDrn2207/personal-library.git
   cd personal-library
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:
   - On **Linux/macOS**:
     ```bash
     source env/bin/activate
     ```
   - On **Windows**:
     ```bash
     env\Script\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the database**:
   - Update the `DATABASES` section in `settings.py` with your database credentials.

6. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

---

## 🗂️ Project Structure

```
personal-library/
├── manage.py               # Django’s command-line utility
├── app_name/               # Your Django applications (models, views, etc.)
├── templates/              # HTML templates for rendering the frontend
├── static/                 # Static files (CSS, JavaScript, images)
├── media/                  # Uploaded book cover images
├── requirements.txt        # Python dependencies
└── settings.py             # Project configuration (database, installed apps, etc.)
```

---

## 🛠️ Technologies Used

| Technology   | Description                                  |
|--------------|----------------------------------------------|
| **Django**   | High-level Python web framework.             |
| **Python**   | Core programming language.                  |
| **PostgreSQL**| Default database (configurable to others).   |
| **Docker**   | Containerization for deployment (optional). |

---

## 🌐 Deployment

You can containerize and deploy the application using **Docker** or use platforms like **Heroku**, **Render**, or **PythonAnywhere**.

### Docker Deployment (Optional)
1. **Build the Docker image**:
   ```bash
   docker build -t personal-library .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 personal-library
   ```

---

## 👤 Author

**Ehsan Doroudian**  
Feel free to reach out for any feedback or questions.

---

## 🤝 Contributing

Currently, the project is not open to contributions. Suggestions and feedback are welcome!

---

## 📜 License


Enjoy organizing your library with **Personal Library**! 🎉
