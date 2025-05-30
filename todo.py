import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks_gui.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List (GUI)")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = self.load_tasks()

        self.title_label = tk.Label(root, text="My Tasks", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, fill=tk.X, padx=20)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 14), selectmode=tk.SINGLE, width=30, height=10)
        self.task_listbox.pack(pady=10)

        self.complete_btn = tk.Button(root, text="Mark Completed", command=self.mark_complete)
        self.complete_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(pady=5)

        self.refresh_tasks()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(FILENAME, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"title": task_text, "done": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.refresh_tasks()
        else:
            messagebox.showinfo("No selection", "Please select a task to mark as completed.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.refresh_tasks()
        else:
            messagebox.showinfo("No selection", "Please select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display = task['title']
            if task['done']:
                display = f"✔ {display}"
            self.task_listbox.insert(tk.END, display)

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
