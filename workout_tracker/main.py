import requests
from Impkey import API_KEY, APP_ID
import datetime
API_ENDPOINT ="https://trackapi.nutritionix.com/v2/natural/exercise"

Sheety_endpoint ='https://api.sheety.co/26c0b5c6e5dd3772c4ea889dc054e19c/myWorkouts/workouts'

query = input("What exercise did you do? ")

header={
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key':API_KEY
}
mssg={
    'query':query
}

resp = requests.post(url=API_ENDPOINT,json=mssg,headers=header)

data = resp.json()
print(data)
data = data['exercises'][0]
workout = data['user_input']
duration = data['duration_min']
calorie = data['nf_calories']
print(workout,duration,calorie)
body = {
    'workout': {
        "Date": str(datetime.date.today()),
        "Time":str(datetime.datetime.now()),
        "Exercise": workout,
        "Duration": duration,
        "Calories":calorie
    }
  }
head = {
    "Authorization": "Bearer 1234456ksjdnd123"

}
res=requests.post(url=Sheety_endpoint,json=body,headers=head)
print(res.text)