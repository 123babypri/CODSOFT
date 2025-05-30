import tkinter as tk
from tkinter import messagebox, simpledialog

# In-memory contact storage
contacts = {}

# GUI Functions

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    if name in contacts:
        messagebox.showinfo("Info", "Contact already exists. Use update.")
        return

    contacts[name] = {"phone": phone, "email": email}
    messagebox.showinfo("Success", f"Contact '{name}' added.")
    clear_entries()
    refresh_contact_list()

def update_contact():
    name = name_entry.get().strip()

    if name not in contacts:
        messagebox.showerror("Not Found", "Contact does not exist.")
        return

    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    contacts[name] = {"phone": phone, "email": email}
    messagebox.showinfo("Updated", f"Contact '{name}' updated.")
    clear_entries()
    refresh_contact_list()

def delete_contact():
    name = name_entry.get().strip()

    if name not in contacts:
        messagebox.showerror("Not Found", "Contact not found.")
        return

    del contacts[name]
    messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    clear_entries()
    refresh_contact_list()

def search_contact():
    name = name_entry.get().strip()

    if name not in contacts:
        messagebox.showinfo("Not Found", "Contact not found.")
        return

    contact = contacts[name]
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])

def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in sorted(contacts.keys()):
        contact_listbox.insert(tk.END, name)

def show_contact_details(event):
    selection = contact_listbox.curselection()
    if not selection:
        return
    name = contact_listbox.get(selection[0])
    contact = contacts.get(name, {})
    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(fill="x", padx=10)

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, font=("Arial", 14))
phone_entry.pack(fill="x", padx=10)

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, font=("Arial", 14))
email_entry.pack(fill="x", padx=10, pady=(0, 10))

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Search", width=10, command=search_contact).grid(row=0, column=3, padx=5)

# Contact List
tk.Label(root, text="Contact List").pack(pady=(10, 0))
contact_listbox = tk.Listbox(root, font=("Arial", 12), height=10)
contact_listbox.pack(fill="both", padx=10, pady=5, expand=True)
contact_listbox.bind('<<ListboxSelect>>', show_contact_details)

# Run the application
refresh_contact_list()
root.mainloop()
