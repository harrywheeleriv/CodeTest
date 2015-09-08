Creates an output file with a collection of anagrams found in a one word per line dictionary where the number of anagramsis atleast as many letters in the anagram. The word must be larger than 4 letters as well.

The underlying assumption is that the anagrams will be identical when all of their letters are sorted into alphabetical order.

On Line 69 and 79, the directory of the dictionary can written in if you're using Windows and the function fileRead cannot find the file 'words'


HOW TO RUN
----------

If the locations of words file is specific as well as the output location:

	python anagrampy.py wordsDirectory outputDirectory

If you want to have it output the file where the script is located, don't specify outputDirectory:

	python anagrampy.py wordsDirectory

If using a mac or linux, then just run:

	python anagrampy.py