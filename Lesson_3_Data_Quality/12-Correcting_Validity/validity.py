"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
    
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same

- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
  
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
from dateutil.parser import parse
import re

INPUT_FILE = 'C:/Benben/UD032 mongoDB/Lesson_3_Data_Quality/12-Correcting_Validity/autos.csv'

OUTPUT_GOOD= 'C:/Benben/UD032 mongoDB/Lesson_3_Data_Quality/12-Correcting_Validity/autos-valid.csv'
OUTPUT_BAD = 'C:/Benben/UD032 mongoDB/Lesson_3_Data_Quality/12-Correcting_Validity/FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        GOODDATA=[]
        BADDATA=[]
        checkYear = re.compile(r'^\d{4}')
        for a in reader:
            if a['URI']<>'URI':
                if a['productionStartYear'] is not None and len(a['productionStartYear'])==25:
                    temp=int(checkYear.match(a['productionStartYear'].strip()).group(0))
                    if 1886<=temp<=2014:
                        a['productionStartYear']=temp
                        #a['productionStartYear']=parse(a['productionStartYear']).year
                        GOODDATA.append(a)
                    else:
                        BADDATA.append(a)
                elif a['productionStartYear']=='NULL':
                    BADDATA.append(a)

        
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in GOODDATA:
            writer.writerow(row)
    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in BADDATA:
            writer.writerow(row)

#def process_file(input_file, output_good, output_bad):
#    checkYear = re.compile(r'^\d{4}')
#    with open(input_file, "r") as f:
#        reader = csv.DictReader(f)
#        header = reader.fieldnames
#        good_data=[]; bad_data=[]
#        for idx, row in enumerate(reader):
#            if not ( row['URI'].find('dbpedia.org') == -1): # ignore row from non dbpedia.org
#                matched = checkYear.match( row['productionStartYear'].strip() )
#            if matched:
#                matchedString = matched.group(0) # extract year
#            if int(matchedString) >= 1886 and int(matchedString) <= 2014: # between 1886-2014
#                print matchedString, row['productionStartYear']
#                row['productionStartYear'] = matchedString
#                good_data.append( row ) 
#            else:
#                bad_data.append( row )


def test():
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()