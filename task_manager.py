import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        # Initialize the task manager with a file to save/load tasks
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        # Load tasks from the JSON file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        else:
            # If file doesn't exist, start with an empty list
            self.tasks = []

    def save_tasks(self):
        # Save the current list of tasks to the JSON file
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, description):
        # Add a new task with description and default status (not done)
        self.tasks.append({"desc": description, "done": False})
        self.save_tasks()

    def list_tasks(self):
        # Print all tasks with their status (done / not done)
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "[x]" if task["done"] else "[ ]"
                print(f"{i}. {status} {task['desc']}")

    def mark_done(self, index):
        # Mark a specific task as done
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def unmark_done(self, index):
        # Unmark (set as not done) a specific task
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["done"] = False
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        # Remove a task from the list
        if 1 <= index <= len(self.tasks):
            self.tasks.pop(index - 1)
            self.save_tasks()
        else:
            print("Invalid task number.")
