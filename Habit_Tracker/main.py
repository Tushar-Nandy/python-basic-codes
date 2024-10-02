import requests
import datetime

today = datetime.date.today()
list_da = str(today).split('-')
today_param =f"{list_da[0]}{list_da[1]}{list_da[2]}"

#print(today_param)
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'kidscorpy'
TOKEN = 'hhkk123qqaasw123'
GRAPH_ID = "graph1"
#token is self generated of size 8,128 words
user_params={
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

#for account creation
# response=requests.post(pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    'id':GRAPH_ID,
    'name':'Code Tracker',
    'unit': 'Hrs',
    'type':'float',
    'color':'ajisai' #purple
}
#used to hide the apikey while searching or using any request
header={
    'X-USER-TOKEN':TOKEN
}
#created a new graph
# response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)
hrs_coded = input("Enter the number of hours you coded today: ")
graph_maker_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data ={
    "date": today_param,
    "quantity": hrs_coded,
}

response=requests.post(url=graph_maker_endpoint,json=pixel_data,headers=header)
print(response.text)



# https://pixe.la/v1/users/kidscorpy/graphs/graph1.html