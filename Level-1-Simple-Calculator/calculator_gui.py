"""
Simple Calculator - GUI Version with Tkinter
Codveda Technology - Python Development Internship
Task: Level 1 - Simple Calculator

A beautiful graphical calculator with modern design
"""

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator - Codveda")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Variables
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        """Create all calculator widgets"""
        
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#1e1e1e", height=60)
        header_frame.pack(fill=tk.X, pady=10)
        
        title_label = tk.Label(
            header_frame,
            text="🔢 CALCULATOR",
            font=("Arial", 16, "bold"),
            bg="#1e1e1e",
            fg="#00ff88"
        )
        title_label.pack()
        
        # Display Frame
        display_frame = tk.Frame(self.root, bg="#2d2d2d", bd=2, relief=tk.RIDGE)
        display_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        # Expression Display
        self.expr_label = tk.Label(
            display_frame,
            text="",
            font=("Arial", 12),
            bg="#2d2d2d",
            fg="#888888",
            anchor="e",
            height=1
        )
        self.expr_label.pack(fill=tk.BOTH, padx=10, pady=(10, 0))
        
        # Result Display
        result_display = tk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 28, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify="right",
            state="readonly"
        )
        result_display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        # Button colors
        special_buttons = {'C': '#ff4444', '=': '#00ff88', '⌫': '#ff9800'}
        operator_buttons = {'/', '*', '-', '+', '%'}
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                # Determine button color
                if btn_text in special_buttons:
                    bg_color = special_buttons[btn_text]
                    fg_color = "#ffffff"
                elif btn_text in operator_buttons:
                    bg_color = "#ff9800"
                    fg_color = "#ffffff"
                else:
                    bg_color = "#3d3d3d"
                    fg_color = "#ffffff"
                
                btn = tk.Button(
                    buttons_frame,
                    text=btn_text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=bg_color,
                    activeforeground=fg_color,
                    bd=0,
                    cursor="hand2",
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="#CodvedaJourney | Python Internship",
            font=("Arial", 9),
            bg="#1e1e1e",
            fg="#666666"
        )
        footer_label.pack(pady=5)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.calculate()
        elif char == '±':
            self.toggle_sign()
        else:
            self.append_char(char)
    
    def append_char(self, char):
        """Append character to expression"""
        self.expression += str(char)
        self.expr_label.config(text=self.expression)
        self.result_var.set(self.expression)
    
    def clear(self):
        """Clear the calculator"""
        self.expression = ""
        self.result_var.set("0")
        self.expr_label.config(text="")
    
    def backspace(self):
        """Remove last character"""
        self.expression = self.expression[:-1]
        if self.expression:
            self.result_var.set(self.expression)
            self.expr_label.config(text=self.expression)
        else:
            self.result_var.set("0")
            self.expr_label.config(text="")
    
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        if self.expression and self.expression[0] == '-':
            self.expression = self.expression[1:]
        elif self.expression:
            self.expression = '-' + self.expression
        
        if self.expression:
            self.result_var.set(self.expression)
            self.expr_label.config(text=self.expression)
    
    def calculate(self):
        """Evaluate the expression"""
        if not self.expression:
            return
        
        try:
            # Check for division by zero
            if '/0' in self.expression.replace(' ', ''):
                messagebox.showerror(
                    "Error",
                    "❌ Division by zero is not allowed!"
                )
                return
            
            # Evaluate expression
            result = eval(self.expression)
            
            # Format result
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
            
            # Update display
            self.expr_label.config(text=f"{self.expression} =")
            self.result_var.set(str(result))
            self.expression = str(result)
            
        except ZeroDivisionError:
            messagebox.showerror(
                "Error",
                "❌ Division by zero is not allowed!"
            )
            self.clear()
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"❌ Invalid expression!\n{str(e)}"
            )
            self.clear()


def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
