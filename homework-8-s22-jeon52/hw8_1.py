#Arguments:
#  filename: name of file to read in
#Returns: a list of strings, each string is one line in the file, 
#    and all of the characters should be lowercase, have no newlines, and have both a prefix and suffix of '__'
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def get_formatted_text(filename) :
    #fill in
    lines = [] #empty list

    with open (filename, "r") as myfile:
        corpus = myfile.read()
        docs = corpus.splitlines()
        lines = ["__" + words.lower().strip() + "__" for words in docs]


    return lines
        
#Arguments:
#  line: a string of text
#   n : Length of each n-gram
#Returns: a list of n-grams
#Notes: make sure to pad the beginning and end of the string with '-'
#       make sure to convert the string to lower-case
#       so "Hello" should be turned into "__hello__" before processing
#       HINT: consider initializing and populating a set and then convert the set to a list and return that list
def get_ngrams(line, n) :
    #fill in
    ngrams = []
    for x in range(len(line) - n + 1): #number of times the for loop should iterate
        ngrams.append(line[x:x+n])

    return ngrams

#Arguments:
#  filename: the filename to create an n-gram dictionary for
#   n : Length of each n-gram
#Returns: a dictionary, with ngrams as keys, and frequency of that ngram as the value.
#Notes: Remember that get_formatted_text gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       use 'map', use get_formatted_text, and use get_ngrams
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def get_dict(filename, n):
    #fill in
    ngram_dict = {}
    ngram_list = [] 

    lines = get_formatted_text(filename) #get sentences 

    for sentence in lines: #gather all the unique words in the corpus into a list 
        ngram_list = get_ngrams(sentence, n) #ngram list of non-unique ngrams
        for word in ngram_list:
            if(not(word in ngram_dict.keys())):
                ngram_dict[word] = 1
            else:
                ngram_dict[word] += 1 

    return ngram_dict

#Arguments:
#   filename: the filename to generate a list of top N (most frequent n-gram, count) tuples for
#   N: the number of most frequent n-gram tuples to have in the output list.
#   n : Length of each n-gram
#Returns: a list of N tuples representing the (n-gram, count) pairs that are most common in the file. It is highly recommended to 
#sort by numerical value first, and for n-grams with the same count, sort them by name within the sorted dict.
# For example
# d = {'a':1,'b':4,'c':2,'d':1,'e':3} -> d = {'b':4,'e':3,'c':2,'a':1,'d':1}
#   To clarify, the first tuple in the list represents the most common n-gram, the second tuple the second most common, etc...
#You may find the following StackOverflow post helpful for sorting a dictionary by its values: 
#Also consider the dict method popitem()
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def top_N_common(filename,N,n):
    common_N = []    
    ngram_dict = get_dict(filename, n)
    dict_inorder = {k: v for k, v in sorted(ngram_dict.items(), key=lambda item: item[1])}

    for x in range(N):
        common_N.append(dict_inorder.popitem())

    return common_N

########################################## Checkpoint, can test code above before proceeding #################################################

#Arguments:
#   filename_list: a list of filepath strings for the different language text files to process
#   n : Length of each n-gram
#Returns: a list of dictionaries where there is a dictionary for each language file processed. Each dictionary in the list
#       should have keys corresponding to the n-grams, and values corresponding to the count of the n-gram
def get_all_dicts(filename_list,n):
    lang_dicts = []
    for filename in filename_list: 
        lang_dicts.append((get_dict(filename, n)))

    return lang_dicts

#Arguments:
#   listOfDicts: A list of dictionaries where the keys are n-grams and the values are the count of the n-gram
#Returns an alphabetically sorted list containing all of the n-grams across all of the dictionaries in listOfDicts (note, do not have duplicates n-grams)
#It is recommended to use the "set" data type when doing this (look up "set union", or "set update" for python)
#Also, for alphabetically sorted, we mean that if you have a list of the n-grams altogether across all the languages, and you call sorted() on it, that is the output we want
def dict_union(listOfDicts):
    union_ngrams = []
    interim_list = []

    for dictinside in listOfDicts:
        for k in dictinside.keys():
            interim_list.append(k) #outputs a list

    union_ngrams.append(sorted(set(interim_list)))

    return union_ngrams


#Arguments:
#   langFiles: list of filepaths of the languages to compare test_file to.
#   n : Length of each n-gram
#Returns a list of all the n-grams across the six languages
def get_all_ngrams(langFiles,n):
    all_ngrams = []

    all_ngrams.append(dict_union(get_all_dicts(langFiles, n)))

    return all_ngrams[0][0]

########################################## Checkpoint, can test code above before proceeding #############################################

#Arguments:
#   test_file: mystery file's filepath to determine language of
#   langFiles: list of filepaths of the languages to compare test_file to.
#   N: the number of top n-grams for comparison
#   n : length of n-gram
# Return a Tuple which is of the format (filename1, filename2, similarity_score), where similarity_score is the score between filename_1 and filename_2
#
# Hint : Normalize the similarity score by dividing the raw similarity by N, so that the value always stays betwen (0,1)
#        Raw similarity is the number of n-grams that are in both languages' top N list
# Note : Please make sure that you detect and ignore similarity measurements for the same language! They will always be the largest!
def compare_langs(langFiles,N,n):
    similarityscore = []
    interimlist = dict()

    for language in langFiles:
        ngram = set([tup[0] for tup in top_N_common(language,N,n)])
        interimlist[language] = ngram

    for i in langFiles:
        for j in langFiles:
            if (i != j):
                similarityscore.append((i, j, len(interimlist[i].intersection(interimlist[j])) / N))

    sortedsimilarity = ([(list1,list2,list3) for list1,list2,list3 in sorted(similarityscore, key = lambda x: x[2])])
    most_similar_pair = sortedsimilarity.pop()

    return most_similar_pair


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    #Test top10Common()
    path = join('ngrams','english.txt')
    print(top_N_common(path,10,3))
    
    #Compile ngrams across all 6 languages and find the two most similar languages and their similarity score for various n-gram lengths 

    path='ngrams'
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    path_list = [join(path, f) for f in file_list]

    for n in range(3,6):
        print(get_all_ngrams(path_list,n)) # list of all n-grams spanning all languages
    
    for n in range(3,6):
        print(compare_langs(path_list, 1000,n)) #Find the similarity between languages
    
