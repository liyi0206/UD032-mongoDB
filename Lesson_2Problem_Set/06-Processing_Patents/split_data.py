#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'C:/Benben/UD032 mongoDB/Lesson_2Problem_Set/06-Processing_Patents/patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    n = 0
    buff = ''         #initialize buffer
    with open(filename, 'r') as f:
        for e in f:
            if e.startswith("</us-patent-grant>"):     #last line before new document start
                print 'end found'
                buff += e
                writefile = "{}-{}".format(filename, n)
                print writefile, " saved"
                towrite = ET.ElementTree(ET.fromstring(buff))
                towrite.write(writefile, xml_declaration=True)
                towrite.write(writefile, encoding="utf-8", xml_declaration=True)
                buff = ''        #reinitialize buffer
                n += 1
            else:
                buff += e


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()