import json
import os
from utils import success, error, info

NOTES_FILE = "storage/notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(content):
    notes = load_notes()
    notes.append({"content": content})
    save_notes(notes)
    success("Note added.")

def list_notes():
    notes = load_notes()
    if not notes:
        info("No notes yet.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note['content']}")

def edit_note(index, new_content):
    notes = load_notes()
    if 0 < index <= len(notes):
        notes[index-1]["content"] = new_content
        save_notes(notes)
        success("Note updated.")
    else:
        error("Invalid note index.")

def delete_note(index):
    notes = load_notes()
    if 0 < index <= len(notes):
        removed = notes.pop(index-1)
        save_notes(notes)
        success(f"Deleted note: {removed['content']}")
    else:
        error("Invalid note index.")
