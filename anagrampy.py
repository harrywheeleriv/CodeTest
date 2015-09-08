# Write a program to find all of the anagrams in a dictionary
# in which there are at least 4 letters in the word and at least
# as many anagrams as there are letters.
#
#
# Underlying assumption: the anagrams will be identical when all of
#                       their letters are sorted into alphabetical order.
#
# By Harry Wheeler

import sys
import csv
from collections import defaultdict

def listDupes(sortedDictionary):
    """
        Contructs a defaultdict object of all the words inputted in sortedDictionary where:
            - keywords are the word that was repeated 
            - items in the dictionary are the indicies in
            
        The inputted dictionary should have had the string entries sorted in alphabetical order.

        Returns a list of lists with the locations (indicies) of words that are repeated atleast twice
    """

    dupes = defaultdict(list)
    for index,word in enumerate(sortedDictionary):
        dupes[word].append(index)
    return [locations for keys,locations in dupes.items() if len(locations) > 1]

def anagrab(dictionary,sortedDictionary):
    """
        Uses the list of index lists created from listDupes() to build a list of anagrams. The indicies returned from listDupes() point to anagram locations in dictionary.
    """

    # list of lists containing index locations
    repeatLocations = listDupes(sortedDictionary)
    anagrams = []
    for locations in repeatLocations:
        # check if the number of anagrams >= number of letters of the first found anagram
        if len(locations) >= len(dictionary[locations[0]]):
            # if so, build a list of the anagrams, append anagrams
            anagrams.append([dictionary[i] for i in locations])

    return anagrams

def sortDict(dictionary):
    """
        Sort the strings themselves in the inputted list into alphabetical order and forces all letters to be lowercase. Return the list.
            Ex. will sort 'post', 'stop', 'spot' and 'tops' into 'opst'  
    """
    return [''.join(sorted(item.lower())) for item in dictionary]

def fileRead(directory=None):
    """
        Reads in the dictionary file that contains one word per line. Keeps the words that are:
            - purely alphabetical
            - longer than four characters
            - all lower case and not repeated (Ex. prevents State and state from both being passed on)

        It will identify if the user is on a mac, linux, or windows machine.
            - On Mac, it will look in '/usr/share/dict/words/'
            - On Linux, it will look in '/usr/dict/words/'
            - On Windows, you'll need to input a directory
    """
    if directory == None:
        if sys.platform == 'win32':
            #I use a windows machine at home and this is where I put my words.txt
            wordsDirectory = 'D:\\Research\\CodingTest\\usr\\'
            wordsFile = 'words.txt'
            fullNameAndPath= wordsDirectory + wordsFile
            if os.path.exists(wordsDirectory) != True:
                print("Looks like you're using Windows. You'll need to specify where the words file is. Do this by inputting it as a sys.argv when calling the script, or hard coding it on line 69 and 70. \n \n Ex. python 'wordsDirectory' 'outputDirectory'")
                
        elif sys.platform == 'darwin':
            wordsDirectory = '/usr/share/dict/words/'
            wordsFile = 'words'
        elif sys.platform == 'linux2':
            wordsDirectory = '/usr/dict/words/'
            wordsFile = 'words'
    else:
        if (directory[-1] != '\\') or (directory[-1] != '/'):
            fullNameAndPath = directory + '/' + 'words'
        else:
            fullNameAndPath = directory + 'words'
        
    fourLetters = []
    # the set will be used as an efficient check for repeats
    seen = set()
    with open(fullNameAndPath,'U') as rawfile:

        for row in rawfile:
            # if the word pulled from rawfile is purely alphabetical, and is greater than or equal to four characters long,
            # and hasn't been seen before, save it
            if (removeNextLine(row).isalpha()) and (len(removeNextLine(row)) >= 4) and (removeNextLine(row.lower()) not in seen):

                #save the word to the list with \n removed and all lowercase
                fourLetters.append(removeNextLine(row.lower()))
                # add it to the seen set with \n removed and all lowercase
                seen.add(removeNextLine(row.lower()))
           
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
    else:
        fullNameAndPath = 'wheelersOutput.txt'
        
    with open(fullNameAndPath, 'wb') as outfile:
        writer = csv.writer(outfile,delimiter=',')
        for words in dictionary:
            # used the list comprehension to include a leading space on the word if its not the first
            # value in the row
            writer.writerow([" "+word if word != words[0] else word for word in words ])
    return 
    

def removeNextLine(word):
    """
        Removes \n character from a word
    """
    return word.rstrip('\n')  

if __name__ == "__main__":
    import os
    import sys
    
    # useful to call this script as
    #   python anagrampy.py 'wordsDirectory' 'outputDirectory'
    
    # if user doesn't call python anagrampy.py 'wordsDirectory' 'outputDirectory', set wordsDirectory to None.
    try:
        wordsDirectory = sys.argv[1]
    except IndexError:
        wordsDirectory = None

    # read in words at wordsDirectory
    dictionary = fileRead(wordsDirectory)

    #collect anagrams
    anagrams = anagrab(dictionary,sortDict(dictionary))

    # if user doesn't call python anagrampy.py 'wordsDirectory' 'outputDirectory', set outputDirectory to None.
    try:
        outputDirectory = sys.argv[2]
    except IndexError:
        outputDirectory = os.getcwd()
    
    #output results
    fileOutput(outputDirectory,anagrams)
    print('Number of anagram lists: ' + str(len(anagrams)))
    print('Outputted file wheelersOutput.txt to ' + outputDirectory)


    
