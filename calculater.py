import tkinter as tk
from tkinter import messagebox
import math

# -------------------------------
# Main Calculator Class
# -------------------------------
class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry field
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

        # Buttons frame
        btns_frame = tk.Frame(self.root, bg="#1e1e2f")
        btns_frame.pack()

        # Button layout
        buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "+", "√", "^"],
            ["sin", "cos", "tan", "log", "e"],
            ["exp", "=", "DEL"]
        ]

        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == "=":
                    self.create_button(btns_frame, button, i, j, colspan=2, width=15)
                elif button == "DEL":
                    self.create_button(btns_frame, button, i, j+1, colspan=2, width=15)
                    break
                else:
                    self.create_button(btns_frame, button, i, j)

    # -------------------------------
    # Button Creation
    # -------------------------------
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

    # -------------------------------
    # Button Logic
    # -------------------------------
    def on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
            self.input_text.set("")
        elif button_text == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid Input")
                self.input_text.set("")
                self.expression = ""
        elif button_text == "√":
            try:
                result = str(math.sqrt(float(self.expression)))
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
        else:
            self.expression += str(button_text)
            self.input_text.set(self.expression)

# -------------------------------
# Run Calculator
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
