from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
hc_site = response.text

soup = BeautifulSoup(hc_site, 'html.parser')
#print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_link.append(link)

article_upvote = [score.getText() for score in soup.find_all(name="span", class_="score")]


print(article_text)
print(article_link)
print(article_upvote)