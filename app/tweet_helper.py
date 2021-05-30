import requests
import json

def fetch_tweets(query):

    url = "https://api.twitter.com/2/tweets/search/recent?query="+query
    payload={}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.api+json',
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAHUUPwEAAAAARIqNH29iO83XUzJMHzatrI9lANU%3DWk6P77bmu7KeK0f5RjggIxCUCDUuZ0SAHffOArKM33Bm6csD47',
    'Cookie': 'guest_id=v1%3A162115147288690413; personalization_id="v1_ynqd9laCyq4BNFwdbUFBmQ=="'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.json()
