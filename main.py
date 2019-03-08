def run():
    #nationality = input("Enter nationality: ")
    #drug = input("Enter drug name: ")
    #main(nationality,drug)

    main("nationality","synthroid")

def main(region,drug_taken):
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
    studyList = []
    populationList = []
    groupList = []
    sizeList = []
    refList = []
    altList = []

    for i in allele_list:

        #i + "List" = []

        data = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/allele_data_sets/" + drug + "/" + str(i) + ".txt")



        index = 0
        for q in data:
            for datum in q.split('	'):

                if index % 6 == 1:
                    populationList.append(datum)

                if index % 6 == 3:
                    sizeList.append(datum)

                if index % 6 == 4:
                    temp = datum

                    #print list(temp)
                    refList.append(datum)

                if index % 6 == 5:
                    altList.append(datum)

                index = index + 1


    print refList


run()
