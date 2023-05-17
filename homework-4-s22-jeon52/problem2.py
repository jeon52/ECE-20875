import statistics

def stencil(data, f, width):
    """

    Params : data(list), f(function), width(int)
    Return : list

    - Perform a stencil using the filter f with width w on list data output the resulting list
    - Note that if len(data) = k, len(output) = k - width + 1; f will accept as input a list of size width and return a single number

    """
    #list of K elements - data 
    #return a list 
    
    k = len(data)
    resultlist = []

    for index in range(k - width + 1): #index goes up to k - 1
        resultlist.append(f(data[index: index + width]))
    return resultlist


def find_covariance_of(series):
    """
    Params  : series : list
    Return  : function, int

    - Create a function to find the covariance between the variable "series" and any input list "window"
    - The function should check if the length of both lists is the same
    - Recall that covariance between two series (lists), let's call them A and B; is calculated as 
        sum( (x_i - u)(y_i - v) )/ N for all i

    - Where,
        - x_i, y_i are the ith elements from A and B respectively
        - u is the mean of list A
        - v is the mean of list B
        - N is the number of elements in either A or B (note that both have to be of the same length.)

    - The function you write should return a function and the width of the sliding window, which is the length of B

    """
    width = len(series)

    # Fill in
    def covariancecalculation (window):
        width1 = len(series)
        width2 = len(window)
        if width2 != width1: 
            print("Both lists have to be of the same size!")

        average1 = statistics.mean(series)
        average2 = statistics.mean(window)
        total = 0

        for index in range(len(series)):
            total += ((series[index] - average1) * (window[index] - average2) / width1)
        return total

    return covariancecalculation, width

            







    


    pass
        
if __name__ == '__main__':
    def mov_avg(L):
        if len(L) != 3:
            raise ValueError(f'Expected list of length 3 but got list of length {len(L)}.')
        return float(sum(L)) / 3
    
    def sum_sq(L):
        if len(L) != 5:
            raise ValueError(f'Expected list of length 5 but got list of length {len(L)}.')
        return sum([i ** 2 for i in L])
    
    
    data = [2.1,2.5,3.6,4.0,2.0,10.0,12.0,14.0]
    
    print(stencil(data, mov_avg, 3))
    print(stencil(data, sum_sq, 5))
    
    cov1, width1 = find_covariance_of([8.0,10.0,12.0])
    print(stencil(data, cov1, width1))
    
    cov2, width2 = find_covariance_of([2.1,2.5,3.6,4.0,2.0])
    print(stencil(data, cov2, width2))
    
