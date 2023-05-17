def histogram(data, n, b, h):
    # data is a list -> []
    # n is an integer -> number of bins between the bound 
    # b and h are floats -> b is a lower bound , h is a upper bound
    
    # Write your code here
    if b == h: #if b and h are the same
        print("b and h are the same value") #print this message
        empty = [] #create a empty list 
        return empty #return the list
    elif b > h:
        temp = h #exchange b and h 
        h = b
        b = temp
    elif n <= 0: #when negative value
        empty = [] #return a empty list 
        return empty
    
    hist = [0] * n #create a list called hist with n numbers of 0 
    w = (h - b) / n #calculate width of the bin 
    
    for loop in data: #go through every element in given data
        if loop > b and loop < h:
            i = (loop - b) // w #check where the data value should be located in 
            integeri = int(i) #convert from float to integer
            hist[integeri] += 1 #update 
        else:
            continue

    return hist

    #hist[0] represents (b, b + w)
    #hist[1] represents [b + w, b + 2w)
    #hist[n-1] represents [b + (n)*w , b + (n+1)*w)

    # return the variable storing the histogram
    # Output should be a list
    pass


def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    #combine these three values into 1 dictionary - month_to_all
        #month is key 
        #name, (day, year, age) -> value, list value
        #current year should be 2022
    # Write your code here

    # return the variable storing name_to_all
    # Output should be a dictionary
    month_to_all = {}
    currentyear = 2022
    for name in name_to_month: #key is name, value is month
        month = name_to_month[name]
        day = name_to_day[name]
        year = name_to_year[name]
        age = currentyear - year
        month_to_all[month] = (name, (day, year, age))

    #for name, year in name_to_year:
    return month_to_all
    pass
