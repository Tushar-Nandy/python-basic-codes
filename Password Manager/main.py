from tkinter import *
from tkinter import messagebox
import random as rd
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if len(password.get())!=0:
        password.delete(0,END)
    password_list=[]
    character=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_characters = ['!','#','$','%','_','&','(',')','{','}','*','-','+','/','@','^']
    number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    req=[]
    for i in range(12):
        if i<=2:
            req.append(rd.choice(special_characters))
        elif i<=6:
            req.append(rd.choice(number))
        else:
            req.append(rd.choice(character))
    while len(req)!=0:
        a = rd.choice(req)
        password_list.append(a)
        req.remove(a)
    actual_password="".join(password_list)
    password.insert(0,actual_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_in.get()
    username = email_in.get()
    pass_word = password.get()
    if len(username) ==0 or len(pass_word)==0 or len(website)==0:
        messagebox.showinfo(title='OOps',message='Make sure no fields are left empty')
    else:
        is_ok=messagebox.askokcancel(title=website, message =f'These are the details entered:\nEmail: {username}\nPassword: {pass_word}\nis it OK?')
        if is_ok:
            with open('./password_manager.txt',mode='+a') as file:
                file.write(f"{website} | {username} | {pass_word}\n")
            web_in.delete(0,END)
            password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

logo_image =PhotoImage(file='logo.png')
canvas = Canvas(width=200, height= 200)
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

web_label = Label(text='Website: ')
web_in = Entry(width=50)
email_label = Label(text='Email / Username: ')
email_in = Entry(width=50)
password_label = Label(text="Password: ")
password = Entry(width=32)
generate_button = Button(text="Generate Password",command=generate_password)
add_password= Button(text="Add",width=36,command= save_password)

web_in.grid(row=1,column=1,columnspan=2)

web_label.grid(row=1,column=0)
email_in.grid(row=2,column=1,columnspan=2)
email_in.insert(0,"tusharnandy0910@gmail.com")
email_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
password.grid(row=3,column=1)
generate_button.grid(row=3,column=2)
add_password.grid(row=4,column=1,columnspan=2)
window.mainloop()