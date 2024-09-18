import datetime as dt
import random as rd
import smtplib

lin1 = './Mail/t1.txt'
lin2 = './Mail/t2.txt'
lin3 = './Mail/t3.txt'
now = dt.datetime.now()
print(now)
day = now.day
month = now.month
messages =[lin1,lin2,lin3]
MY_EMAIL="email_of_sender"
APP_PASSWORD ='app_password'
mom={
    'day' : 1,
    'month': 9,
    'year': 1998,
    'email':'email'
}

dad={
    'day' : 18,
    'month': 9,
    'year': 1990,
    'email':'email'
}

parents =[mom,dad]
try:
    for name in parents:
        if name['day'] == day and name['month']==month:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                with open(rd.choice(messages)) as file:
                    mssg = file.readlines()
                    
                letter = "".join(mssg)
                print(letter)
                connection.starttls()
                connection.login(user=MY_EMAIL,password=APP_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, 
                                    to_addrs=name['email'],
                                    msg=f"Subject:Happy Birthday\n\n{letter}")
except:
     print("There was an error")
else:
     print("Message Send Successfully")