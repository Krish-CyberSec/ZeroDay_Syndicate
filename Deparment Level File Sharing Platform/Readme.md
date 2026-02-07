# 📘 Department-Level Secure Academic File Sharing System

A secure, role-based academic web portal built using **Python (Django)** that enables faculty and students to safely share notes and assignments within a university department. The system focuses on **security, controlled access, and real-world academic workflows**, complementing existing LMS platforms.

---

## 🚀 Project Overview

In many universities, academic files are shared using informal platforms such as WhatsApp, email, or USB drives, which introduces risks like malware propagation, unauthorized access, and lack of accountability.

This project provides a **secure, department-level solution** where:
- Only **college-created accounts** can access the system
- Faculty control which student groups receive documents
- Students can only access content meant for their academic group
- Files are validated using **file signature (magic bytes)** and **hashing (SHA-256 / MD5)** to prevent disguised malware uploads
- Students receive **notifications** for new notes and assignments

---

## 🎯 Key Features

### 👥 User Roles
- **Admin (College)**
  - Creates student and faculty accounts
  - Assigns roles, branch, specialization, course, and year
  - Resets passwords
  - No public signup allowed

- **Faculty**
  - Upload notes and assignments
  - Select target student group
  - View student submissions
  - Files are visible to students with faculty name

- **Student**
  - Login using official university email
  - Download notes
  - View and submit assignments
  - Change password after first login
  - Access only group-specific content

---

### 📘 Notes Module
- Uploaded only by faculty
- Students can only download
- Visible only to selected student groups
- Faculty name shown with each upload

---

### 📝 Assignment Module
- Faculty uploads assignments
- Students download assignments
- Students upload assignment solutions
- Submissions are validated and hashed

---

### 🔔 Notification System
- Triggered when faculty uploads notes or assignments
- Sent only to selected student groups
- Displayed on:
  - Student dashboard
  - Assignment page

---

## 🔐 Security Implementation

### 1️⃣ Authentication & Authorization
- Django built-in authentication
- Role-Based Access Control (RBAC)
- Group-Based Access Control (branch, specialization, course, year)

---

### 2️⃣ Secure File Upload (Advanced Protection)

To prevent attackers from disguising malicious files by changing file extensions, the system uses **three-layer file validation**:

#### ✅ Layer 1: File Extension Check
- Allowed: `.pdf`, `.docx`
- Not trusted alone

#### ✅ Layer 2: MIME Type Check
- Checks OS-reported file type
- Can be spoofed

#### 🔥 Layer 3: File Signature (Magic Byte) Validation
Validates the actual file content.

| File Type | Magic Bytes |
|----------|-------------|
| PDF | `%PDF-` |
| EXE | `MZ` |
| ZIP / DOCX | `PK` |

❌ Example: A `.pdf` file starting with `MZ` is blocked.

---

### 3️⃣ File Hashing (SHA-256 / MD5)
- Hash generated on upload
- Hash stored in database
- Hash verified on download
- Ensures file integrity and tamper detection

---

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap (optional)

### Backend
- **Python (Django)**

### Database
- SQLite (development)
- PostgreSQL (deployment)

### Security
- Django Authentication
- Role-Based & Group-Based Access Control
- File Signature (Magic Byte) Validation
- SHA-256 / MD5 Hashing

### Deployment
- Department-level local server
- Internal university network

---

## 🗂️ Conceptual Database Structure

- **UserProfile**
  - user
  - role
  - branch
  - specialization
  - course
  - year

- **Notes**
  - title
  - file
  - group fields
  - uploaded_by
  - file_hash

- **Assignment**
  - title
  - file
  - deadline
  - group fields
  - file_hash

- **AssignmentSubmission**
  - assignment
  - student
  - file
  - submission_hash

- **Notification**
  - user
  - message
  - is_read

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- pip
- Virtual environment (recommended)

### Installation Steps

```bash
# Clone the repository
git clone <repository-url>
cd university_portal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (Admin)
python manage.py createsuperuser

# Run server
python manage.py runserver

```
# Project Tree

```
ZeroDay_Syndicate/
│
└── Deparment Level File Sharing Platform/
    │
    ├── manage.py
    ├── requirements.txt
    ├── README.md
    ├── db.sqlite3              ← (will be removed after MySQL switch)
    │
    ├── Secured_Moodle/         ← Django Project Config
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── accounts/               ← Authentication & Roles
    │   ├── migrations/
    │   ├── templates/
    │   │   └── accounts/
    │   │       ├── login.html
    │   │       ├── forgot_password.html
    │   │       ├── change_password.html
    │   │       └── profile.html
    │   ├── static/
    │   │   └── accounts/
    │   │       ├── css/
    │   │       │   └── auth.css
    │   │       └── js/
    │   │           └── auth.js
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py        ← UserProfile, roles
    │   ├── views.py         ← Login, logout, redirect
    │   ├── urls.py
    │   └── tests.py
    │
    ├── pages/                 ← Public Pages + Dashboards
    │   ├── templates/
    │   │   └── pages/
    │   │       ├── index.html
    │   │       ├── about.html
    │   │       ├── support.html
    │   │       ├── student_dashboard.html
    │   │       └── faculty_dashboard.html
    │   ├── views.py
    │   ├── urls.py
    │   └── apps.py
    │
    ├── notes/                 ← Notes Module
    │   ├── migrations/
    │   ├── templates/
    │   │   └── notes/
    │   │       ├── notes_list.html
    │   │       └── upload_note.html
    │   ├── admin.py
    │   ├── models.py        ← Notes + file_hash
    │   ├── views.py
    │   ├── urls.py
    │   └── validators.py    ← Magic byte + MIME checks
    │
    ├── assignments/          ← Assignment Module
    │   ├── migrations/
    │   ├── templates/
    │   │   └── assignments/
    │   │       ├── assignment_list.html
    │   │       ├── upload_assignment.html
    │   │       └── submit_assignment.html
    │   ├── admin.py
    │   ├── models.py        ← Assignment + Submission
    │   ├── views.py
    │   ├── urls.py
    │   └── validators.py    ← Hash + signature checks
    │
    ├── notifications/       ← Notification System
    │   ├── migrations/
    │   ├── models.py        ← Notification model
    │   ├── views.py
    │   ├── urls.py
    │   └── utils.py         ← Trigger notifications
    │
    ├── core/                ← Shared Security Utilities
    │   ├── utils/
    │   │   ├── file_hashing.py
    │   │   ├── magic_bytes.py
    │   │   └── permissions.py
    │   └── middleware.py
    │
    ├── templates/           ← Global Templates
    │   ├── base.html
    │   └── partials/
    │       ├── navbar.html
    │       └── footer.html
    │
    ├── static/              ← Global Static Files
    │   ├── css/
    │   │   └── main.css
    │   ├── js/
    │   │   └── loader.js
    │   └── images/
    │
    ├── media/               ← Uploaded Files
    │   ├── notes/
    │   └── assignments/
    │
    └── venv/                ← Virtual Environment

```

