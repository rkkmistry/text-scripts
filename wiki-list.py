from urllib2 import urlopen
from bs4 import BeautifulSoup as bs


url = "https://en.wikipedia.org/wiki/Category:Diageo_brands"
soup = bs(urlopen(url))
print soup.get_text()