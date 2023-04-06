from db import *
import json

# from gui import load_register

# (
#     username_entry,
#     password_entry,
#     remember_me_toggle,
#     register_button,
#     login_button,
#     window,
# ) = load_register()


# def register_user():
#     username = username_entry.get()
#     password = password_entry.get()
#     remember_me = remember_me_toggle.custom_value

#     # Read data.json
#     with open("data.json", "r") as f:
#         data = json.load(f)

#     # Print out the user created
#     print(add_new_user(User(username=username, password=password)))

#     # Save data to data.json
#     data["remember_me"] = remember_me
#     data["user"] = {"username": username, "password": str(hash_password(password))}

#     with open("data.json", "w") as f:
#         json.dump(data, f, indent=4)


# register_button.configure(command=register_user)

# window.mainloop()

from tkinter import Tk
from gui import load_register, load_login

window = Tk()
window.geometry("864x558")
window.configure(bg="#FFFFFF")

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Register
username_entry, password_entry, remember_me_toggle, register_button, login_text_button = load_register(window)

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    remember_me = remember_me_toggle.custom_value

    # Read data.json
    with open("data.json", "r") as f:
        data = json.load(f)

    # Print out the user created
    print(add_new_user(User(username=username, password=password)))

    # Save data to data.json
    data["remember_me"] = remember_me
    data["user"] = {"username": username, "password": str(hash_password(password))}

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def go_to_login():
    global username_entry, password_entry, remember_me_toggle, register_button, login_text_button
    clear_window()
    username_entry, password_entry, remember_me_toggle, register_button, login_text_button = load_login(window)

register_button.configure(command=register_user)
login_text_button.configure(command=go_to_login)

# Login
login_button = register_button
register_text_button = login_text_button



window.resizable(False, False)
window.mainloop()