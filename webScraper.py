# @author: Finnian Allen

import bs4 as bs
import urllib.request

# our url to scrape from
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

# creates the object "soup" which stores the source and lxml
soup = bs.BeautifulSoup(source, 'lxml')

# gets the title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

# print(soup.get_text())
