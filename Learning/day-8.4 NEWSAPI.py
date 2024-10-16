# program to fetcth news from API 
import requests
import json

query = input('What Type of news you wanna Know, mention some keywords: ')
url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey=438eca06792e4d00bcc1e0bbb041ec87"
r = requests.get(url)
news = json.loads(r.text)
articles = news['articles']
for article in articles:
    print(article['title'])
    print(article['description'])
    print("------------------------------")
