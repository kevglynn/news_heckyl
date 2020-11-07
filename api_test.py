import requests, json

payload = {
    'limit': 5,
    't': 'all'
}
headers = {
    'User-agent': 'Reddit bot 1.0'
}

#For the purposes of demonstration, I will use the /r/funny subreddit

endpoint = 'https://www.reddit.com/r/funny/top.json'
r = requests.get(endpoint, headers = headers, params = payload)
r = json.loads(r.content)

print(r)