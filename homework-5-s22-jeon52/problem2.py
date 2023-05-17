import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

# code for question 1
print('Problem 1 Answers:')
# code below this line
samplesize = len(data)
samplemean = np.mean(data)
print("mean is {}".format(samplemean))
samplestd = np.std(data, ddof = 1)
standarderror = samplestd / (samplesize ** 0.5)
print("standard error is {}".format(standarderror))
c = .9
df = samplesize - 1
t = stats.t.ppf(1 - (1 - c) / 2, df)
print("t score is {}".format(t))

botci = samplemean - samplestd/(np.sqrt(samplesize)) * t
topci = samplemean + samplestd/(np.sqrt(samplesize)) * t

print("bottom confidence interval is {}".format(botci))
print("top confidence interval is {}".format(topci))

# code for question 2
print('Problem 2 Answers:')
# code below this line
c = 0.95
df = samplesize - 1
t = stats.t.ppf(1 - (1 - c) / 2, df)
print("t score is {}".format(t))
botci = samplemean - samplestd/(np.sqrt(samplesize)) * t
topci = samplemean + samplestd/(np.sqrt(samplesize)) * t
print("bottom confidence interval is {}".format(botci))
print("top confidence interval is {}".format(topci))

# code for question 3
print('Problem 3 Answers:')
# code below this line
populationstd = 15.836
standarderror = populationstd / (samplesize ** 0.5)
print("standard error is {}".format(standarderror))
c = 0.95
z = stats.norm.ppf(1 - (1 - c) / 2) 
print("z score is {}".format(z))
botci = samplemean - populationstd/(np.sqrt(samplesize)) * z
topci = samplemean + populationstd/(np.sqrt(samplesize)) * z
print("bottom confidence interval is {}".format(botci))
print("top confidence interval is {}".format(topci))


# code for question 4
print('Problem 4 Answers:')
# code below this line
c = 0.8225
t = stats.t.ppf(1 - (1 - c) / 2, df)
print("t score is {}".format(t))
botci = samplemean - samplestd/(np.sqrt(samplesize)) * t
topci = samplemean + samplestd/(np.sqrt(samplesize)) * t
print("bottom confidence interval is {}".format(botci))
print("top confidence interval is {}".format(topci))

