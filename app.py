import tkinter as tk
from tkinter import messagebox
from db import init_db, save_to_db, fetch_history

# Initialize DB
init_db()

def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))  # ⚠️ simple eval, safe for local use
        save_to_db(expression, result)
        messagebox.showinfo("Result", f"{expression} = {result}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")

def show_history():
    records = fetch_history()
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    for expr, res in records:
        tk.Label(history_window, text=f"{expr} = {res}").pack()

# UI Setup
root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_eval = tk.Button(root, text="Calculate", command=evaluate_expression, width=15, height=2)
btn_eval.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

btn_history = tk.Button(root, text="History", command=show_history, width=15, height=2)
btn_history.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
btn_exit.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
