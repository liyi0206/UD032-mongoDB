#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "C:/Benben/UD032 mongoDB/Lesson_2Problem_Set/02-Airport_List/options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        al = soup.find(id='AirportList')
        for tag in al:
            if tag.name == 'option':
                data.append(tag['value'])
    del data[0:2]
    del data[13:14]
    return data


def test():
    data = extract_airports(html_page)
    print data
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()