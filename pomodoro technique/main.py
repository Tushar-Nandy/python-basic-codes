import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text='Timer')
    check_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%2 !=0:
        count_down(work_sec)
        timer_label.config(text="Timer",fg=GREEN)
        
        
    elif reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK",fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}" # to display seconds in 00 format

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down,count - 1) # takes time in millisec, function to call, arguments within the called function
    else:
        mark=''
        start_timer()
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady=50, bg=YELLOW)


tomato_img=tk.PhotoImage(file="./tomato.png")
#for some reason, the image won't open when inside the folder and thus has to keep it outside

canvas = tk.Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0)

canvas.create_image(103,112, image=tomato_img)
timer_text= canvas.create_text(103,130,text="00:00", fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)



start_button =tk.Button(text='Start',highlightthickness=0, command=start_timer)
reset_button = tk.Button(text='Restart', highlightthickness=0, command= reset_timer)
check_label = tk.Label(text='', fg= GREEN, bg=YELLOW, font=(FONT_NAME,15,'bold'))
timer_label = tk.Label(text='Timer', fg= GREEN, bg=YELLOW, font=(FONT_NAME,45,'bold'))

timer_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column= 2)
check_label.grid(row=3, column=1)


window.mainloop()