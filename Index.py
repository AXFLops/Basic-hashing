import tkinter as tk
from tkinter import messagebox
import hashlib

def hash_string(input_string):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the input string's bytes
    sha256_hash.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()
    
    return hex_digest

def generate_hash():
    input_string = entry.get()
    if input_string:
        hash_result = hash_string(input_string)
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, hash_result)
    else:
        messagebox.showwarning("Input Error", "Please enter a string to hash.")

# Initialize the main window
root = tk.Tk()
root.title("SHA-256 Hash Generator")
root.geometry("500x500")  # Set the window size

# Create and place the widgets
entry_label = tk.Label(root, text="Enter the string to hash:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

hash_button = tk.Button(root, text="Generate Hash", command=generate_hash)
hash_button.pack(pady=10)

result_label = tk.Label(root, text="SHA-256 Hash:")
result_label.pack(pady=5)

result_textbox = tk.Text(root, height=5, width=60)
result_textbox.pack(pady=5)

# Start the main event loop
root.mainloop()