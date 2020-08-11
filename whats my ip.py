import requests

URL = "http://httpbin.org/ip"

def whats_my_ip():
    response = requests.get(URL)
    ip = response.json()['origin']
    return ip.split(",")[0]
print(whats_my_ip())