import math
def run():
    #nationality = input("Enter nationality: ")
    #drug = input("Enter drug name: ")
    #compile(nationality,drug)

    compile("nationality","synthroid")

def compile(region,drug_taken):
    directory = "C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/drug_data_sets/"
    drug = (str(drug_taken)).lower()
    file = open(directory + drug + '_data.txt')



    allele_list = [] # Will store all of the alleles
    pval_list = []

    for line in file:
        for term in line.split():

            if term[:2] == 'rs':
                allele_list.append(term)

            if str(term) == 'void':
                pval_list.append(term)

            try:

                if float(term) < 1 or str(term) == 'void':
                    pval_list.append(term)
            except:
                a = 0

    # Filter out all void terms
    for i in pval_list:
        try:
            float(i)
        except:
            index = pval_list.index(i)
            pval_list.pop(index)
            allele_list.pop(index)


    #print allele_list
    #print pval_list
    populationList = []
    sizeList = []
    refList = []
    altList = []

    for i in allele_list:

        data = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/allele_data_sets/" + drug + "/" + str(i) + ".txt")

        index = 0
        for q in data:
            for datum in q.split('	'):

                if index % 6 == 1:
                    populationList.append(datum)

                if index % 6 == 3:
                    sizeList.append(datum)

                if index % 6 == 4:
                    temp = float(datum[2:])
                    refList.append(temp)

                    alt = round(1 - temp, 4)
                    altList.append(alt)

                index = index + 1


    print refList

    # Created four lists with population, sample size, ref allele and alt allele


def correctNationality(target,study):
    countryList = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/Model/Countries-Continents.csv")

    africaList = []
    asiaList = []
    europeList = []
    northList = []
    oceaniaList = []
    southList = []

    for i in countryList:
        i = str(i)
        if "Africa" in i:
            africaList.append(i[7:-1])
        elif "Europe" in i:
            europeList.append(i[7:-1])
        elif 'Asia' in i:
            asiaList.append(i[5:-1])
        elif "North America" in i:
            northList.append(i[14:-1])
        elif "South America" in i:
            southList.append(i[14:-1])
        elif "Oceania" in i:
            oceaniaList.append(i[8:-1])
    print oceaniaList

#run()
correctNationality("India","India")
