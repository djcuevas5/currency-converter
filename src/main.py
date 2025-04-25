import tkinter as tk
from gui import launch_gui

def main():
    root = tk.Tk()
    print("Window is loading...")  # Debug line
    root.title("Smart Currency Converter")
    root.geometry("255x270")
    launch_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
