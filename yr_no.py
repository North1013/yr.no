#!/usr/bin/env python3

import requests
import xml.etree.cElementTree as ET

def get_url(url, filename):
    """Dl the xml file from yr.no"""
    print("Downloading xml with requests")
    r = requests.get(url)
    with open(filename, "wb") as code:
        code.write(r.content)

def xml_parse(filename):
    """Parse the downloaded xml"""
    e = ET.parse(filename).getroot()
    for atype in e.findall('location'):
        print(atype.get('name'))


def main(url, filename):
    get_url(url, filename)
    xml_parse(filename)

FILENAME = "yr.xml"
URL = input("Input url to your yr.no location")

main(URL, FILENAME)
