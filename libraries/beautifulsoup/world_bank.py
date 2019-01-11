"""world_bank.py

An example of using scraping techniques for interacting with an API
"""
import csv

import requests
from bs4 import BeautifulSoup



BASE_URL = "http://api.worldbank.org/v2/countries/"
COUNTRY_CODE_FILENAME = 'country_iso_codes.csv'
VERBOSE = False


def get_country_codes(filename, verbose=VERBOSE):
    fh = open(filename, 'r')
        
    # csv.reader takes an iterable (and optionally a dialect or format 
    # specifications) and returns an iterable csv.reader object.
    # Each element in the iterable is a list representing a table row
    # (each element in the inner lists represents a table cell)
    country_codes = csv.reader(fh)  # A _csv.reader object 
    
    # Turn the csv.reader object into a simple list of strings
    country_codes = [x[0] for x in country_codes]

    if verbose:
        print(country_codes)
    
    return country_codes
    

def get_country_data(country_code, text=True, verbose=VERBOSE):
    url = BASE_URL + country_code

    response = requests.get(url)

    if not response.ok:
        print("Request Failed")
        print(f'{response.status_code}: {response.reason}')
        return

    if verbose:
        print("Received response from url:")
        print(response.url)
        print("---- Response Details ----")
        print(response.status_code, response.reason)
        print("Headers:")
        print("--------")
        for key, value in response.headers.items():
            print(f'{key}: {value}')

        if text:
            print("Body (Assuming Text-based):")
            print("---------------------------")
            print(response.text)
        else:
            print("Body (Treating as non=text:")
            print("---------------------------")
            print('first 500 bytes')
            print(response.content[:500])
        print("\n\n")

    return response.content


def parse_country_data(data, format='xml', verbose=VERBOSE):
    """For any parser other than Python's built-in HTML parser ('html.parser'),
    it needs to be obtained and installed.
    For example, for XML, use lxml:
    ```console
    (venv) $ pip3 install lxml
    ```
    """
    soup = BeautifulSoup(data, format)

    output = {}
    
    if soup.find('wb:error'):
        # something went wrong
        if verbose:
            print(soup)
        output['error'] = soup.find('wb:error').get_text()
    else:
        output['country name'] = soup.find('wb:name').get_text()
        output['region'] = soup.find('wb:region').get_text()
        output['income level'] = soup.find('wb:incomeLevel').get_text()
 
    if verbose:
        for key, value in output.items():
            print(f'{key}: {value}')

    return output


# ---------------------------

if __name__ == "__main__":

    country_codes = get_country_codes(COUNTRY_CODE_FILENAME)
    
    bad_codes = {}
    for code in country_codes:
        # Note, this is ridiculously slow because we are iterating through
        # a list and then making a synchronous call out to the Internet.
        # In production we'd want to grab all the data asynchronously
        data = get_country_data(code)

        parsed = parse_country_data(data)

        if 'error' in parsed.keys():
            bad_codes[code] = parsed['error']
        else:
            for key, value in parsed.items():
                print(f'{key}: {value}')

    if bad_codes:
        print("\n\n!!Errors were found during processing!!")
        print(f"No data was available for the following country codes:")
        if VERBOSE:
            for key, value in bad_codes.items():
                print(key + ":")
                print("----")
                print(value)
        else:
            print( ", ".join(bad_codes) )
    
