import numpy as np
import matplotlib.pyplot as plt
from helper import *

def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: a numpy ndarray object
    :return: list
    """

    total = 0
    for x in hist:
        total += x #get total number 

    probability = [] #create empty list 
    for y in hist:
        probability.append(y / total)

    return probability
    pass


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list
    :param width: float
    :return: float
    """
    addedprob = 0 
    total = 0 
    for x in histo:
        total += x #get total number of samples 
        
    probability = norm_histogram(histo) #uses norm_histogram to convert to probabilties

    squared = [] #create empty list 
    for element in probability:
        squared.append(element ** 2)

    for element in squared:
        addedprob += element

    J = (2 / ((total - 1) * width)) - ((total + 1) / ((total - 1) * width)) * (addedprob)

    return J
    pass


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin   ro = sweep_n(data, lo, hi, 1, 100)
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """

    J = [] # empty list 
    numberofbin = range(min_bins, max_bins + 1, 1) #+1 to add the min_bins
    for bins in numberofbin:
        histo = plt.hist(data, bins, (minimum, maximum))[0]
        width = (maximum - minimum) / bins
        J.append(compute_j(histo, width)) 

    return J 
    pass


def find_min(l):
    """
    takes a list of numbers and returns the mean of the three smallest number in that list and their index.
    return as a tuple i.e. (the_mean_of_the_3_smallest_values,[list_of_the_3_smallest_values])
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        The you should return ((14+15+23)/3,[0,2,4])

    :param l: list
    :return: tuple
    """

    #sort -> 012 
    sortedlist = sorted(l)
    min1 = sortedlist[0]
    min2 = sortedlist[1]
    min3 = sortedlist[2]

    location1 = l.index(min1)
    location2 = l.index(min2)
    location3 = l.index(min3)

    locationlist = [location1, location2, location3]
    average = (min1 + min2 + min3) / 3

    tuplereturn = (average, locationlist) 
    return tuplereturn
    pass


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
