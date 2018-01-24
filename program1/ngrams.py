import re


#compute_ngram_charfreq(invertedIndex, charFile, n, text) computes the frequency
#of each word in the given file.
#invertedIndex is the inverted index
#charFreq is the frequency in which each character appears.
#n is the size of grams (number of tokens).
#text is the text we're working with.
def compute_ngram_charfreq(invertedIndex, charFreq, n, text):
	i = 0
	while i < len(text):
		if (i + n) < len(text):
			ngram_as_list = text[i:i+n] 
			ngram = " ".join(ngram_as_list) #converts ngram to string
			
			#adds/inserts ngram to dictonary invertedIndex
			if ngram in invertedIndex:
				invertedIndex[ngram] += 1
			else:
				invertedIndex[ngram] = 1
		
		compute_char_freq(charFreq, text[i])
		
		i = i + 1


#compute_char_freq(char_freq, word) calculates the character frequency 
def compute_char_freq(char_freq, token):
	for i in token:
		char_freq[rank(i)] += 1

#calculates position of character c in charFreq array
#rank('a') = 0
def rank(char):
	return ord(char) - 97

#returns list of words from file called filename
def give_word_list(filename):
    f = open(filename, 'r')
    words = [token for line in f for token in line.split()]
    return words

#tokenizes a word
def tokenize(word):
    regex = re.compile('[^a-zA-Z]+')
    w = regex.sub('', word)
    w = w.lower()
    return w

#tokenizes a list of words
def tokenize_word_list(wordlist):
    i = 0
    while i < len(wordlist):
	#regex = re.compile('[^a-zA-Z]+')
        wordlist[i] = tokenize(wordlist[i])
        i = i + 1
    return wordlist

#writes the charater frequency to an output file
def write_char_freq(charFreq):
    outf = open('charfreq.txt', 'w')
    i = 0
    while i < len(charFreq):
        outf.write(chr(i + 97) + " : " + str(charFreq[i]) + "\n")
        i += 1
    outf.close()

#read in all the files in a loop
def processCorpus(inputList, charFreq, invertedIndex):
    i = 0
    while i < len(inputList):
        text = give_word_list(inputList[i])
	print("processing %s" %inputList[i])
	text = tokenize_word_list(text)
	compute_ngram_charfreq(invertedIndex, charFreq, n, text)
	i +=  1


#####Main######


invertedIndex = {}

#charater frequenct array
#charFreq[0] represents the character a
#charFreq[1] represents the character b
#....
#charFreq[25] represents the character z
charFreq = [0] * 26

#n is the size of the n-gram 
n = 2

inputFiles = give_word_list('input-files.txt')
processCorpus(inputFiles, charFreq, invertedIndex)

print charFreq

IItuples = [(value, key) for key, value in invertedIndex.iteritems()]
SortedTuples = sorted(IItuples, key=lambda x: x[0], reverse=True)

#print IItuples
#print SortedTuples

j = 0
while j < 10:
	print SortedTuples[j]
	j += 1

write_char_freq(charFreq)
