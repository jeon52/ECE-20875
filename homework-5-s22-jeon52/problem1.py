import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
OpenFile = open ("engagement_1.txt")
data = OpenFile.readlines() #knowledgable
OpenFile.close #read data and close file 
OpenFile2 = open ("engagement_0.txt")
data2 = OpenFile2.readlines() #Not Knowledgable
OpenFile2.close

data = [float(x) for x in data] #convert data from string to float
data2 = [float(x) for x in data2]
populationmean = 0.75

# code for question 2
print('Problem 2 Answers:')
samplesize = len(data)
samplemean = np.mean(data)
samplestd = np.std(data, ddof = 1) #unless we know the population mean -> use ddof = 0 but IDK how this works exactly..
standarderror = samplestd / (samplesize ** 0.5) #or np.sqrt(samplesize)
Zscore = (samplemean - populationmean) / standarderror
Pvalue = 2 * stats.norm.cdf(-abs(Zscore))

print('sample size of knowlegable student is {}'.format(samplesize))
print('sample mean is {}'.format(samplemean))
print('sample standard deviation is {}'.format(samplestd))
print('sample standard error is {}'.format(standarderror))
print('Z score is {}'.format(Zscore))
print('P value is {}'.format(Pvalue))
# code below this line


# code for question 3
print('Problem 3 Answers:')
Pvalueforproblem3 = 0.025
Zscoreforproblem3 = stats.norm.ppf(Pvalueforproblem3) #IS THIS PART CORRECT
SEforproblem3 = (samplemean - populationmean) / Zscoreforproblem3 
samplesize3 = (samplestd / SEforproblem3) ** 2

print("The largest standard error is {}".format(SEforproblem3))
print("The largest samplesize is {}".format(m.ceil(samplesize3)))
# code below this line


# code for question 5
print('Problem 5 Answers:')
samplesize2 = len(data2) # NOT knowledgable 
samplemean2 = np.mean(data2)
samplestd2 = np.std(data2, ddof = 1) 

#SE calculation:
squaredsamplestd2 = (samplestd2 ** 2) / samplesize2
squaredsamplestd = (samplestd ** 2) / samplesize

standarderror2 = np.sqrt(squaredsamplestd + squaredsamplestd2)
testpoint = samplemean2 - samplemean

Zscore2 = (testpoint) / standarderror2 
Pvalue2 = 2 * stats.norm.cdf(-abs(Zscore2))

print('sample size not-knowlegable student is {}'.format(samplesize2))
print('sample mean is {}'.format(samplemean2))
print('sample standard deviation is {}'.format(samplestd2))
print('sample standard error is {}'.format(standarderror2))
print('Z score is {}'.format(Zscore2))
print('P value is {}'.format(Pvalue2))

# code below this line


