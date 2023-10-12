import requests


def quote_category(category):
    api_url = "https://zenquotes.io/api/quotes&category{}".format(category)
    res = requests.get(url=api_url)
    data = res.json()
    status = res.status_code
    match status:
        case 200:
            quotes = data [0]['q']
        case 400:
            quotes = data['error']['message']
        case _:
            quotes = "its Unecpected Error,Sorry fior Inconvenice"
    return quotes

quotes = quote_category(category='inspire')

print(quotes)