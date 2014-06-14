#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
    
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'C:/Benben/UD032 mongoDB/Lesson_3Problem_Set/01-Auditing_Data_Quality/cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    for title in FIELDS:
        fieldtypes[title]=set()
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #header = reader.fieldnames
        for line in reader:
            if line['URI'] not in ('URI','http://www.w3.org/2002/07/owl#Thing'):
                for title in FIELDS:
                    if line[title]=='NULL':
                        fieldtypes[title].add(type(None)) 
                    elif line[title][0]=="{":
                        fieldtypes[title].add(type([]))
                    elif is_number(line[title]):
                        fieldtypes[title].add(type(1.1))
                    else: 
                        fieldtypes[title].add(type('str')) 
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
