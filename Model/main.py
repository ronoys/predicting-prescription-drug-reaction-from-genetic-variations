import math

def run():
    nationality = input("Enter nationality: ")
    drug = input("Enter drug name: ")
    #return compile(nationality,drug)
    return compile(nationality,drug)
    #compile("India","synthroid")

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

    new_p_list = []
    for z in pval_list:
        new_p_list.append(float(z))

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


    #print populationList, sizeList, refList, altList
    total = 0
    fakeTotal = 0
    newPopulationList = []
    newSizeList = []
    newRefList = []
    newAltList  = []
    pval = float(sum(new_p_list))/float(len(new_p_list))



    #print pval

    for i in range(0,len(populationList)):
        if correctNationality(region,populationList[i]) == True:
            newPopulationList.append(populationList[i])
            newSizeList.append(sizeList[i])
            newRefList.append(refList[i])
            newAltList.append(altList[i])

    #print newSizeList, newRefList, newAltList

    for r in range(0,len(newSizeList)-1):
        total = total + (float(newRefList[r]) * float(newSizeList[r]))
        fakeTotal = fakeTotal + (float(newAltList[r]) * float(newSizeList[r]))

        #print total, fakeTotal
    sum1 = total + fakeTotal
    averageRef = (total/sum1) * pval
    averageAlt = (fakeTotal/sum1) * pval

    newRefTotal = 0
    newAltTotal = 0

    for l in range(0,len(populationList)):
        newRefTotal = newRefTotal + (float(refList[r])*float(sizeList[r]))
        newAltTotal = newAltTotal + (float(altList[r]) * float(sizeList[r]))

    newSum = newRefTotal + newAltTotal
    newAverageRef = (newRefTotal/newSum) * pval
    newAverageAlt = (newAltTotal/newSum) * pval

     # displays an average
    #print newAverageAlt

    #print ("Average Reference Allele: " + str(averageRef * pval) )
    #print ("Average Alternate Allele: " + str(averageAlt * pval))
    return averageRef, newAverageRef # displays the result

def correctNationality(target,study):
    countryList = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/Model/Countries-Continents.csv")

    africaList = []
    asiaList = []
    europeList = []
    northList = []
    oceaniaList = []
    southList = []
    bigList = []
    answer = ""

    # Assigns country lists
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

    bigList = africaList + asiaList + europeList + northList + oceaniaList + southList

    # Find region of the target -- Works
    if target in bigList:
        if target in africaList:
            answer =  "Africa"
        elif target in europeList:
            answer = "Europe"
        elif target in asiaList:
            answer = "Asia"
        elif target in northList:
            answer = "North America"
        elif target in oceaniaList:
            answer = "Oceania"
        elif target in southList:
            answer = 'South America'


    # Hard Assign
    if study == "American":
        study = "North America"
    if study == "African":
        study = "Africa"
    if study == "European":
        study = "Europe"
    if study == "Asian" or study == "East Asian" or study == 'South Asian':
        study = "Asia"

    if study == "Global":
        study = answer

    if answer == study:
        return True
    else:
        return False
