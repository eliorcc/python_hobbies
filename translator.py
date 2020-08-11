import requests
from bs4 import BeautifulSoup

#english to any other language translator

l = "https://www.google.com/search?q={}"
q = "meaning of {} in {}"

def meaning(word,language):
    query = l.format(q.format(word,language))
    r = requests.get(query)
    s = BeautifulSoup(r.text,"html.parser")
    return s.find("div",class_= "AP7Wnd").text

word = meaning("hello","hebrew")
print(word)