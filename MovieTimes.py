import requests
from bs4 import BeautifulSoup
import pprint
# Movie titles and times are subject to Cinemark Allen 16 and XD ONLY

url = "https://www.cinemark.com/north-texas/cinemark-allen-16-and-xd"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

headers = soup.select('h2') # selects all movie titles

movieTitles = [] # list that will contain h2 elements

for x in headers:
    movieTitles.append(x.text) # movieTitles now contains list of titles

for x in movieTitles:
    print(x)

#titleChoice = list(input("Enter what movie you would like to see: ").split())

showtime_divs = soup.find_all("div", {"class": "col-xs-12 col-sm-10"})
for x in showtime_divs:
    movieTimes = []
    movieTimes.append(x)
    movieTimes2 = ''.join(x.text).split()
    movietimes3 = [' '.join(movieTimes2)]
    pprint.pprint(movietimes3)
