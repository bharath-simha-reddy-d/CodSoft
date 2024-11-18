import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables
        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()

        # GUI Components
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Spinbox(root, from_=4, to=64, textvariable=self.password_length, width=10).grid(row=0, column=1, padx=10, pady=5)

        tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=self.include_uppercase).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=self.include_lowercase).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Digits (0-9)", variable=self.include_digits).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Special (!@#$%^&*)", variable=self.include_special).grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Entry(root, textvariable=self.generated_password, state="readonly", width=40).grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        """Generate a random password based on user settings."""
        length = self.password_length.get()
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        character_pool = ""
        if self.include_uppercase.get():
            character_pool += string.ascii_uppercase
        if self.include_lowercase.get():
            character_pool += string.ascii_lowercase
        if self.include_digits.get():
            character_pool += string.digits
        if self.include_special.get():
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showerror("Error", "You must select at least one character type.")
            return

        password = "".join(random.choices(character_pool, k=length))
        self.generated_password.set(password)

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard."""
        password = self.generated_password.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()  # Update the clipboard content
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
