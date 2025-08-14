import argparse
from notes import add_note, list_notes, edit_note, delete_note
from tasks import add_task, list_tasks, edit_task, delete_task, complete_task
from calendar_integration import list_calendar_events, add_calendar_event
import datetime

def main():
    parser = argparse.ArgumentParser(description="CLI Personal Assistant")
    subparsers = parser.add_subparsers(dest="command")

    # Notes
    subparsers.add_parser("list-notes", help="List all notes")
    add_note_cmd = subparsers.add_parser("add-note", help="Add a new note")
    add_note_cmd.add_argument("content")

    edit_note_cmd = subparsers.add_parser("edit-note", help="Edit a note")
    edit_note_cmd.add_argument("index", type=int)
    edit_note_cmd.add_argument("content")

    del_note_cmd = subparsers.add_parser("delete-note", help="Delete a note")
    del_note_cmd.add_argument("index", type=int)

    # Tasks
    subparsers.add_parser("list-tasks", help="List all tasks")
    add_task_cmd = subparsers.add_parser("add-task", help="Add a new task")
    add_task_cmd.add_argument("title")
    add_task_cmd.add_argument("--due")

    edit_task_cmd = subparsers.add_parser("edit-task", help="Edit a task")
    edit_task_cmd.add_argument("index", type=int)
    edit_task_cmd.add_argument("title")
    edit_task_cmd.add_argument("--due")

    del_task_cmd = subparsers.add_parser("delete-task", help="Delete a task")
    del_task_cmd.add_argument("index", type=int)

    complete_task_cmd = subparsers.add_parser("complete-task", help="Mark a task complete")
    complete_task_cmd.add_argument("index", type=int)

    calendar_list_cmd = subparsers.add_parser("list-events", help="List upcoming Google Calendar events")
    calendar_list_cmd.add_argument("--max", type=int, default=10, help="Max events to show")

    calendar_add_cmd = subparsers.add_parser("add-event", help="Add a new Google Calendar event")
    calendar_add_cmd.add_argument("summary", help="Event title")
    calendar_add_cmd.add_argument("start", help="Start time (YYYY-MM-DDTHH:MM:SS)")
    calendar_add_cmd.add_argument("end", help="End time (YYYY-MM-DDTHH:MM:SS)")

    args = parser.parse_args()

    if args.command == "add-note":
        add_note(args.content)
    elif args.command == "list-notes":
        list_notes()
    elif args.command == "edit-note":
        edit_note(args.index, args.content)
    elif args.command == "delete-note":
        delete_note(args.index)
    elif args.command == "add-task":
        add_task(args.title, args.due)
    elif args.command == "list-tasks":
        list_tasks()
    elif args.command == "edit-task":
        edit_task(args.index, args.title, args.due)
    elif args.command == "delete-task":
        delete_task(args.index)
    elif args.command == "complete-task":
        complete_task(args.index)
    elif args.command == "list-events":
        list_calendar_events(args.max)
    elif args.command == "add-event":
        add_calendar_event(args.summary, args.start, args.end)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
