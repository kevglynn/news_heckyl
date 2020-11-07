import requests, json

payload = {
    'limit': 1,
    't': 'all'
}
headers = {
    'Authorization': 'e5ac96cd-6010-4201-8cb0-661443072caa'
}

#For the purposes of demonstration, I will use the /r/funny subreddit

# endpoint = 'https://www.reddit.com/r/funny/top.json'

endpoint = "https://di.apidata.world/news/api/newsfeed/GetUniqueNews?entityTypeIds=1&languages=en&categoryIds=47&countryIds=1&lastNewsUpdateTime=1596546000000"

r = requests.get(endpoint, headers = headers, params = payload)
r = json.loads(r.content)

print(r)