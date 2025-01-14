from bs4 import BeautifulSoup
import requests

myurl = requests.get("https://www.gamesradar.com/best-anime/")
mycontent = myurl.text
mysoup = BeautifulSoup(mycontent, 'html.parser')

mylist = mysoup.find_all('h2', class_='list-item__title')
for i in mylist:
    print(i.text)



# for i in mysoup.find_all('h3'):
#     print(i.text)

# for i in mysoup.find_all('p'):
#     print(i.text)

# for i in mysoup.find_all('a'):