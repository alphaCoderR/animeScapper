import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.parse
pd.set_option('display.max_colwidth', 500)


def searchModule(animeName):
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
        print(index+1, name)


animeName = urllib.parse.quote(input("Enter the name of the anime : "))
searchModule(animeName)
# print(searchList)