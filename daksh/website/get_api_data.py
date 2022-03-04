import requests

def get_data():
    url = 'http://127.0.0.1:8000/website/api/v1/'
    req = requests.get(url)
    return req.json()