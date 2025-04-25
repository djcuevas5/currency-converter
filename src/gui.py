import tkinter as tk
from tkinter import ttk

CURRENCY_LIST = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "PHP", "CHF", "CNY", "SEK", "NZD"]

def launch_gui(root):
    # Create a frame to organize layout with padding
    frame = tk.Frame(root, padx=20, pady=20)
    frame.grid()

    # Amount input
    tk.Label(frame, text="Amount:").grid(row=0, column=0, sticky="e", pady=15)
    amount_entry = tk.Entry(frame)
    amount_entry.grid(row=0, column=1, pady=5)

    # From currency
    tk.Label(frame, text="From:").grid(row=1, column=0, sticky="e", pady=15)
    from_currency = ttk.Combobox(frame, values=CURRENCY_LIST, state="readonly")
    from_currency.current(0)
    from_currency.grid(row=1, column=1, pady=5)

    # To currency
    tk.Label(frame, text="To:").grid(row=2, column=0, sticky="e", pady=5)
    to_currency = ttk.Combobox(frame, values=CURRENCY_LIST, state="readonly")
    to_currency.current(1)
    to_currency.grid(row=2, column=1, pady=5)

    # Result label
    result_label = tk.Label(frame, text="Result will appear here", font=("Arial", 12, "bold"))
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Convert button
    def convert_currency():
        amount = amount_entry.get()
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result_label.config(text=f"Converting {amount} {from_curr} to {to_curr}...")

    convert_btn = tk.Button(frame, text="Convert", command=convert_currency)
    convert_btn.grid(row=4, column=0, columnspan=2, pady=10)

    # Optional: Center all columns equally
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
