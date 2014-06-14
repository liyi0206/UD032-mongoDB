# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
import numpy as np

datafile = "C:/Benben/UD032 mongoDB/Lesson_1_Data_Extraction_Fundamentals/11-Reading_Excel_Files/2013_ERCOT_Hourly_Load_Data.xls"
outfile = "C:/Benben/UD032 mongoDB/Lesson_1Problem_Set/02-Excel_To_CSV/2013_Max_Loads.csv"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data =[]
    times_ex = sheet.col_values(0, start_rowx=1) 
    FIELDS=['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    for i in range(1,9):
        key=FIELDS[i-1]
        value=sheet.col_values(i, start_rowx=1)  
        idx=value.index(max(value))
        time=xlrd.xldate_as_tuple(times_ex[idx],0)
        if i==6:
            data.append([key,time[0],time[1],time[2],time[3],str(np.max(value))])
        else:    
            data.append([key,time[0],time[1],time[2],time[3],np.max(value)])
    return data

def save_file(data, filename):
    open(filename,'wb')
    writer = csv.writer(open(outfile,'wb'), delimiter="|")
    writer.writerow(['Station','Year','Month','Day','Hour','Max Load'])
    for row in data:
        writer.writerow(row)
    
def test():
    data = parse_file(datafile)
    save_file(data, outfile)
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()
   