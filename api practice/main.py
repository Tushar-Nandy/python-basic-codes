import requests
from datetime import datetime

MY_LAT = 19.075983 # Your latitude
MY_LONG = 72.877655 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
time_hrs = int(time_now.split(" ")[1].split(':')[0])
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if (iss_latitude <= MY_LAT +5 and iss_latitude >= MY_LAT - 5) and (iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG -5) and time_hrs>sunset:
    print("Look Up")
else:
    print("hmmm")
print(iss_latitude,iss_longitude)