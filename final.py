import tkinter as tk
from tkinter import messagebox
import sqlite3

# Set up database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL)''')
conn.commit()
conn.close()

# Set up Tkinter GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
bg_color = "#003049"  # Dark blue
fg_color = "#f4f1de"  # beige
root.config(bg=bg_color)

# Title Label
title_label = tk.Label(root, text="My To-Do List", bg=bg_color, fg=fg_color, font=("nunito", 20))
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task
def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showwarning("Warning", "You must enter a task.")
    else:
        conn = sqlite3.connect('todo_list.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, 'Pending'))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)
        display_tasks()

# Delete Task
def delete_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        task_text = selected_task.split(" - ")[0]
        conn = sqlite3.connect('todo_list.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE task=?", (task_text,))
        conn.commit()
        conn.close()
        display_tasks()

# Mark as Done
def mark_as_done():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        task_text = selected_task.split(" - ")[0]
        conn = sqlite3.connect('todo_list.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = 'Done' WHERE task=?", (task_text,))
        conn.commit()
        conn.close()
        display_tasks()

# Remove Done Tasks
def remove_done_tasks():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE status='Done'")
    conn.commit()
    conn.close()
    display_tasks()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg=fg_color, fg=bg_color)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=fg_color, fg=bg_color)
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", command=mark_as_done, bg=fg_color, fg=bg_color)
done_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Done Tasks", command=remove_done_tasks, bg=fg_color, fg=bg_color)
remove_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, height=15, width=50, bg=fg_color, fg=bg_color)
task_listbox.pack(pady=10)

# Display Tasks
def display_tasks():
    task_listbox.delete(0, tk.END)
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute("SELECT task, status FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        task_display = f"{task[0]} - [{task[1]}]"
        task_listbox.insert(tk.END, task_display)
    conn.close()

# Load tasks on startup
display_tasks()

# Run the Tkinter loop
root.mainloop()
