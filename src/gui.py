import tkinter as tk
from tkinter import ttk
from api_handler import convert_currency as api_convert_currency
import matplotlib.pyplot as plt
from api_handler import convert_currency as api_convert_currency, get_historical_rates
import datetime
CURRENCY_LIST = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "PHP", "CHF", "CNY", "SEK", "NZD"]

def launch_gui(root):
    # Create a frame to organize layout with padding
    frame = tk.Frame(root, padx=30, pady=30, bg="#4fbc29") 
    frame.grid(sticky="nsew")

    label_font = ("Arial", 16, "bold")
    entry_font = ("Arial", 12)
    result_font = ("Arial", 12, "bold")

    # Amount input
    tk.Label(frame, text="Amount:").grid(row=0, column=0, sticky="e", pady=10)
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
    result_label = tk.Label(text="Result will appear here", font=("Arial", 12, "bold"))
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Convert button
    def convert_currency():
        amount = amount_entry.get()
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if amount =="":
            result_label.config(text="Please enter an amount" )
            return
        try:
            amount = float(amount)
        except ValueError:
            result_label.config(text="Invalid amount. Please enter a number.")
            return
        
        converted_amount = api_convert_currency(from_curr, to_curr, amount)

        if converted_amount:
            result_label.config(text=f"{amount} {from_curr} = {converted_amount} {to_curr}")
        else:
            result_label.config(text="Error fetching conversion data.")

    convert_btn = tk.Button(frame, text="Convert", command=convert_currency)
    convert_btn.grid(row=4, column=0, columnspan=2, pady=10)
    
    def plot_historical_graph(from_curr, to_curr):
        today = datetime.date.today()
        seven_days_ago = today - datetime.timedelta(days=7)
        start_date = seven_days_ago.strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")
        
        rates = get_historical_rates(from_curr, to_curr, start_date, end_date)
        if rates:
            dates = []
            values = []
            for date, rate_info in rates.items():
                dates.append(date)
                values.append(rate_info[to_curr])
                
                plt.figure(figsize=(8, 5), facecolor="#4fbc29")
                plt.plot(dates, values, marker='o', color="#ffffff", markerfacecolor="#ffffff")
                plt.title(f"Exchange Rate Trend: {from_curr} to {to_curr}", color="white")
                plt.xlabel("Date", color="white")
                plt.ylabel("Exchange Rate", color="white")
                plt.xticks(rotation=45, color="white")
                plt.yticks(color="white")
                plt.grid(True, color="white", linestyle="--", alpha=0.5)
                plt.tight_layout()
                plt.show()
        else:
            print("No historical data available.")


    # Optional: Center all columns equally
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

