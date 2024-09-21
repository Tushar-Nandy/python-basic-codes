from tkinter import *
from pandas import *
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
try:
    data=read_csv('./FlashCard/data/words_to_learn.csv')
except FileNotFoundError:
    data=read_csv('./FlashCard/data/french_words.csv')  
    to_learn= data.to_dict(orient="records")
else:  
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=rd.choice(to_learn)
    canvas.itemconfig(card_title,text='French',fill='black')
    canvas.itemconfig(card_word,text=current_card["French"],fill='black')
    canvas.itemconfig(card_bg,image=flash_front)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white')
    canvas.itemconfig(card_word,text=current_card['English'],fill='white')
    canvas.itemconfig(card_bg,image=flash_back)

def is_known():
    to_learn.remove(current_card)
    data=DataFrame(to_learn)
    data.to_csv("./FlashCard/data/words_to_learn.csv",index=False) # path is incorrect as VS code is taking the root file as Udemy and not FlashCard :(
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

flash_front = PhotoImage(file='./FlashCard/images/card_front.png')
flash_back = PhotoImage(file='./FlashCard/images/card_back.png')
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_bg=canvas.create_image(400,263,image=flash_front)
card_title=canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file='./FlashCard/images/wrong.png')
unknown_button = Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file='./FlashCard/images/right.png')
know_button =Button(image=check_image,highlightthickness=0, command=is_known)
know_button.grid(row=1,column=1)

next_card()

window.mainloop()