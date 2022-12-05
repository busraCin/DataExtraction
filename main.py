import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

rating_filter = float(input("Set the Lowest Rating:" ))

titles = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class","ratingColumn imdbRating"})

for title,rating in zip(titles,ratings):

    title=title.text
    title=title.strip()
    title=title.replace("\n"," ")

    rating=rating.text
    rating=rating.strip()
    rating=rating.replace("\n"," ")

    if(float(rating) > rating_filter):
        print("Movie: {} movie IMDB : {}".format(title,rating))







