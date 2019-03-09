
'''
import os

directory = 'C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/allele_data_sets/synthroid'

for file in os.listdir(directory): # for each file
    #print file
    f = open(directory + "/" + file)
    for row in f: # For each row in each files
        for term in row.split("	"):
            print term


'''

import math
