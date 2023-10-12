import requests

api_url = "https://zenquotes.io/api/quotes"
res = requests.get(url=api_url)
data = res.json()
print(data [0]['q'])

