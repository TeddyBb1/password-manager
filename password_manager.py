import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from cryptography.fernet import Fernet

# Master password for authentication
MASTER_PASSWORD = "putYOURpassword"

# Encryption functions
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Database functions
def create_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (service TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_password(service, username, password):
    encrypted_password = encrypt_message(password)
    print(f"Encrypted password: {encrypted_password}")  # Check the encrypted password

    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (service, username, encrypted_password))
    conn.commit()
    conn.close()
    
    print("Password has been added to the database")

def get_all_passwords():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT service, username, password FROM passwords")
    result = c.fetchall()
    conn.close()
    print("Passwords retrieved:", result)  # Check the passwords retrieved from the database
    return result

# GUI functions
def show_passwords():
    for row in tree.get_children():
        tree.delete(row)
    passwords = get_all_passwords()
    for service, username, encrypted_password in passwords:
        try:
            password = decrypt_message(encrypted_password)
            print(f"Adding to table: {service}, {username}, {password}")  # Ensure decryption is correct
            tree.insert("", tk.END, values=(service, username, password))
        except Exception as e:
            print(f"Decryption error: {e}")  # Display any decryption errors

def add_password_window():
    def save_new_password():
        service = entry_service.get()
        username = entry_username.get()
        password = entry_password.get()
        if service and username and password:
            add_password(service, username, password)
            messagebox.showinfo("Success", "Password has been successfully saved!")
            add_window.destroy()
            show_passwords()
        else:
            messagebox.showwarning("Error", "All fields are required!")

    add_window = tk.Toplevel(root)
    add_window.title("Add a new password")

    tk.Label(add_window, text="Service:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(add_window, text="Username:").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(add_window, text="Password:").grid(row=2, column=0, padx=10, pady=10)

    entry_service = tk.Entry(add_window)
    entry_username = tk.Entry(add_window)
    entry_password = tk.Entry(add_window, show="*")

    entry_service.grid(row=0, column=1, padx=10, pady=10)
    entry_username.grid(row=1, column=1, padx=10, pady=10)
    entry_password.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_new_password).grid(row=3, column=0, columnspan=2, pady=10)

def login():
    if entry_password.get() == MASTER_PASSWORD:
        auth_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Error", "Incorrect password!")

def show_main_window():
    global root
    global tree

    root = tk.Tk()
    root.title("Password Manager")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    tree = ttk.Treeview(frame, columns=("Service", "Username", "Password"), show="headings")
    tree.heading("Service", text="Service")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")
    tree.pack()

    tk.Button(root, text="Add Password", command=add_password_window).pack(pady=20)

    show_passwords()
    root.mainloop()

def main():
    create_db()

    global auth_window
    global entry_password

    auth_window = tk.Tk()
    auth_window.title("Authentication")

    tk.Label(auth_window, text="Enter the password:").pack(pady=10)

    entry_password = tk.Entry(auth_window, show="*")
    entry_password.pack(pady=10)

    tk.Button(auth_window, text="Login", command=login).pack(pady=10)

    auth_window.mainloop()

if __name__ == "__main__":
    main()
