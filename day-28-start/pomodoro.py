from tkinter import *
import math

# CONSTANTS 
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# FUNCTIONALITY

def reset():
    timer_text = canvas.create_text(text="00:00")
    heading.config(text="Timer")

def start():
    

# UI SETUP

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

heading = Label(text="Timer", font=(FONT_NAME, 35) , bg=YELLOW)
heading.grid(row=0, column=1)

start = Button(text="Start", border=1)
start.grid(row=2, column=0)

reset = Button(text="Reset", border=1)
reset.grid(row=2, column=2)

window.mainloop()