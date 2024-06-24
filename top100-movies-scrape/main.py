from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_titles = [movie.getText() for movie in reversed(all_movies)]

with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
     file.write(f"{movie}\n")
