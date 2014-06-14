#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI
# All your changes should be in the 'extract_carrier' function
# Also note that the html file is a stripped down version of what is actually on the website.

# Your task in this exercise is to get list of all airlines. 
# Exclude all of the combination values, 
# like "All U.S. Carriers" from the data that you return.
# You should return a list of codes for the carriers.

from bs4 import BeautifulSoup
html_page = "C:/Benben/UD032 mongoDB/Lesson_2Problem_Set/01-Carrier_List/options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        cl = soup.find(id='CarrierList')
        for tag in cl:
            if tag.name == 'option':
                data.append(tag['value'])
    del data[0:3]
    return data


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

test()