import os
#print (os.getcwd() + "hi")

'''
f = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/drug_data_sets/crestor_data.txt")

for item in


count = 0

variantList = []
idList = []
pList = []

for line in f:
    for term in line.split(" "):

        if term[:2] == "rs":
            variantList.append(term)
        elif term > 100000:
            idList.append(term)
        else:
            pList.append(term)




print idList
'''

import os

directory = 'C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/allele_data_sets/synthroid'

for file in os.listdir(directory): # for each file
    #print file
    f = open(directory + "/" + file)
    for row in f: # For each row in each files
        for term in row.split("	"):
            print term

#file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))]
#print file_list
