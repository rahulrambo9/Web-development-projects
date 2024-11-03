from bs4 import BeautifulSoup 

# beautiful soup is python library that use to extraxt data from html and xml files

with open("D:/Web-development-projects/Web_scraping/bs4-start/website.html") as file:
    soup = BeautifulSoup(file, 'html.parser')

print(soup.title)
print(soup.title.string)

all_a_tag = soup.find_all(name="a")
for tag in all_a_tag:
    #print(tag.getText())
    print(tag.get("href"))

#print(all_a_tag)

