Creates an output file with a collection of anagrams found in a one word per line dictionary where the number of anagrams is at least as many letters in the anagram. The word must be larger than 4 letters as well.

The underlying assumption is that the anagrams will be identical when all of their letters are sorted into alphabetical order.


HOW TO RUN
----------
There are at least three ways to run this script.

If the location of words file needs to be specific as well as the output location:

	python anagrampy.py wordsDirectory outputDirectory

If you want to have it output the file where the script is located, don't specify outputDirectory:

	python anagrampy.py wordsDirectory

If using a mac or linux, then just run:

	python anagrampy.py

NOTES
-----

For the last option, the script assumes if you're using a Mac, words is in '/usr/share/dict/words/'. If your using Linux, words is in '/usr/dict/words/'. 

If you're using Windows, use the second option or hard code the directory at line 69.

