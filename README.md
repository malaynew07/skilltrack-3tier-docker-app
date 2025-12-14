# 🚀 SkillTrack – 3-Tier Dockerized Application

## 📌 Overview

SkillTrack is a simple **3-tier web application** built to demonstrate real-world **Docker and DevOps practices**.  
The application allows users to submit their skills and progress, which are stored persistently in a MySQL database.

This project focuses on:
- Dockerfile and Docker Compose usage
- Multi-container orchestration
- Database initialization using init scripts
- Service healthchecks
- Practical debugging (CORS, networking, startup order)

---

## 🧱 Architecture

Frontend (Nginx + HTML/JS)
|
| HTTP POST
|
Backend (Flask API)
|
| SQL INSERT
|
Database (MySQL)


---

## 📂 Project Structure

skilltrack-3tier-docker-app/
├── frontend/
│ ├── Dockerfile
│ ├── index.html
│ └── app.js
│
├── backend/
│ ├── Dockerfile
│ ├── app.py
│ ├── db.py
│ └── requirements.txt
│
├── database/
│ └── init.sql
│
└── docker-compose.yml


---

## 🎨 Frontend Layer

**Technology:** HTML, JavaScript, Nginx  

**Responsibilities:**
- Collect user input (name, email, skill, progress)
- Send POST request to backend API
- Display response to the user

Nginx is used as a lightweight, production-ready web server.

---

## ⚙️ Backend Layer

**Technology:** Python, Flask, Flask-CORS  

**Responsibilities:**
- Exposes REST API endpoint `/add`
- Accepts JSON payload from frontend
- Inserts data into MySQL database
- Returns success response

CORS is enabled to allow browser-based requests.

---

## 🗄️ Database Layer

**Technology:** MySQL 8  

The database is initialized using an `init.sql` script that runs automatically on first container startup.

```sql
CREATE TABLE skills (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  skill VARCHAR(50),
  progress INT
);
Docker volumes are used to persist data across container restarts.

🐳 Docker & Docker Compose
Dockerfile

Used for frontend and backend services

Backend uses multi-stage Dockerfile to reduce image size and improve security

Docker Compose

Orchestrates frontend, backend, and database services

Uses internal Docker networking for service communication

Includes MySQL healthcheck to ensure DB readiness before backend startup.

▶️ How to Run the Application
docker-compose down -v
docker-compose up -d --build

Access

Frontend: http://localhost

Backend: http://localhost:5000

✅ Application Flow

User submits data from frontend UI

Frontend sends POST request to backend

Backend processes request and inserts data into MySQL

Data is stored persistently

Success response is returned

🧪 Verification
USE skilltrack;
SELECT * FROM skills;

🎯 Key Learnings

3-tier application architecture

Dockerfile vs Docker Compose

Multi-stage Docker builds

Docker networking and service discovery

Database initialization using init scripts

Healthchecks for service readiness

CORS debugging in containerized applications

End-to-end DevOps troubleshooting

👤 Author

Malay Ranjan Panigrahi
DevOps Enthusiast | Docker | Linux | Cloud
Thank you.............................
