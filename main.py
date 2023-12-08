import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Harry_Potter"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

article = soup.find("div", {"id": "mw-content-text"})

myParagraphs = article.find_all("p")[1:4]

print("Something about Harry Potter: \n")
for p in myParagraphs:
  print(p.text)
  print()
print("For more information, visit: https://en.wikipedia.org/wiki/Harry_Potter")