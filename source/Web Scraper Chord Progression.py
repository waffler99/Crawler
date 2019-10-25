

#Libraries




from selenium import *
#from beautifulsoup4 import *
import pandas as pd
from scrapy import *
#from urllib import urlopen





#Song and artist data functions
#
#
#
#
#
#
#
#
#
# May need to reorganize the data structure to be ordered. Depends on how I call it later?
#
#
#
#Check robots.txt
#Import Scrapy and actually do some scraping
#
#


l1 = list()
l2 = list()
def song_title():
    l1 = 0
    fh = open("Billboard_100.html")
    #words = dict()
    for item in fh:
        item = item.rstrip()
        item = item.strip("song text")
        if not item.startswith("""<span class="chart-element__information__song text"""): continue
        item = item[77:200]
        item = item[:-7]
        l2.append(item)
def song_artist():
    fh = open("Billboard_100.html")
    artists = {}
    for item in fh:
        item = item.rstrip()
        item = item.strip("song text")
        if not item.startswith("""<span class="chart-element__information__artist text--truncate color--secondary">"""): continue
        item = item[81:300]
        item = item[:-7]
        l1.append(item)
def song_result():
    song_artist()
    song_title()
    mapped = zip(l1,l2,)
    main_function_result = set(mapped)
    print(main_function_result)


song_result()




#Chord Data Functions


def chord_lookup():
    for item in song_result():
        pass
        #pull data from song_result
        #check for result on chordify
        #do first link that is result
        #combine song_result and chord_lookup


#<span class="label-Gs_maj"></span>



#Spiders

def spider_1():
    pass












"""

Find the URL that you want to scrape

Flow:


#FIRST INPUT DATA FOR TOP 100 SONGS
Inspecting the Page
Find the data you want to extract
Write the code
Run the code and extract the data
Store the data in the required format

#THEN INPUT CHORD PROGRESSION DATA







To Do:
Find Websites
---For names: https://www.billboard.com/charts/hot-100
---For readable chord progressions:

Find out how to manipulate html/css data.

Make sure that scraping that website is legal. (check url/robots.txt)

Required libraries
Selenium:  Selenium is a web testing library. It is used to automate browser activities.
BeautifulSoup: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
Pandas: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format.





"""
