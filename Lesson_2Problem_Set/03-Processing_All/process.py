#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".


# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function

# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "C:/Benben/UD032 mongoDB/Lesson_2Problem_Set/03-Processing_All/data/"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")    
    with open("{}/{}".format(datadir, f), "r") as html:
        soup = BeautifulSoup(html)
        dg=soup.find(id="DataGrid1")
        for tr in dg.find_all('tr'):
            temp=[]
            for td in tr.find_all('td'):
                tmp=td.text               
                temp.append(tmp) 
            print temp,type(temp[0]),str(temp[0])
            if temp[0] not in ('Year','<b>2002</b>'):              
                data.append({"courier":info["courier"], "airport":info["airport"],
                            "year":temp[0],"month":temp[1],
                            "flights":{"domestic":temp[2],"international":temp[3]}})

    dataFinal = [] 
    for i in range(0,len(data)): 
        if not str(data[i]['month'])=='TOTAL': 
            data[i]['year']=int(data[i]['year']) 
            data[i]['month']=int(data[i]['month']) 
            tmp=data[i]['flights']["domestic"] 
            data[i]['flights']["domestic"]=int(tmp.replace(",","")) 
            tmp=data[i]['flights']["international"] 
            data[i]['flights']["international"]=int(tmp.replace(",","")) 
            dataFinal.append(data[i]) #print data return dataFinal  
    #print data    
    return dataFinal


def test():
    print "Running a simple test..."
    #open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)

    assert len(data) == 3
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    print "... success!"

if __name__ == "__main__":
    test()