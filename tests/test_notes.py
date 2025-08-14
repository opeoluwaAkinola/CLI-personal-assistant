import os
import json
import notes

def setup_function():
    os.makedirs("storage", exist_ok=True)
    with open("storage/notes.json", "w") as f:
        json.dump([], f)

def test_add_note():
    notes.add_note("Test note")
    data = notes.load_notes()
    assert data[0]["content"] == "Test note"

def test_edit_note():
    notes.add_note("Old")
    notes.edit_note(1, "New")
    assert notes.load_notes()[0]["content"] == "New"

def test_delete_note():
    notes.add_note("To delete")
    notes.delete_note(1)
    assert len(notes.load_notes()) == 0
