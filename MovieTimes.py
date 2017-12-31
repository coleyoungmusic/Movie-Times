import requests
import pprint
from bs4 import BeautifulSoup

# Movie titles and times are subject to Cinemark Allen 16 and XD ONLY

url = "https://www.cinemark.com/north-texas/cinemark-allen-16-and-xd"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

headers = soup.select('h2')  # selects all movie titles

movieTitles = []  # list that will contain h2 elements

for x in headers:
    movieTitles.append(x.text)  # movieTitles now contains list of titles

for x in movieTitles:
    print(x + '\n')

titleChoice = int(input("Enter what movie you would like to see: ")) - 1


showtime_divs = [soup.find_all('div', {'class:', 'showtimeMovieBlock'})]  # individual movie info

for x in showtime_divs:
    movieTimes = [' '.join(x[titleChoice].text.split())]
    pprint.pprint(movieTimes)
