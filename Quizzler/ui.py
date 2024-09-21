from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")
class QuizInterface:

    def __init__(self,quiz_brain : QuizBrain) -> None:
        self.quiz = quiz_brain
        self.ans = False
        self.score=0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        check = PhotoImage(file='./Quizzler/images/true.png')
        cross = PhotoImage(file='./Quizzler/images/false.png')

        self.score_label = Label(text=f'Score: 0',fg="white",background=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(bg='white',height=250,width=300)
        self.question_text = self.canvas.create_text(150,125,text="Hello",fill=THEME_COLOR,font=FONT,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_button = Button(image=check,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.correct)
        self.false_button = Button(image=cross,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.wrong)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=next_question)

    def correct(self):
        self.ans = "True"
        self.get_correct_ans()

    def wrong(self):
        self.ans ="False"
        self.get_correct_ans()

    def get_correct_ans(self):
        print(self.quiz.check_answer(self.ans))
        if self.quiz.check_answer(self.ans):
            self.score +=1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        if self.quiz.still_has_questions():
            self.window.after(1000,self.get_next_question)
            
        else:
            self.window.after(1000,self.disable_button)
            
        self.score_label.config(text=f"Score: {self.score}")
    def disable_button(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text,text=f'Game Over\nFinal Score: {self.score}')
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')