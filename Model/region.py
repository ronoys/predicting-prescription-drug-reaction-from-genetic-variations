import os
def identifyRegion(region,drug):

    # Iterates through all allele files
    directory = "C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/allele_data_sets/" + drug.lower()
    for file in os.listdir(directory):
        f = open(directory + "/" + file)
        for row in f: # For each row in each files
            for term in row.split("	"):
                print term
