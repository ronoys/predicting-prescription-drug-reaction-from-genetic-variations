from main import run
specificAlelle, averageAllele = run()

print specificAlelle
print averageAllele

difference = specificAlelle - averageAllele


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=50)

#[result from drug,average for drug, compared to other drugs]

X = [[.2,.3],[.27,.3],[.3,.3],[.33,.3],[.4,.3]]

Y = ['Category 1','Category 2','Category 3','Category 4','Category 5']

clf = clf.fit(X, Y)

prediction = clf.predict([[specificAlelle,averageAllele]])

print prediction
