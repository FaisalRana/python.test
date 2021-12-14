import random 
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    innerMovieTags = soup.select('td.titleColumn a' )
    innerMovieTag0 = innerMovieTags[0]
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    movietag0 = movietags[0]
    movieInfo = movietag0.text.split()
    def get_year(movie_tag):
      moviesplit = movie_tag.text.split()
      year = moviesplit[-1]
      return year

    year = movieInfo[len(movieInfo)-1]
    title = movieInfo[1] + " " +  movieInfo[2] + " " + movieInfo[3]

    # print(innerMovieTags[0])
    # print(movietag0)

    def get_title(inner_movie_tag):
      actors = inner_movie_tag['title']
      title = inner_movie_tag.text
      return title

    years = [get_year(tag) for tag in movietags]
    movieTitles = [tag['title'] for tag in innerMovieTags]
    movieActors = [tag.text for tag in innerMovieTags]
    ratings = [float(tag['data-value']) for tag in rating_tags]

    n_movies = len(movieTitles)

    while(True):
      index = random.randrange(0, n_movies)

      print(f'{titles[index]} {years[index], rating')
    print(n_movies)
    # print(movieTitles)


    actors = innerMovieTag0['title']
    title = innerMovieTag0.text
    link = innerMovieTag0['href']

    # print(actors)
    # print(title)
    # print(link)
    # print(innerMovieTag0)


if __name__ == '__main__':
  main() 