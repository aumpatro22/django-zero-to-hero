# ⚡ Django Zero to Hero

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>
  <img src="https://img.shields.io/badge/Git-Active-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT"/>
</p>

<p align="center">
  <strong>An interactive, day-by-day learning journal mapping my progression from absolute beginner to advanced Django engineer.</strong>
</p>

<p align="center">
  <a href="#-learning-journal">Journal Logs</a> •
  <a href="#-repository-structure">Repository Structure</a> •
  <a href="#-quick-start">Quick Start</a>
</p>

---

## 🧭 Repository Mission
This repository serves as my developer diary. Each day, I build real features, learn core Django concepts, and log my debug history. The goal is to build deep conceptual muscle memory and establish excellent development habits.

---

## 📅 Learning Journal

Here is the progress tracker and index of my learning logs. Click on any day to see full notes, diagrams, and bug resolution logs:

| Day | Topic | Core Focus Areas | Status | Log Link |
| :---: | :--- | :--- | :---: | :---: |
| 🚀 **Day 1** | **Foundations & Routing** | Virtual Environments, Django Apps, Project-level vs App-level URL routing, View classes vs function views, Context Dictionaries, template rendering loops. | 🟢 Completed | [View Log 📝](file:///e:/vibe-Learning/Day-1/journal/day_1.md) |
| ⏳ **Day 2** | *Upcoming* | Database Models, Django ORM, Admin Panel | 🔴 Pending | — |
| ⏳ **Day 3** | *Upcoming* | Class-Based Views, Static File Handling | 🔴 Pending | — |

---

## 📂 Repository Structure

```directory
Day-1/
├── djnago/                  # Django project root
│   ├── core/                # Project configuration folder
│   ├── catalog/             # Product catalog application
│   ├── blog/                # Blog application
│   └── manage.py            # Django administration utility
├── journal/                 # Day-by-day developer logs
│   └── day_1.md             # Detailed log & bug report for Day 1
└── README.md                # Repository directory & hub (You are here)
```

---

## 🛠️ Quick Start

Want to run this project locally? Follow these steps:

### 1. Navigate to the project root
```bash
cd djnago
```

### 2. Activate the Virtual Environment
* **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
* **Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```

### 3. Start the Local Server
```bash
python manage.py runserver
```

Open your browser and visit: [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)

---

<p align="center">
  Made with ❤️ & curiosity. Follow along on my path to becoming a Django Hero!
</p>
