# 🧠 CLI Personal Assistant

A powerful **Command-Line Interface (CLI)** personal assistant built with Python to help you manage:

- 📝 **Notes**
- ✅ **Tasks** (with due dates)
- 📅 **Google Calendar events**

This project is designed for **portfolio quality**, demonstrating **Python scripting, file handling, API integration (Google Calendar)**, and **CLI development**.

---

## 🚀 Features

### Notes
- Add, list, edit, and delete notes
- Stored in `storage/notes.json`

### Tasks
- Add, list, edit, and delete tasks
- Optional due date (`YYYY-MM-DD`)
- Stored in `storage/tasks.json`

### Google Calendar
- Add events to your Google Calendar
- List upcoming events
- Secure OAuth 2.0 authentication

---

## 📂 Project Structure

cli_assistant/
│
├── main.py # Main CLI entry point
├── notes.py # Notes management
├── tasks.py # Tasks management
├── calendar_integration.py # Google Calendar integration
├── utils.py # Reusable helper functions
├── storage/ # JSON storage for notes & tasks
├── requirements.txt # Dependencies
└── README.md # Project documentation

## 🛠 Installation

Set up Google Calendar API

Go to Google Cloud Console

Create a project and enable Google Calendar API

Create OAuth 2.0 credentials for a "Desktop App"

Download credentials.json and place it in the project root

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/cli_assistant.git
cd cli_assistant

pip install -r requirements.txt

python main.py add-note "Buy groceries"
python main.py list-notes
python main.py edit-note 1 "Buy groceries and milk"
python main.py delete-note 1

python main.py add-task "Finish portfolio" --due "2025-08-20"
python main.py list-tasks
python main.py edit-task 1 "Finish portfolio and deploy website"
python main.py delete-task 1

# Add a calendar event
python main.py add-event "Project Meeting" 2025-08-15T10:00:00 2025-08-15T11:00:00

# List upcoming events
python main.py list-events --max 5

python main.py add-note "Research API integration"
python main.py add-task "Complete CLI Assistant" --due "2025-08-18"
python main.py add-event "Team Meeting" 2025-08-15T14:00:00 2025-08-15T15:00:00
python main.py list-tasks
python main.py list-events
