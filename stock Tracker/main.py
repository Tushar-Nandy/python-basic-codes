import requests
from datetime import date,timedelta

STOCK_NAME = "AMGN"
COMPANY_NAME = "Tesla Inc"
TODAY = date.today()
Stock_today = TODAY - timedelta(days=1)
Stock_yesterday = TODAY - timedelta(days= 2)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':'demo'
}
news_param={
    'q':COMPANY_NAME,
    'from':(Stock_yesterday),
    'sortBy':'publishedAt',
    'apiKey':'demo'
}
r = requests.get(STOCK_ENDPOINT,params=stock_params).json()

try:
    data =r['Time Series (Daily)']
except KeyError:
    print('Daily Limit Exceeded')
    print(r)
#print(data[str(Stock_today)])
artcles=[]
def get_news():
    res = requests.get(NEWS_ENDPOINT,params=news_param).json()
    news = res['articles']
    print(type(news))
    for i in range(3):
       artcles.append(news[i])
    display_news()
def display_news():
    for j in range(len(artcles)):
        news_dict = artcles[j]
        print(f"Author: {news_dict['author']}\nTitle: {news_dict['title']}\nDescription: {news_dict['description']}\n\n")
#url ='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_close = float(data[str(Stock_today)]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_close = float(data[str(Stock_yesterday)]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_difference = abs(yesterday_close - before_yesterday_close)
print(price_difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = price_difference*100/yesterday_close
print(percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage >=5:
    get_news()

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



# NNNEDNMDKEMIDNED DDKEND122KM231   MKMKNKM1WKEMKE  #KKLPSDMD2K123X1A#:  KKPAJBCE2A160X1C21234#
#mek3m3 3krn3kr 3k4n34 2k3k4 3k4 k2 m3 2kn2k 4kn4 m4 123 1k24n 42kmkmk,9a2d75b7a5b2472a9ea5903dcc4f0a81 1133 21313131 311mk33r3 r3 rn3r 3 rr