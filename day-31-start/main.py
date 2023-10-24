from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------------------ FILE HANDLING ------------------
try: 
    data_file = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
    to_learn  = original_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")
# ------------------ Functionality ------------------
    
def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(title, text="French", fill= "black")
    card.itemconfig(word, text=current_card["French"], fill= "black")
    card.itemconfig(card_image, image= card_front)
    flip_timer = window.after(3000, flip_card)
    

def flip_card():
    card.itemconfig(title, text="English", fill= "white")
    card.itemconfig(word, text=current_card["English"], fill= "white")
    card.itemconfig(card_image, image= card_back)
        
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  

    change_word()


# ------------------ GUI ------------------

window = Tk()
window.title("Flashy")
window.config(background= BACKGROUND_COLOR, padx=50, pady=50)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

card = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=card_front)

title = card.create_text(400,180,font=("Ariel", 40, "italic"), text="Title")
word = card.create_text(400,300,font=("Ariel", 60, "bold"), text="word")

card.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, flip_card)
change_word()

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, border=0, command=is_known)
tick_button.grid(row=1, column=1)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, border=0, command=change_word)
cross_button.grid(row=1, column=0)


window.mainloop()

