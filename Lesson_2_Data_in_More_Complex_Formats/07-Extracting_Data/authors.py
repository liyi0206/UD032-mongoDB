#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys

import xml.etree.ElementTree as ET

article_file = "C:/Benben/UD032 mongoDB/Lesson_2_Data_in_More_Complex_Formats/07-Extracting_Data/exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {"fnm": None,"snm": None,"email": None}
        
        #for fnm in author: 
        #    data['fnm']=fnm.text
        #for snm in author:
        #    data['snm']=snm.text
        #for email in author:
        #    data['email']=email.text
        
        fname=author.find('fnm')
        if fname is not None:
            data['fnm']=fname.text
        sname=author.find('snm')
        if sname is not None:
            data['snm']=sname.text
        email=author.find('email')
        if email is not None:
            data['email']=email.text      
              
        authors.append(data)
    return authors


def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    
    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]


test()
