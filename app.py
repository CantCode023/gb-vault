from tkinter import Tk
from gui import load_register as start_app, load_home
import json
from db import *
from db.exceptions import *

window = Tk()
window.geometry("864x558")
window.configure(bg="#FFFFFF")
window.title("GBVault")
window.iconbitmap("./assets/icon.ico")

with open("data.json", "r") as f:
    data = json.load(f)

if data["remember_me"]:
    try:
        user = get_user_from_username(data["user"]["username"])

        # If password entered is correct
        if str(data["user"]["password"]) == str(user.password):
            print("Account remembered!")
            load_home(window, user)
        else:
            start_app(window)
    except UserNotFound:
        print("User not found!")
        start_app(window)
else:
    start_app(window)

# return (
#     entry_2, # Username entry
#     entry_1, # Password entry
#     button_1, # Remember me toggle
#     button_2, # Register button
#     button_3 # Login text button
# )

window.resizable(False, False)
window.mainloop()