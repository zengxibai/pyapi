#!/usr/bin/python3

import json

def extract(a_list):
    for person in a_list:
        res = [ sub['name'] for sub in person["friends"]] 
        print(f"""
        name: {person["name"]}
        email: {person["email"]}
        phone: {person["phone"]}
        address: {person["address"]}
        friends: {str(res)}
        """)

def main():
    with open("challenge.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)
    extract(datadecoded)

main()
