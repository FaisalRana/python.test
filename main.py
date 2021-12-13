import random 
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

if __name__ == '__main__':
  main()