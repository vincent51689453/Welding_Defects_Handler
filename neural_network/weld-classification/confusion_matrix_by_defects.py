import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

predset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\predicted_results.csv", error_bad_lines=False, header=None)
testset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\testing_results.csv", error_bad_lines=False, header=None)

predset = predset.values
testset = testset.values

incompen = []
incomfus = []
porosity = []
underfill = []

testincompen = []
testincomfus = []
testporosity = []
testunderfill = []

for i in predset:
    incompen.append(i[0])
    incomfus.append(i[1])
    porosity.append(i[2])
    underfill.append(i[3])

for k in testset:
    testincompen.append(k[0])
    testincomfus.append(k[1])
    testporosity.append(k[2])
    testunderfill.append(k[3])

cm = confusion_matrix(testincompen, incompen)
print(cm)
print("accuracy for incompen is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity for incompen is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity for incompen is: ", (cm[1][1]/np.sum(cm[1]))*100)

cm = confusion_matrix(testincomfus, incomfus)
print(cm)
print("accuracy for incomfus is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity for incomfus is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity for incomfus is: ", (cm[1][1]/np.sum(cm[1]))*100)
cm = confusion_matrix(testporosity, porosity)
print(cm)
print("accuracy for porosity is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity for porosity is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity for porosity is: ", (cm[1][1]/np.sum(cm[1]))*100)

cm = confusion_matrix(testunderfill, underfill)
print(cm)
print("accuracy for underfill is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity for underfill is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity for underfill is: ", (cm[1][1]/np.sum(cm[1]))*100)
