#!/usr/bin/env python3

import xml.etree.cElementTree as ET
import requests

def get_url(url, filename):
    """Dl the xml file from yr.no"""
    print("Downloading xml with requests")
    r = requests.get(url)
    with open(filename, "wb") as code:
        code.write(r.content)

def xml_parse(filename):
    """Parse the downloaded xml"""
    root = ET.parse(filename).getroot()
    print(root.tag)
    for foo in root.findall('location'):
        country = foo.find('country').text
        name = foo.find('name').text
        print('Country: ', country)
        print('City: ', name)
    for qwe in root.findall('forecast/tabular/time'):
        attributes = qwe.attrib
        asd = attributes.get('from')
        print(asd)

def main(url, filename):
    # get_url(url, filename)
    xml_parse(filename)

FILENAME = "yr.xml"
URL = "Input url to yr.no forecast xml:\n"

main(URL, FILENAME)
