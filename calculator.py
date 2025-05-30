import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Input Error", "Invalid expression!")
        entry.delete(0, tk.END)

# Function to update the entry widget with button text
def press(key):
    entry.insert(tk.END, key)

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# GUI Window setup
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for input and output
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: press(x) if x != '=' else calculate()
        tk.Button(frame, text=btn, font=("Arial", 18), command=action).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(root, text="Clear", font=("Arial", 16), bg="red", fg="white", command=clear).pack(fill="both", padx=10, pady=5)

# Run the main loop
root.mainloop()
