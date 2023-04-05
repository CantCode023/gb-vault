from __future__ import annotations
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\cantc\OneDrive\Desktop\Coding\Python\gb-vault\build\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("864x558")
window.configure(bg="#FFFFFF")


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
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(257.0, 279.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(509.0, 279.0, image=image_image_2)

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

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(663.5, 286.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#fff", fg="#000716", font=("Poppins", -12))
entry_1.place(x=524.0, y=266.0, width=279.0, height=43.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_1_2 = PhotoImage(file=relative_to_assets("button_1_2.png"))


def change_image():
    current_value = button_1.custom_value
    print(not current_value)
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


def register():
    username = entry_2.get()
    password = entry_1.get()
    remember = button_1.custom_value
    print(username, password, remember)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="sunken",
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

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="sunken",
)
button_3.place(x=739.0, y=452.0, width=44.0, height=22.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(663.5, 186.0, image=entry_image_2)
entry_2 = Entry(
    bd=0, bg="#fff", fg="#000716", highlightthickness=0, font=("Poppins", -12)
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
window.resizable(False, False)
window.mainloop()