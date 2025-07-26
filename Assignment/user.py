import sqlite3
import hashlib
import getpass

conn = sqlite3.connect("rd.db")

conn.execute('''
    CREATE TABLE IF NOT EXISTS user (
        username VARCHAR(100) PRIMARY KEY NOT NULL,
        password VARCHAR(100) NOT NULL,
        is_log_in INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()

def hashpassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_anyone_logged_in():
    result = conn.execute('SELECT is_log_in FROM user WHERE is_log_in = 1').fetchone()
    return result is not None

def register():
    if is_anyone_logged_in():
        print("A user is currently logged in. Please log out before registering a new user.")
        return

    username = input("Enter Username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashpassword(password)

    try:
        conn.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try again.")

def login():
    if is_anyone_logged_in():
        print("A user is already logged in. Please log out before logging in again.")
        return

    username = input("Enter Username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashpassword(password)

    result = conn.execute('SELECT password FROM user WHERE username = ?', (username,)).fetchone()

    if result:
        db_password = result[0]
        if db_password == hashed_password:
            conn.execute('UPDATE user SET is_log_in = 1 WHERE username = ?', (username,))
            conn.commit()
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

def logout():
    if is_anyone_logged_in():
        conn.execute('UPDATE user SET is_log_in = 0 WHERE is_log_in = 1')
        conn.commit()
        print("Logout successful!")
    else:
        print("No user is currently logged in.")

def change():
    username = input("Enter your username: ")
    current_password = getpass.getpass("Enter your current password: ")
    new_password = getpass.getpass("Enter your new password: ")
    
    hashed_current_password = hashpassword(current_password)
    hashed_new_password = hashpassword(new_password)

    result = conn.execute('SELECT password, is_log_in FROM user WHERE username = ?', (username,)).fetchone()

    if result:
        stored_password, is_logged_in = result
        if is_logged_in == 1:
            if stored_password == hashed_current_password:
                conn.execute('UPDATE user SET password = ? WHERE username = ?', (hashed_new_password, username))
                conn.commit()
                print("Password changed successfully!")
            else:
                print("Current password is incorrect.")
        else:
            print("User is not logged in.")
    else:
        print("Username not found.")

while True:
    print("\nUser Management System")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Change Password")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        logout()
    elif choice == '4':
        change()
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")

conn.commit()
conn.close()
