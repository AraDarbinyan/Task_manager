# 🧩 Task Manager API

A simple and functional **Task Manager REST API** built with **FastAPI**.  
The project includes user registration, login with JWT authentication, and CRUD operations for tasks.  
It demonstrates core backend development skills: authentication, database models, API design, and clean architecture.

---

## 🚀 Features

- **User Authentication**
  - Registration and secure password hashing (using `bcrypt`)
  - Login with JWT-based authentication
  - Protected routes using OAuth2

- **Task Management**
  - Create, read, update, and delete personal tasks
  - Each user can manage only their own tasks

- **Tech Stack**
  - **FastAPI** — web framework
  - **SQLAlchemy** — ORM for database operations
  - **SQLite** — lightweight development database
  - **Pydantic** — data validation
  - **JWT (python-jose)** — token-based authentication

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/task-manager.git
   cd task-manager
