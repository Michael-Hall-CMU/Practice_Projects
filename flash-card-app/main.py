from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_STYLE = "Ariel"
FRONT_TEXT_COLOR = "black"
BACK_TEXT_COLOR = "white"
FRONT_TITLE = "French"
BACK_TITLE = "English"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=FRONT_TITLE, fill=FRONT_TEXT_COLOR)
    canvas.itemconfig(card_word, text=current_card[FRONT_TITLE], fill=FRONT_TEXT_COLOR)
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text=BACK_TITLE, fill=BACK_TEXT_COLOR)
    canvas.itemconfig(card_word, text=current_card[BACK_TITLE], fill=BACK_TEXT_COLOR)
    canvas.itemconfig(card_image, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_STYLE, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_STYLE, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()