import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q={}"

def find_rating(name):
    ratings = {}
    r = requests.get(URL.format(name))
    s = BeautifulSoup(r.text,"html.parser")
    n = s.find_all("div",class_="sDYTm")
    for i in n:
        d = i.text.split(".")
        ratings[d[1]] = d[0]
    return ratings


movie = "Avengers Infinity War"
rating = find_rating(movie)
print (rating)