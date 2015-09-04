# Write a program to find all of the anagrams in a dictionary
# in which there are at least 4 letters in the word and at least
# as many anagrams as there are letters.
#
#
# By Harry Wheeler

import sys
import csv


def anagrab(dictionary, repeatIndex):
    """
        Inputs are a list of the repeated indicies when the words in dictionary are sorted in alphabetical order. A list is built
        that contains all of the potential anagrams, and a second list is built where each row has a collection of words that are
        exactly the same when the word is sorted into alphabetical order. Returns a list of anagram lists. Prints out the temp list
        when it meets the code test criteria.

    """

    anagrams = [dictionary[i] for i in repeatIndex]
    seen = set()
    finalList = []
    for index, keyWord in enumerate(anagrams):

        #build a temp list to see if it has an equal amount or more of anagrams as letters
        temp = [word for word in anagrams if ''.join(sorted(word)) == ''.join(sorted(keyWord)) ]

        #do nothing if temp is empty
        if temp == []: continue

        # append the temp list into the finalList. If for some reason temp was seen already
        # don't append it to finalList
        if letterCount(temp[0]) <= len(temp) and (''.join(temp) not in seen):
            print(temp)
            finalList.append(temp)
            seen.add(''.join(temp))
    return finalList


def sortDict(dictionary):
    """
        Sort the strings themselves in the inputted list into alphabetical order and forces all letters to be lowercase. Return the list.
    """
    return [ ''.join(sorted(item.lower())) for item in dictionary]

def repeatIndex(dictionary):
    """
        Creates a list of the indicies in dictionary that contain strings that are repeated.
    """

    seenRepeats = set()
    seenRepeats_add = seenRepeats.add
    return [ indexRepeats for indexRepeats, word in enumerate(dictionary) if word in seenRepeats or seenRepeats_add(word)]

def fileRead():
    """
        Reads in the dictionary file that contains one word per line,. Keeps the words that are purely alphabetical and longer than four characters and returns them.
        
    """

    if sys.platform == 'win32':
        #I use a windows machine at home.
        wordsDirectory = 'D:\\Research\\CodingTest\\usr\\'
        wordsFile = 'words.txt'
        fullNameAndPath= wordsDirectory + wordsFile

    fourLetters = []
    with open(fullNameAndPath,'U') as rawfile:

        for row in rawfile:
            # if the word pulled from rawfile is purely alphabetical, and is greater than or equal to four characters long, save it
            if (removeNextLine(row).isalpha()) and (letterCount(removeNextLine(row)) >= 4):
                fourLetters.append(removeNextLine(row))
           
    return fourLetters

def fileOutput(directory, dictionary):
    """
        Takes all of the inputted data, and outputs a file named 'wheelersOutput.txt' in the chosen directory, if applicable.
    """
    if directory is not None:
        if (directory[-1] != '\\') or (directory[-1] != '/'):
            fullNameAndPath = directory + '/' + 'wheelersOutput.txt'
        else:
            fullNameAndPath = directory + 'wheelersOutput.txt'

    with open(fullNameAndPath, 'wb') as outfile:
        writer = csv.writer(outfile,delimiter=',')
        for words in dictionary:
            # used the list comprehension to include a leading space on the word if its not the first
            # value in the row
            writer.writerow([" "+word if word != words[0] else word for word in words ])
    return 
    
def letterCount(word):
    """
        Counts the number of letters in an inputted string. Can be used for number of element in a list as well.
    """
    return len([letter for letter in word])

def removeNextLine(word):
    """
        Removes \n character
    """
    return word.rstrip('\n')

    

if __name__ == "__main__":
    import os
    import sys


    # read in files
    dictionary = fileRead()
    # gather indexes of repeated alphabetized words
    indexes = repeatIndex(sortDict(dictionary))
    #collect anagrams
    anagrams = anagrab(dictionary, indexes)
    #output results
    fileOutput(os.getcwd(),anagrams)
    print('Number of anagram sets: ' + letterCount(anagrams))
    print('Outputted file wheelersOutput.txt to ' + os.getcwd())


    
