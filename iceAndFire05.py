#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def get_house(house_url):
    ## Send HTTPS GET to the API of ICE and Fire house resource
    gotresp = requests.get(house_url)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    #pprint.pprint(got_dj)
    print(f"House: {got_dj['name']}")


def get_book(book_url):
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(book_url)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    #pprint.pprint(got_dj)
    print(f"Book: {got_dj['name']}")

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #pprint.pprint(got_dj)

        ## get house url
        got_house_url = got_dj["allegiances"]
        #print(got_house_url)

        get_house(got_house_url[0])

        ## get book url
        got_books_urls = got_dj["books"]
        for book_url in got_books_urls:
            get_book(book_url)

if __name__ == "__main__":
        main()

