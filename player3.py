"""
def api_slice(json2python):
    poke_pic= json2python[][]
    return poke_pic

api_slice("https://pokeapi.co/api/v2/pokemon/bulbasaur/") # this is a temporary link

"""

#!/usr/bin/python3

import json
import requests

MAJORTOM = "https://pokeapi.co/api/v2/pokemon/bulbasaur/"

def api_slice(a_url):

    response = requests.get(a_url).json()
    print(type(response))

api_slice(MAJORTOM) # this is a temporary link
