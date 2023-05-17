from cv2 import mean
import pandas
#from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split


'''
The following is the starting code for path1 for data reading to make your first step easier.
'dataset_1' is the clean data for path1.
'''
dataset_1 = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
dataset_1['Brooklyn Bridge']      = pandas.to_numeric(dataset_1['Brooklyn Bridge'].replace(',','', regex=True)) 
dataset_1['Manhattan Bridge']     = pandas.to_numeric(dataset_1['Manhattan Bridge'].replace(',','', regex=True))
dataset_1['Queensboro Bridge']    = pandas.to_numeric(dataset_1['Queensboro Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))
dataset_1['Total']  = pandas.to_numeric(dataset_1['Total'].replace(',','', regex=True))
#print(dataset_1.to_string()) #This line will print out your data

#problem 1  
BrookMean = dataset_1["Brooklyn Bridge"].mean()
ManMean = dataset_1["Manhattan Bridge"].mean()
QueenMean = dataset_1["Queensboro Bridge"].mean()
WillMean = dataset_1["Williamsburg Bridge"].mean()
Tot = dataset_1["Total"].mean()

forplot = []
forplot.append(BrookMean)
forplot.append(ManMean)
forplot.append(QueenMean)
forplot.append(WillMean)

#problem 2

#see if there is any correlationship for otuput and the factors individually. 
#Also do the predictions 
#normalize
HighTemp = []
LowTemp = []
Precipitation = []
Total = []

dataset_1['High Temp']      = pandas.to_numeric(dataset_1['High Temp'].replace(',','', regex=True))
dataset_1['Low Temp']      = pandas.to_numeric(dataset_1['Low Temp'].replace(',','', regex=True))
dataset_1['Precipitation']      = pandas.to_numeric(dataset_1['Precipitation'].replace(',','', regex=True))

for i in range(len(dataset_1['High Temp'])): #Data Extraction without number
    HighTemp.append(dataset_1['High Temp'][i])
    LowTemp.append(dataset_1['Low Temp'][i])
    Precipitation.append(dataset_1['Precipitation'][i])
    Total.append(dataset_1['Total'][i])

Xfactor = []
Xfactor.append(HighTemp)
Xfactor.append(LowTemp)
Xfactor.append(Precipitation)

#plt.hist(Xfactor)
#plt.xlabel("Precipitation")
#plt.ylabel("count")
#plt.show()

Xfactortransposed = np.transpose(Xfactor)

x_train, x_test, y_train, y_test = train_test_split(Xfactortransposed, Total, random_state = 0)

meanx = np.mean(x_train, axis = 0)
stdx = np.std(x_train, axis = 0)
meany = np.mean(y_train)
stdy = np.std(y_train)

print("this is x mean", meanx)
print("this is x std", stdx)
print("this is y mean", meany)
print("this is y std", stdy)

X_train_normalized = (x_train - meanx) / stdx
Y_train_normalized = (y_train - meany) / stdy
X_test_normalized = (x_test - meanx) / stdx
Y_test_normalized = (y_test - meany) / stdy

regr = LinearRegression(fit_intercept = True)
regr.fit(X_train_normalized , Y_train_normalized)

prediction = regr.predict(X_test_normalized)

#print("MSE is", mean_squared_error(Y_test_normalized, prediction))
#print("Rsquared value is", r2_score(Y_test_normalized, prediction))




