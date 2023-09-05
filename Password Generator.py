import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.root.geometry("400x300") 

        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 16)) 
        self.length_label.pack(pady=10)
        
        self.length_entry = tk.Entry(root, font=("Helvetica", 14)) 
        self.length_entry.pack(pady=5)

        self.complexity_label = tk.Label(root, text="Password Complexity:", font=("Helvetica", 16))  
        self.complexity_label.pack(pady=5)
        
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, *self.complexity_options)
        self.complexity_menu.config(font=("Helvetica", 14)) 
        self.complexity_menu.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 14))  
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()
        
        if complexity == "Low":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text="Generated Password: " + password)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
