import smtplib
import datetime as dt
import random as rd
days = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
with open('./Mail/quotes.txt') as file:
    qoutes=file.readlines()

MY_EMAIL = "email@gmail.com"
#password ='Abcdefgh1234'
APP_PASSWORD ="emial"

now = dt.datetime.now()
week_day = now.weekday()
print(week_day)

try:
    if week_day ==2:
        #for gmail.com
        #for different mail serever the SMTP(part), part will be different
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #to make the connection secure
            connection.login(user=MY_EMAIL,password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs="scorpking0910@gmail.com",
                                msg=f"Subject:Motivational {days[week_day]}\n\n{rd.choice(qoutes)}")
except:
    print(f"There was a problem")

else:
    print("Email sent successfully")
