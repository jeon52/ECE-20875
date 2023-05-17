from helper import remove_punc
from hw8_1 import *
import nltk
from nltk.corpus import stopwords
import numpy as np

#Clean and prepare the contents of a document
#Takes in a file name to read in and clean
#Return a single string, without stopwords, spaces, and punctuation
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def read_and_clean_doc(doc) :
    #1. Open document, read text into *single* string
    with open(doc, "r") as myfile:
        corpus = myfile.read()
    
    #2. Filter out punctuation from list of words (use remove_punc)
    docs_clean = remove_punc(corpus)

    #3. Make the words lower case
    docs_lowered = docs_clean.lower()

    #4. Filter out stopwords
    #5. Remove remaining whitespace
    stop = stopwords.words('english')

    removestopword = docs_lowered.split(' ')
    remove = [loweredwords for loweredwords in removestopword if loweredwords not in stop]
    all_no_stop = ''.join(remove)

    return all_no_stop
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames* and a number *n* corresponding to the length of each ngram
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per ngram (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the list of ngrams output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of ngrams that should correspond to the columns in
#docword
def build_doc_word_matrix(doclist, n) :
    #1. Create the cleaned string for each doc (use read_and_clean_doc)
    # column - = each document 
    # row | = ngrams
    #(1,3) -> (1,1,1) -> 1 row 3 column

    docs_clean = [read_and_clean_doc(file) for file in doclist]
    ngram_list = [] #all list
    uniquelist = [] #unique list
    interimlist = []
    frequencylist = []

    for eachdoc in docs_clean: #gather all the unique words in the corpus into a list 
        ngram_list = get_ngrams(eachdoc, n) #ngram list of non-unique ngrams
        for word in ngram_list:
            if(not(word in uniquelist)):
                uniquelist.append(word)

    length = len(uniquelist)
    uniquelist.sort()
    ngramlist = uniquelist

    for eachdoc in docs_clean:
        interimlist = get_ngrams(eachdoc, n) #ngram list of non-unique ngrams
        empty_matrix = [0] * length #maximum number of columns
        for word in interimlist:
            index = uniquelist.index(word)
            empty_matrix[index] += 1
        frequencylist.append(empty_matrix)  

    docword = np.array(frequencylist) #convert to numpy array

    #2. Create and use ngram lists to build the doc word matrix
            
    return docword, ngramlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def build_tf_matrix(docword) :
    sum = np.sum(docword,axis = 1)[:, np.newaxis]
    tf = docword / sum

    #fill in
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of ngrams in the doc word matrix)
#Don't forget the log factor!
def build_idf_matrix(docword) :
    sum = np.sum(docword > 0, axis = 0)
    idf = np.log10(docword.shape[0] / sum).reshape(1,-1)

    #fill in
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword) :
    tf = build_tf_matrix(docword)
    idf = build_idf_matrix(docword)

    tfidf = tf * idf
    
    #fill in
    return tfidf
    
#Find the three most distinctive ngrams, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most unique ngrams in each document
def find_distinctive_ngrams(docword, ngramlist, doclist) :
    distinctive_words = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    for loop in range(len(doclist)):
        tfidf = build_tfidf_matrix(docword)
        distinctive_words[doclist[loop]] = list(np.array(ngramlist)[np.argsort(-tfidf[loop,:])[:3]])

    return distinctive_words


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    #Some main code:
    '''directory='lecs'
    path = join(directory, '1_vidText.txt')
    read_and_clean_doc(path)
    #build document list
    
    path='lecs'
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    path_list = [join(path, f) for f in file_list]
    
    mat,wlist=build_doc_word_matrix(path_list)
    
    tfmat = build_tf_matrix(mat)
    idfmat = build_idf_matrix(mat)
    tfidf = build_tfidf_matrix(mat)
    results = find_distinctive_words(mat,wlist,file_list)'''
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    
    print("*** Testing read_and_clean_doc ***")
    print(read_and_clean_doc(path1)[0:20])
    print("*** Testing build_doc_word_matrix ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist, 3)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing build_tf_matrix ***") 
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing build_idf_matrix ***") 
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    print("*** Testing build_tfidf_matrix ***") 
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing find_distinctive_words ***")
    print(find_distinctive_ngrams(docword, wordlist, doclist))
