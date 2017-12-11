import requests
from bs4 import BeautifulSoup

# Movie titles and times are subject to Cinemark Allen 16 and XD ONLY

url = "https://www.cinemark.com/north-texas/cinemark-allen-16-and-xd"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

movie_title = soup.find_all("h2")

titles = [movie.text for movie in movie_title]

print(titles)

digitalCinema = soup.find_all("div", {"class": "showtimeMovieBlock"})

movieTime = [time.text.strip() for time in digitalCinema]
movieTimes = ''.join(movieTime)

print(movieTimes, sep=" ", end="", flush=True)
