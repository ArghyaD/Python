from selenium import webdriver
from bs4 import BeautifulSoup
import urllib

name = []
img = []
profession = []
best_work = []


def extractData():
    url = r"http://m.imdb.com/feature/bornondate"
    driver = webdriver.Chrome(r"C:\Python27\Tools\chromedriver.exe")
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html5lib")
    for tag in soup.find_all("div", class_="label", limit=10):
        name.append(tag.span.text)
        temp = str(tag.div.text)
        lst = temp.split(",", 2)
        profession.append(lst[0])
        best_work.append(lst[1])
        img.append(tag.previous.get('src'))
    i = 0
    while i < 10:
        urllib.urlretrieve(img[i], name[i] + ".jpg")
        i += 1
    driver.close()