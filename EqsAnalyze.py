################################# Project

#### Imports
import json
import datetime
import time
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import scipy as sc
import numpy as np

#### Defines
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
days = 4 # Max Days
pages = 3 # Max Pages
delay = 300 # 5 Minutes

#### Fucntions

#### Main

### API
startDate = "2014-01-01"
endDate = "2014-02-01"

### Crawling
tables_wiki = pd.read_html("https://en.wikipedia.org/wiki/Lists_of_20th-century_earthquakes", match="Deaths")
#asession = AsyncHTMLSession()
#r = await asession.get('https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data?maxYear=2020&minYear=2000')
#tables_noaa = driver.get("https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/event-data?maxYear=2020&minYear=2000")
#bs = BeautifulSoup(tables_noaa.content, "html.parser")

df = pd.DataFrame()

#print(r)

for table in tables_wiki:
    df = pd.concat([df, table])

df = df[["Date", "Time", "Place", "Deaths", "Magnitude"]]
print(df.head(10))
#for t in bs.findAll("table"):
#    if "wikitable" in t['class']:
#        t.findAll(lambda tag: tag.name=='th')
#        t.findAll(lambda tag: tag.name=='td')

#df = pd.DataFrame({'genre_name' : genre_name, 'link_to_genre_page' : link_to_genre_page})
#print(df)

#names = []; years = []; genres = []; ratings = []
#next = "drama.html"
#for i in range(2):
#    bs = BeautifulSoup(open(next), "html.parser")
#    for t in bs.findAll("div", attrs={"class":"lister-item-content"}):
#        names.append(t.find("h3").find("a").text)
#        years.append(t.find("span", attrs={"class":"lister-item-year"}).text)
#        genres.append(t.find("span", attrs={"class":"genre"}).text)
#        ratings.append(t.find("strong").text)
#    # Find next
#    next = bs.find("a", attrs={"class":"lister-page-next"})['href']
#df = pd.DataFrame({"movie_name": names,
#                   "release_year": years,
#                   "genre_names": genres,
#                   "rating": ratings})
#print(df)
