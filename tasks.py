import json
import os
from datetime import datetime
from utils import success, error, info

TASKS_FILE = "storage/tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title, due=None):
    task = {"title": title, "completed": False}
    if due:
        try:
            task["due"] = datetime.strptime(due, "%Y-%m-%d").date().isoformat()
        except ValueError:
            error("Invalid date format. Use YYYY-MM-DD.")
            return
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    success("Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        info("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "⏳"
            due = f" (Due: {task['due']})" if "due" in task else ""
            print(f"{i}. {status} {task['title']}{due}")

def edit_task(index, new_title, new_due=None):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["title"] = new_title
        if new_due:
            try:
                tasks[index-1]["due"] = datetime.strptime(new_due, "%Y-%m-%d").date().isoformat()
            except ValueError:
                error("Invalid date format. Use YYYY-MM-DD.")
                return
        save_tasks(tasks)
        success("Task updated.")
    else:
        error("Invalid task index.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        success(f"Deleted task: {removed['title']}")
    else:
        error("Invalid task index.")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["completed"] = True
        save_tasks(tasks)
        success(f"Marked task '{tasks[index-1]['title']}' as complete.")
    else:
        error("Invalid task index.")
