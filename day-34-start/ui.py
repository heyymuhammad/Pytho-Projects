from tkinter import *
from quiz_brain import quiz_brain
import time

THEME_COLOR ="#375362"

class QuizInterface:

    def __init__(self, quiz_brain: quiz_brain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.configure(background=THEME_COLOR,pady=20, padx=20)

        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, fg="white", font=("Arial", 20))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(158, 125, text="Question Text", fill=THEME_COLOR, font=("Arial", 15, "italic"), width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="./day-34-start/images/true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, border=0, command=self.true_pressed)
        self.true.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./day-34-start/images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, border=0, command=self.false_pressed)
        self.false.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()
    
    # def celebrate(self):
    #     self.one_img = PhotoImage(file="./day-34-start/images/+1.png")
    #     self.plus_one = Canvas(height=200, width=200)
    #     self.plus_one.create_image(100,100,image=self.one_img)
    #     self.plus_one.grid(row=1, column=0, columnspan=2)


    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the Quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def trigger_button(self, answer):
        if self.quiz.check_answer(user_answer=answer):
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)

    def true_pressed(self):
        self.trigger_button("True")

    def false_pressed(self):
        self.trigger_button("False")
        

