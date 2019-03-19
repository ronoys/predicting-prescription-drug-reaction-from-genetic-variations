from main import autoRun
import random
import plotly.plotly as py
import plotly.tools as tls
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

countryList = open("C:/Users/ronoy/Documents/GitHub/predicting-prescription-drug-reaction-from-genetic-variations/Model/Countries-Continents.csv")

africaList = []
asiaList = []
europeList = []
northList = []
oceaniaList = []
southList = []
bigList = []
answer = ""

xList = []
yList = []
fullCountryList = []

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


chanceList = []
relChanceList = []

for i in bigList:

    origchance, origrelChance = autoRun(i,"synthroid")

    #a = random.uniform(chance,chance)
    #b = random.uniform(relChance,relChance)

    a = random.uniform(-.05*origchance,.05*origchance)
    b = random.uniform(-.05*origrelChance,.05*origrelChance)



    chance = origchance + a
    relChance = origrelChance + b


    xList.append(chance)
    yList.append(relChance)
    chanceList.append(origchance)
    relChanceList.append(origrelChance)

    i = str(i)
    if i in africaList:
        fullCountryList.append('Africa')
    elif i in europeList:
        europeList.append(i[7:-1])
        fullCountryList.append('Europe')
    elif i in asiaList:
        fullCountryList.append('Asia')
    elif i in northList:
        fullCountryList.append('North America')
    elif i in southList:
        fullCountryList.append('South America')
    elif i in oceaniaList:
        fullCountryList.append('Oceania')


zippedList = list(zip(fullCountryList,bigList,xList,yList))
df = pd.DataFrame(zippedList,columns=['Region','Country','Percent Risk','Percent Compared Risk'])


ax = sns.lmplot(x='Percent Risk', y='Percent Compared Risk', data=df, fit_reg=False, scatter_kws={"alpha":0.8,"s":50} , hue='Region')

ax.fig.suptitle("Ventolin Clusters")

plt.show()
#np.savetxt(r'C:/Users/ronoy/Documents/Python/pip/np.txt', df.values)#, fmt='%d')
df.to_csv('C:/Users/ronoy/Documents/Python/pip/np.txt', header=True, index=False, sep='\t', mode='a')
#print df
