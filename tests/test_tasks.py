import os
import json
import tasks

def setup_function():
    os.makedirs("storage", exist_ok=True)
    with open("storage/tasks.json", "w") as f:
        json.dump([], f)

def test_add_task():
    tasks.add_task("Test task")
    data = tasks.load_tasks()
    assert data[0]["title"] == "Test task"

def test_edit_task():
    tasks.add_task("Old task")
    tasks.edit_task(1, "New task")
    assert tasks.load_tasks()[0]["title"] == "New task"

def test_delete_task():
    tasks.add_task("Delete me")
    tasks.delete_task(1)
    assert len(tasks.load_tasks()) == 0

def test_complete_task():
    tasks.add_task("Complete me")
    tasks.complete_task(1)
    assert tasks.load_tasks()[0]["completed"] is True
