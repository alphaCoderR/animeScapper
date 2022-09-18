import requests
import re
from bs4 import BeautifulSoup as bs
import urllib.parse
from animate import (search_loader, loader)


def searchModule(animeName):
    search_loader.start()
    global searchList
    searchList = []
    page = requests.get("https://kayoanime.com/?s="+animeName)
    soup = bs(page.content, 'html.parser')
    for index, link in enumerate(soup.find_all("h2", class_=re.compile("post-title"))):
        option = {}
        # Accessing the inner child element of the link option
        # link_tag=link.contents[0]
        # Accessing the title of the element
        name = link.contents[0].contents[0]
        # Accessing the link from the element
        link = link.contents[0].get('href')
        option = dict({"Name": name, "Link": link})
        searchList.append(option)
        if index == 0:
            search_loader.stop()
        print(index+1, name)


def pageModule(choice):
    page = requests.get(searchList[choice-1]["Link"])
    searchList.clear()
    soup = bs(page.content, "html.parser")
    fetchedLinks = soup.find_all(class_="shortc-button")
    for i in fetchedLinks:
        name = i.contents[0]
        link = i.get("href")
        option = dict({"Name": name, "Link": link})
        searchList.append(option)
    print(searchList)


animeName = urllib.parse.quote(input("Enter the name of the anime : "))
searchModule(animeName)
choice = int(input("Enter your choice : "))
pageModule(choice)
# print(page)
# print(searchList[0]["Link"])
