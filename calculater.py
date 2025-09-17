import tkinter as tk
from tkinter import messagebox
import math
import os

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.history_file = r"c:/Users/shravan singh/OneDrive/Desktop/python/projects/history.txt"
        self.history_win = None  

        # Entry_field
        input_frame = tk.Frame(self.root, bd=2, relief=tk.RAISED, bg="#1e1e2f")
        input_frame.pack(side=tk.TOP, pady=15)

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("Arial", 20, "bold"),
            bg="#2b2b3c",
            fg="white",
            bd=10,
            insertwidth=4,
            width=20,
            justify="right"
        )
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons_frame
        btns_frame = tk.Frame(self.root, bg="#1e1e2f")
        btns_frame.pack()

        # Button_layout
        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "+", "√", "^"],
            ["sin", "cos", "tan", "log", "e"],
            ["exp", "=", "DEL"],
            ["History"]
        ]

        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == "=":
                    self.create_button(btns_frame, button, i, j, colspan=2, width=15)
                elif button == "DEL":
                    self.create_button(btns_frame, button, i, j+1, colspan=2, width=15)
                    break
                elif button == "History":
                    self.create_button(btns_frame, button, i, j, colspan=5, width=40)
                else:
                    self.create_button(btns_frame, button, i, j)


    # Lopping over buttons to disp[lay on user's ui side

    def create_button(self, frame, text, row, col, colspan=1, width=6):
        btn = tk.Button(
            frame,
            text=text,
            width=width,
            height=2,
            bg="#2b2b3c",
            fg="white",
            font=("Arial", 14, "bold"),
            activebackground="#3b3b4f",
            activeforeground="yellow",
            relief="ridge",
            bd=3,
            command=lambda: self.on_button_click(text)
        )
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    # Button_Logic

    def on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
            self.input_text.set("")
        elif button_text == "=":
            try:
                result = str(eval(self.expression))
                record = self.expression + " = " + result
                self.save_history(record)  # save to file
                self.input_text.set(result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid Input")
                self.input_text.set("")
                self.expression = ""
        elif button_text == "√":
            try:
                result = str(math.sqrt(float(self.expression)))
                record = f"√({self.expression}) = {result}"
                self.save_history(record)
                self.input_text.set(result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid Input")
        elif button_text == "sin":
            self.expression = str(math.sin(math.radians(float(self.expression))))
            self.input_text.set(self.expression)
        elif button_text == "cos":
            self.expression = str(math.cos(math.radians(float(self.expression))))
            self.input_text.set(self.expression)
        elif button_text == "tan":
            self.expression = str(math.tan(math.radians(float(self.expression))))
            self.input_text.set(self.expression)
        elif button_text == "log":
            try:
                self.expression = str(math.log10(float(self.expression)))
                self.input_text.set(self.expression)
            except:
                messagebox.showerror("Error", "Invalid Input")
        elif button_text == "π":
            self.expression += str(math.pi)
            self.input_text.set(self.expression)
        elif button_text == "e":
            self.expression += str(math.e)
            self.input_text.set(self.expression)
        elif button_text == "^":
            self.expression += "**"
            self.input_text.set(self.expression)
        elif button_text == "exp":
            try:
                self.expression = str(math.exp(float(self.expression)))
                self.input_text.set(self.expression)
            except:
                messagebox.showerror("Error", "Invalid Input")
        elif button_text == "!":
            try:
                self.expression = str(math.factorial(int(self.expression)))
                self.input_text.set(self.expression)
            except:
                messagebox.showerror("Error", "Invalid Input")
        elif button_text == "DEL":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif button_text == "History":
            self.show_history()
        else:
            self.expression += str(button_text)
            self.input_text.set(self.expression)


    # Save history to file

    def save_history(self, record):
        with open(self.history_file, "a") as f:
            f.write(record + "\n")


    # Show history (from file)
    
    def show_history(self):
        if self.history_win is not None and tk.Toplevel.winfo_exists(self.history_win):
            self.refresh_history()
            return

        self.history_win = tk.Toplevel(self.root)
        self.history_win.title("Calculation History")
        self.history_win.geometry("400x400")
        self.history_win.configure(bg="#1e1e2f")

        label = tk.Label(self.history_win, text="History", font=("Arial", 16, "bold"),
                         bg="#1e1e2f", fg="white")
        label.pack(pady=10)

        self.text_area = tk.Text(self.history_win, font=("Arial", 12), bg="#2b2b3c", fg="white")
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        self.refresh_history()

        self.text_area.config(state=tk.DISABLED)

    def refresh_history(self):
        """Refreshes history window text area with updated file data"""
        if hasattr(self, "text_area"):
            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete("1.0", tk.END)

            if os.path.exists(self.history_file):
                with open(self.history_file, "r") as f:
                    data = f.read()
                    if data.strip():
                        self.text_area.insert(tk.END, data)
                    else:
                        self.text_area.insert(tk.END, "No history yet.")
            else:
                self.text_area.insert(tk.END, "No history yet.")

            self.text_area.config(state=tk.DISABLED)



# Run Calculator (Main code)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
