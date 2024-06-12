import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ['STOCK_API']
TWILIO_PHONE_NUM = os.environ['TWILIO_PHONE_NUM']
MY_PHONE_NUM = os.environ['MY_PHONE_NUM']
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, stock_params)
stock_response.raise_for_status()
daily_stock_data = stock_response.json()['Time Series (Daily)']

stock_closing_prices = [float(stock_data['4. close']) for (day, stock_data) in daily_stock_data.items()]
closing_price_diff = stock_closing_prices[0] - stock_closing_prices[1]
percent_diff = round(abs(closing_price_diff / stock_closing_prices[1]) * 100, 2)

if percent_diff >= 4:
    if closing_price_diff > 0:
        stock_diff = f"🔺{percent_diff}%"
    else:
        stock_diff = f"🔻{percent_diff}%"

    news_params = {
        "q": "tesla",
        "apiKey": os.environ['NEWS_API']
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_response.raise_for_status()

    three_articles = news_response.json()['articles'][:3]

    formatted_articles = [(f"{STOCK_NAME}: {stock_diff} \nHeadline: {article['title']}. "
                           f"\nBrief: {article['description']}") for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages \
            .create(
                body=article,
                from_=TWILIO_PHONE_NUM,
                to=MY_PHONE_NUM
            )
        print("Successfully sent message")

# The formatted SMS message looks like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
