"""scraping.py

Web Scraping - Using Beautiful Soup
===================================

Definitions:
------------
'web scraping': any automated collection of data from the web that is not
    a program interacting with an API (definition from Treehouse)


Beautiful Soup
--------------
### Installation ###
(venv) $ pip3 install beautifulsoup4


Sidenote from [Treehouse Video](https://teamtreehouse.com/library/beautiful-soup)
-------------------------------
Ken mentions (in the context of HTML content populated by JavaScript) that
"Beautiful Soup doesn't wait for JavaScript to run before it scrapes
a page."
This does not seem to be a true statement. Beautiful Soup could wait all 
day long: it's still only going to process whatever HTML was passed into
it. What determines the content of the HTML passed in is whatever we
got from the web, in the example below, by performing a GET request using
`requests`.
"""
import requests
from bs4 import BeautifulSoup


# Step 1: determine URL
url = 'https://treehouse-projects.github.io/horse-land/index.html'

# Step 2: make a GET request to the URL
response = requests.get(url)

# Step 3: assign the text content of the page to a variable
html = response.text

# Step 4: Make a BeatifulSoup object from the html
# (In this case we are using Python's builtin html parser)
soup = BeautifulSoup(html, 'html.parser')

# Examples of using the soup
## Full content
print( soup )  # the full content of the parsed HTML
print( soup.prettify() )  # nicely indented parsed HTML

## Basic extractions
print( soup.title )  # the HTML title element (including tags)
print( soup.div )  # the first div element in the page

## Collection extractions
divs = soup.find_all('div', {'class': 'featured'})
for div in divs:
    print(div)

## More advanced extractions
featured_h2 = soup.find('div', {'class': 'featured'}).h2
h2_text = featured_h2.get_text()  # this method strips tag data so it should be the last step in a scrape workflow
print( h2_text )

## find (and find_all) syntax:
### `find(name, attrs, recursive, string, **kwargs) -> <result> | None`
### `find_all(name, attrs, recursive, string, limit, **kwargs) -> [<result>]`
### - name : only consider tags that match the name
### - attrs : this is a way to search for css classes in pre 4.1.2 versions (use `class_` in newer versions)
### - recursive=True : boolean switch for whether find can look at descendants other than direct children
### - string : use to search for a string instead of a tag

### - class_ : a kwarg to search for CSS classes (new in 4.1.2). 

### - limit (find_all only): an int that determines the max number of hits that will be returned

### name, string, class_ all accept a string or regex or fn or True
print("class_ example")
print("--------------")
print("all references to the primary button class")
primary_btns = soup.find_all(class_="button--primary")
print(primary_btns)

