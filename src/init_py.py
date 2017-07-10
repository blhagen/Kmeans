#!/usr/bin/env python

# Python script for Kmeans Clustering 

import csv
import os


def init_Program(filename, x, y, numLines):
    cmd = "make"
    os.system(cmd)
    cmd = "./kmeansclustering " + filename + " " + x + " " + y + " " + str(numLines)
    os.system(cmd)

    
def parse(filename, x, y):
    cmd = "wc -l <" + filename
    numLines = int(os.popen(cmd).read()[:-1])
    print numLines
    init_Program(filename, x, y, numLines)
    
    
def user_params():
    inpFlag = False
    while inpFlag == False:
        inpFlag = True
        filename = raw_input("Enter the name of file to be analyzed: ")
        try:
            f = open(filename, "r")
        except IOError:
            inpFlag = False
            print "Error File does not exist"
    inpFlag = [False, False]
    while inpFlag[0] == False and inpFlag[1] == False:
        x = raw_input("Input X field: ")
        y = raw_input ("Input Y field: ")
        f = open(filename, "r+")
        reader = csv.reader(f)
        headers = reader.next()
        for i in headers:
            if x == i:
                inpFlag[0] = True
            if y == i:
                inpFlag[1] = True
        if inpFlag[0] == False or inpFlag[1] == False:
            inpFlag = (False, False)
            print "error, one of the specified fields does not exist"
    parse(filename, x, y)

    
user_params()