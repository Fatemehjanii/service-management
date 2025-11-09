
# 🛠 Service Management API

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![REST Framework](https://img.shields.io/badge/DRF-3.15-blueviolet)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A **Django REST Framework** project for managing **users, projects, and tasks**.  
This API allows creating, updating, deleting, and retrieving users, projects, and tasks, as well as assigning tasks to users and projects.

---

## ⚡ Features

- ✅ Full CRUD operations for Users, Projects, and Tasks
- ✅ Assign tasks to multiple users
- ✅ Assign tasks to projects
- ✅ Retrieve tasks by user and sort by start time
- ✅ Built with **Django** and **DRF**

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Fatemehjanii/service-management.git
cd service-management

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## 🔗 API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/users/` | List all users |
| POST   | `/users/` | Create a new user |
| PUT    | `/users/{id}/` | Update user |
| DELETE | `/users/{id}/` | Delete user |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/projects/` | List all projects |
| POST   | `/projects/` | Create a project |
| PUT    | `/projects/{id}/` | Update project |
| DELETE | `/projects/{id}/` | Delete project |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/tasks/` | List all tasks |
| POST   | `/tasks/` | Create a task |
| PUT    | `/tasks/{id}/` | Update a task |
| DELETE | `/tasks/{id}/` | Delete a task |
| PUT    | `/tasks/{task_id}/assign-users/` | Assign users to a task |
| PUT    | `/tasks/assign-to-project/` | Assign task to a project |
| GET    | `/tasks/user/{user_id}/` | List tasks by user |
| GET    | `/tasks/by-start-time/` | List tasks sorted by start time |

---

## 🧪 Testing

You can test API endpoints using tools like:  
- [Postman](https://www.postman.com/)  
- [Insomnia](https://insomnia.rest/)

---

## 🌟 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> **Tip:** All API requests and responses use **JSON format**. Task start and end times are automatically set when created.

