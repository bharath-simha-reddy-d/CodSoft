import tkinter as tk
from tkinter import messagebox
import json


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(title=data["title"], completed=data["completed"])


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.storage_file = "tasks.json"
        self.load_tasks()

        # GUI Components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=2, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=15, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.update_task_listbox()

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_task_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=10)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=2, column=2, padx=5, pady=10)

    def load_tasks(self):
        """Load tasks from the JSON storage file."""
        try:
            with open(self.storage_file, "r") as file:
                task_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in task_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON storage file."""
        with open(self.storage_file, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def add_task(self):
        """Add a new task."""
        task_title = self.task_entry.get().strip()
        if task_title:
            self.tasks.append(Task(title=task_title))
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")

    def update_task_listbox(self):
        """Refresh the task listbox to display the current tasks."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✔" if task.completed else "✘"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task.title} [{status}]")

    def mark_task_complete(self):
        """Mark the selected task as complete."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index].completed = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
