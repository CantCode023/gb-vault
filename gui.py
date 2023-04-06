from __future__ import annotations
from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage
from db import *
from db.exceptions import *
import json
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\cantc\OneDrive\Desktop\Coding\Python\gb-vault\build\assets"
)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_register(window):
    canvas = Canvas(window,
        bg="#FFFFFF",
        height=558,
        width=864,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    window.image_image_1 = image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    window.image_image_2 = image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    window.entry_image_1 = entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.place(x=0, y=0)
    canvas.create_image(257.0, 279.0, image=image_image_1)
    canvas.create_image(509.0, 279.0, image=image_image_2)

    canvas.create_text(
        509.0,
        81.0,
        anchor="nw",
        text="Register",
        fill="#71008F",
        font=("Poppins Medium", 40 * -1),
    )

    canvas.create_text(
        509.0,
        240.0,
        anchor="nw",
        text="Password",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    canvas.create_image(663.5, 286.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#fff", fg="#000716", font=("Poppins", -12))
    entry_1.place(x=524.0, y=266.0, width=279.0, height=43.0)

    window.button_image_1 = button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    window.button_image_1_2 = button_image_1_2 = PhotoImage(file=relative_to_assets("button_1_2.png"))


    def change_image():
        button_1.custom_value = not button_1.custom_value
        if button_1.custom_value:
            button_1.config(image=button_image_1)
        else:
            button_1.config(image=button_image_1_2)


    button_1 = Button(
        image=button_image_1_2,
        borderwidth=0,
        highlightthickness=0,
        command=change_image,
        relief="sunken",
    )
    button_1.custom_value = False
    button_1.place(x=509.0, y=321.5, width=25.0, height=25.0)

    canvas.create_text(
        545.0,
        325.0,
        anchor="nw",
        text="Remember Me",
        fill="#A5A5A5",
        font=("Poppins Medium", 12 * -1),
    )

    def register_user():
        username = entry_2.get()
        password = entry_1.get()
        remember_me = button_1.custom_value

        # Read data.json
        with open("data.json", "r") as f:
            data = json.load(f)

        # Print out the user created
        print(add_new_user(User(username=username, password=password)))

        if remember_me:
            # Save data to data.json
            data["remember_me"] = remember_me
            data["user"] = {"username": username, "password": str(hash_password(password))}

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        go_to_login()

    window.button_image_2 = button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="sunken",
        command=register_user
    )
    button_2.place(x=554.0, y=387.5, width=220.0, height=45.5)

    canvas.create_text(
        546.0,
        452.0,
        anchor="nw",
        text="Got an account already?",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    def go_to_login():
        for widget in window.winfo_children():
            widget.destroy()
        load_login(window)

    window.button_image_3 = button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        relief="sunken",
        command=go_to_login
    )
    button_3.place(x=739.0, y=452.0, width=44.0, height=22.0)

    canvas.create_image(663.5, 186.0, image=entry_image_1)
    entry_2 = Entry(
        bd=0,
        bg="#fff",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", -12),
    )
    entry_2.place(x=524.0, y=164.0, width=279.0, height=44.0)

    canvas.create_text(
        509.0,
        140.0,
        anchor="nw",
        text="Username",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    return (
        entry_2, # Username entry
        entry_1, # Password entry
        button_1, # Remember me toggle
        button_2, # Register button
        button_3 # Login text button
    )

def load_login(window):
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=558,
        width=864,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvas.place(x=0, y=0)
    window.image_image_1 = image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(257.0, 279.0, image=image_image_1)

    window.image_image_2 = image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(509.0, 279.0, image=image_image_2)

    canvas.create_text(
        509.0,
        81.0,
        anchor="nw",
        text="Login",
        fill="#71008F",
        font=("Poppins Medium", 40 * -1),
    )

    canvas.create_text(
        509.0,
        240.0,
        anchor="nw",
        text="Password",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    window.entry_image_1 = entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(663.5, 286.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#fff", fg="#000716", font=("Poppins", -12))
    entry_1.place(x=524.0, y=266.0, width=279.0, height=43.0)

    window.button_image_1 = button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    window.button_image_1_2 = button_image_1_2 = PhotoImage(file=relative_to_assets("button_1_2.png"))


    def change_image():
        button_1.custom_value = not button_1.custom_value
        if button_1.custom_value:
            button_1.config(image=button_image_1)
        else:
            button_1.config(image=button_image_1_2)


    button_1 = Button(
        image=button_image_1_2,
        borderwidth=0,
        highlightthickness=0,
        command=change_image,
        relief="sunken",
    )
    button_1.custom_value = False
    button_1.place(x=509.0, y=321.5, width=25.0, height=25.0)

    canvas.create_text(
        545.0,
        325.0,
        anchor="nw",
        text="Remember Me",
        fill="#A5A5A5",
        font=("Poppins Medium", 12 * -1),
    )

    def login_user():
        # Check if user exists
        username_entry = entry_2
        password_entry = entry_1
        remember_me = button_1.custom_value
        try:
            user = get_user_from_username(username_entry.get())

            # If password entered is correct
            if check_password(password_entry.get(), user.password):
                print("Logged in!")
            else:
                print("Wrong password!")

            if remember_me:
                with open("data.json", "r") as f:
                    data = json.load(f)

                # Save data to data.json
                data["remember_me"] = remember_me
                data["user"] = {"username": user.username, "password": str(user.password)}

                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

            for widget in window.winfo_children():
                widget.destroy()

            load_home(window, user)
        except UserNotFound:
            print("User not found!")


    window.button_image_2 = button_image_2 = PhotoImage(file=relative_to_assets("login_button.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="sunken",
        command=login_user
    )
    button_2.place(x=554.0, y=387.5, width=220.0, height=45.5)

    canvas.create_text(
        528.0,
        452.0,
        anchor="nw",
        text="Don’t have an account yet?",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    def go_to_register():
        for widget in window.winfo_children():
            widget.destroy()
        load_register(window)

    window.register_text = register_text = PhotoImage(file=relative_to_assets("register_button_text.png"))
    button_3 = Button(
        image=register_text,
        borderwidth=0,
        highlightthickness=0,
        bg="#fff",
        relief="sunken",
        command=go_to_register,
    )
    button_3.place(x=739.0, y=452.0, width=71.0, height=22.0)

    window.entry_image_2 = entry_image_2 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(663.5, 186.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#fff", fg="#000716", highlightthickness=0, font=("Poppins", -12))
    entry_2.place(x=524.0, y=164.0, width=279.0, height=44.0)

    canvas.create_text(
        509.0,
        140.0,
        anchor="nw",
        text="Username",
        fill="#B6B6B6",
        font=("Poppins Medium", 15 * -1),
    )

    return (
        entry_2, # Username entry
        entry_1, # Password entry
        button_1, # Remember me toggle
        button_2, # Register button
        button_3 # Login text button
    )

def load_home(window, current_user):
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 558,
        width = 864,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    text_item = canvas.create_text(
        223.0,
        52.0,
        anchor="nw",
        text=f"Welcome, {current_user.username}",
        fill="#71008F",
        font=("Poppins Medium", 40 * -1)
    )

    text_len = len(current_user.username)
    if text_len > 10:
        font_size = int((15 / text_len) * 40)
        font_size = max(font_size, 25)  # set a minimum font size
        canvas.itemconfig(text_item, font=("Poppins Medium", font_size * -1))

    text_width = canvas.bbox(text_item)[2] - canvas.bbox(text_item)[0]
    x = (864 - text_width) / 2
    canvas.coords(text_item, x, 52.0)

    window.image_image_1 = image_image_1 = PhotoImage(
        file=relative_to_assets("subheader.png"))
    canvas.create_image(
        432.0,
        170.0,
        image=image_image_1
    )

    window.button_image_1 = button_image_1 = PhotoImage(
        file=relative_to_assets("server_link.png"))
    button_1 = canvas.create_image(
        432.0,
        170.0,
        image=button_image_1
    )
    canvas.tag_bind(button_1, "<Button-1>", lambda event: webbrowser.open_new_tab("https://discord.gg/JeegWD4VPc"))

    window.image_image_2 = PhotoImage(
        file=relative_to_assets("footer.png"))
    canvas.create_image(
        432.0,
        528.0,
        image=window.image_image_2
    )

    window.button_image_2 = button_image_2 = PhotoImage(
        file=relative_to_assets("github_link.png"))
    button_2 = canvas.create_image(
        432.0,
        528.0,
        image=button_image_2
    )
    canvas.tag_raise(button_2)
    canvas.tag_bind(button_2, "<Button-1>", lambda event: webbrowser.open_new_tab("https://github.com/CantCode023"))

    window.image_image_3 = image_image_3 = PhotoImage(
        file=relative_to_assets("topbar.png"))
    canvas.create_image(
        432.0,
        6.0,
        image=image_image_3
    )

    canvas.bindtags((canvas, window, "all"))