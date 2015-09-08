Creates an output file with a collection of anagrams found in a one word per line dictionary where the number of anagrams is atleast as many letters in the anagram. The word must be larger than 4 letters as well.

The underlying assumption is that the anagrams will be identical when all of their letters are sorted into alphabetical order.


HOW TO RUN
----------

If the location of words file needs to be specific as well as the output location:

	python anagrampy.py wordsDirectory outputDirectory

If you want to have it output the file where the script is located, don't specify outputDirectory:

	python anagrampy.py wordsDirectory

If using a mac or linux, then just run:

	python anagrampy.py

For the last option, the script assumes if you're using a Mac, words is in '/usr/share/dict/words/'. If your using Linux, words is in '/usr/dict/words/'.


NOTES
-----
On Line 69 and 79, the directory of the dictionary can be written in if you're using Windows and the function fileRead cannot find the file 'words'.