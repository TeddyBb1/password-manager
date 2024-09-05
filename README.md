# 🔐 Password Manager - Simple and Secure Password Management

**Password Manager** is a simple and effective tool for managing your passwords. With this program, you can securely store all your passwords in an encrypted database and access them by entering a master password.

### Features:

- **🔒 Secure Storage**: Passwords are encrypted using a unique key and stored in a local database.
- **💻 User-Friendly Interface**: The program offers a simple, easy-to-use interface for managing your passwords.
- **🔑 Secure Authentication**: Access to all passwords is protected by a master password, known only by you.

---

### 🚀 Installation and Usage Guide

Follow the steps below to set up and use this Password Manager on your system:

### 1. Clone the Repository

First, clone this repository to your computer:

```bash
git clone https://github.com/TeddyBb1/password-manager.git
cd password-manager
```

### 2. Set Up Your Development Environment

If you don't already have Python installed on your computer, download and install it from the [official website](https://www.python.org/).

Make sure you have `pip` and `virtualenv` installed. To install these tools, use the following commands:

```bash
pip install virtualenv
```

Create and activate a virtual environment (optional but recommended):

```bash
virtualenv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install all necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file does not exist, you can manually install the required library:

```bash
pip install cryptography
```

### 4. Set Up the Project

- **Open the project** in your preferred editor. If you are using Visual Studio Code, you can open the project as follows:

  1. Open Visual Studio Code.
  2. Select "File" > "Open Folder..." and navigate to the project folder.
  3. In this folder, create a new file `password_manager.py` and insert the source code.

- **Generate the encryption key** (only on the first run). Run the following code to create the key necessary for encrypting and decrypting passwords:

  ```python
  import cryptography
  from cryptography.fernet import Fernet

  def generate_key():
      key = Fernet.generate_key()
      with open("key.key", "wb") as key_file:
          key_file.write(key)

  generate_key()
  ```

### 5. Run the Program

Now, to run the application, open a terminal in the project directory and execute:

```bash
python password_manager.py
```

### 6. Create an Executable (.exe)

If you want to create an executable file for your application, use `PyInstaller`. Make sure `PyInstaller` is installed:

```bash
pip install pyinstaller
```

Then, run the following command to generate an executable without a console window:

```bash
pyinstaller --onefile --windowed password_manager.py
```

The executable file will be generated in the `dist` folder within your project directory. You can distribute this file to other Windows systems without needing Python installed.

### 7. Using the Application

1. **🔑 Authentication**: When you open the application, you will be prompted to enter the master password. Enter `"putYOURpassword"` to access your stored passwords.
2. **🗄️ Manage Passwords**: After authentication, you can view all your passwords in an easy-to-use table. You can add new passwords by clicking the "Add Password" button.

---

With this Password Manager, your passwords are protected and accessible only to you. Simple to use, secure, and efficient, it’s the ideal solution for managing passwords safely! 🔐

---
