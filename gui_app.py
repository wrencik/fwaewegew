import tkinter as tk
from tkinter import messagebox, ttk


class SimpleFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Form Application")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = ttk.Label(main_frame, text="User Information Form", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(main_frame, text="Full Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(main_frame, text="Email:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(main_frame, width=30)
        self.email_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(main_frame, text="Age:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(main_frame, width=30)
        self.age_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(main_frame, text="Number 1:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.num1_entry = ttk.Entry(main_frame, width=30)
        self.num1_entry.grid(row=4, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(main_frame, text="Number 2:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.num2_entry = ttk.Entry(main_frame, width=30)
        self.num2_entry.grid(row=5, column=1, pady=5, padx=(10, 0))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        submit_btn = ttk.Button(button_frame, text="Submit Form", command=self.submit_form)
        submit_btn.grid(row=0, column=0, padx=5)
        
        calculate_btn = ttk.Button(button_frame, text="Calculate Sum", command=self.calculate_sum)
        calculate_btn.grid(row=0, column=1, padx=5)
        
        clear_btn = ttk.Button(button_frame, text="Clear All", command=self.clear_form)
        clear_btn.grid(row=0, column=2, padx=5)
        
        ttk.Label(main_frame, text="Results:", font=('Arial', 12, 'bold')).grid(
            row=7, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        
        self.result_text = tk.Text(main_frame, height=6, width=50, wrap=tk.WORD)
        self.result_text.grid(row=8, column=0, columnspan=2, pady=5)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=8, column=2, sticky=(tk.N, tk.S))
        self.result_text.config(yscrollcommand=scrollbar.set)
    
    def submit_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        age = self.age_entry.get().strip()
        
        if not name:
            messagebox.showwarning("Validation Error", "Please enter your name.")
            return
        
        if not email:
            messagebox.showwarning("Validation Error", "Please enter your email.")
            return
        
        if not age:
            messagebox.showwarning("Validation Error", "Please enter your age.")
            return
        
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                messagebox.showerror("Validation Error", "Please enter a valid age (0-150).")
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Age must be a number.")
            return
        
        result = f"Form Submitted Successfully!\n"
        result += f"{'=' * 40}\n"
        result += f"Name: {name}\n"
        result += f"Email: {email}\n"
        result += f"Age: {age_int}\n"
        result += f"{'=' * 40}\n"
        
        if age_int < 18:
            result += "Status: Minor\n"
        elif age_int < 65:
            result += "Status: Adult\n"
        else:
            result += "Status: Senior\n"
        
        self.display_result(result)
        messagebox.showinfo("Success", "Form submitted successfully!")
    
    def calculate_sum(self):
        num1_str = self.num1_entry.get().strip()
        num2_str = self.num2_entry.get().strip()
        
        if not num1_str or not num2_str:
            messagebox.showwarning("Validation Error", "Please enter both numbers.")
            return
        
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
            
            result = f"Calculation Results:\n"
            result += f"{'=' * 40}\n"
            result += f"Number 1: {num1}\n"
            result += f"Number 2: {num2}\n"
            result += f"{'=' * 40}\n"
            result += f"Sum: {num1 + num2}\n"
            result += f"Difference: {num1 - num2}\n"
            result += f"Product: {num1 * num2}\n"
            if num2 != 0:
                result += f"Division: {num1 / num2:.2f}\n"
            else:
                result += "Division: Cannot divide by zero\n"
            
            self.display_result(result)
            
        except ValueError:
            messagebox.showerror("Validation Error", "Please enter valid numbers.")
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
    
    def display_result(self, message):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, message)


def main():
    root = tk.Tk()
    app = SimpleFormApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
