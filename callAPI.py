import requests

def call(url, methods):
    response = requests.request(methods, url)
    return response