# 📨 Customer Feedback Portal

A full-stack web application that allows users to submit feedback and administrators to track and resolve responses. Built with Django (REST API) and React (frontend).

---

## 🧰 Tech Stack

- **Frontend:** React, Axios
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Styling:** CSS (plain)

---

## 🚀 Features

- Submit feedback (name, email, message)
- API endpoint for creating and retrieving feedback
- Admin panel to manage feedback entries
- Responsive form built in React

---

## 📂 Folder Structure

feedback-portal/
├── backend/ # Django project + feedback app
├── client/ # React frontend
├── manage.py # Django entry point
├── venv/ # Python virtual environment


---

## ⚙️ Getting Started

### 🐍 Django Backend

```bash
cd feedback-portal
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt  # Optional if you create one
python manage.py migrate
python manage.py runserver

🌐 React Frontend

cd client
npm install
npm start

🔗 API Endpoint
POST /api/feedback/

{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Love your service!"
}


