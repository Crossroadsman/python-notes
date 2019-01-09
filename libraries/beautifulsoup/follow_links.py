"""follow_links.py

This program will visit a specified URL. It will then crawl all internal links
and print to the console internal and external links.
"""
import re

import requests
from bs4 import BeautifulSoup


# Constants
# =========
BASE_URL = 'https://treehouse-projects.github.io/horse-land/'

"""This program assumes (using the Treehouse video's assumptions) that
internal links are those that end in ".html" and external links do not.
"""
INTERNAL_LINK_PATTERN = r'\.html$'
"""pattern explanation:
   (?<! ... ) : negative lookback: looking back from this point in the string
                there is no instance of the specified group pattern
   \.html     : the pattern in the group: ".html"
   $          : position the negative lookback at the end of the string (i.e.,
                the grouped sequence does not appear at the end of the pattern).
                This means that "www.html.com/external" will still match

Note that this match is zero-length. This is adequate for the purposes of
using as an input to BeautifulSoup.find_all() where it is solely being used as 
boolean (does this pattern exist or not). If we actually wanted to extract and 
use the matching text we could precede the above pattern with `.*` (any 
character, zero or more times). The full pattern would thus become:
`.*(?<!\.html)$`
"""
EXTERNAL_LINK_PATTERN = r'(?<!\.html)$'


# Link-scraping functions
# =======================
def get_links(path, pattern, base_url=BASE_URL):
    """Returns a list of BeautifulSoup objects representing all the links
    on the specified page conforming to the specified regex pattern.
    """
    full_url = f'{base_url}{path}'
    resp = requests.get(full_url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    pattern = pattern
    regex = re.compile(pattern)
    return soup.find_all('a', href=regex)


def get_internal_links(path, base_url=BASE_URL):
    """Returns a list of BeautifulSoup objects representing all the internal
    links on the specified page.
    """
    return get_links(path, INTERNAL_LINK_PATTERN, base_url)


def get_external_links(path, base_url=BASE_URL):
    """Returns a list of BeautifulSoup objects representing all the external
    links on the specified page.
    """
    return get_links(path, EXTERNAL_LINK_PATTERN, base_url)
    

# Display functions
# =================
def print_url(url):
    print(url)
    print("=" * len(url))

def print_external_links(url):
    external_links = get_external_links(url)
    if len(external_links) > 0:
        print("External links:")
        print("---------------")
        for link in external_links:
            url = link.attrs['href']
            print(url)

def print_everything(url):
    print_url(url)
    print_external_links(url)


# Crawl functions
# ===============
def crawl_internal_links(start_url, fn):
    """Starts at a given URL. Gets all the internal links on that page as list, 
    calls fn on the page,
    works through the list, recursively visiting each listed page, adding any 
    found links to the list and calling fn on each page.
    """
    visited_links = []
    print("starting at:")
    print(start_url)
    links = get_internal_links(start_url)
    print("visiting links:")
    while len(links) > 0:
        link = links.pop(0)
        url = link.attrs['href']
        if url in visited_links:
            continue
        visited_links.append(url)
        fn(url)
        links.extend( get_internal_links(link) )


# -----------------------------------------

if __name__ == "__main__":

    crawl_internal_links("index.html", print_everything)
