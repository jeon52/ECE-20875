import numpy as np
import matplotlib.pyplot as plt

# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    OpenFile = open(datapath)
    data = OpenFile.readlines() #knowledgable

    X = []
    y = []
    for i in data:
        [a,b] = i.split()
        X.append(float(a))
        y.append(float(b))
        
    OpenFile.close #read data and close file 

    for iterate in degrees: #iterating through each degrees
        #call for feature_maxttrix and least_sqaures functions below
        featurematrix = feature_matrix(X, iterate) #call feature_matrix
        leastsquare = least_squares(featurematrix, y)
        paramFits.append(leastsquare) #append the result

    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X = [[feature ** degree for degree in range(d, -1, -1)] for feature in x]
    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    B = np.linalg.inv(X.T @ X) @ X.T @ y 

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    return B


if __name__ == "__main__":
    #step 2
    datapath = "poly.txt"
    degrees = [1,2,3,4,5]

    paramFits = main(datapath, degrees)
    print(paramFits)

    #step 3 
    OpenFile = open(datapath)
    data = OpenFile.readlines() #knowledgable
    X = []
    y = []
    for i in data:
        [a,b] = i.split()
        X.append(float(a))
        y.append(float(b))
        
    OpenFile.close #read data and close file 
    degrees1 = [1,2,3,4,5]
    paramFits1 = main(datapath, degrees1)

    f = 1
    for parameter in paramFits1:
        x = np.linspace(-5, 5)
        y1 = [np.polyval(parameter, k) for k in x]
        plt.plot(x, y1, label = f)
        f += 1
        
    plt.scatter(X, y, color = "black", label = "input vs. output") #data visualization 
    plt.legend()
    plt.title("linear regression at varying degrees")
    plt.xlabel("input")
    plt.ylabel("output")
    plt.show()

    #step 4
    input = 2
    degrees2 = [3]
    paramFits2 = main(datapath, degrees2)
    print(paramFits2)
