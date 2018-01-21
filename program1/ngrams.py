import re


#compute_ngram_charfreq(invertedIndex, charFile, n, text) computes the frequency
#of each word in the given file.
#invertedIndex is the inverted index
#charFreq is the frequency in which each character appears.
#n is the size of grams (number of tokens).
#text is the text we're working with.
def compute_ngram_charfreq(invertedIndex, charFreq, n, text):
	while i < len(text):
		if (i + n) < len(text):
			ngram = text[i:i+n] 
			str(ngram) #converts ngram to string
			invertedIndex.insert(ngram) #adds/inserts ngram to list invertedIndex 
			
		calcCharFreq(charFreq, text[i])
		
		i = i + 1


#calcCharFreq(char_freq, word) calculates the character frequency 
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
    regex = re.compile('[^a-zA-Z]')
    w = regex.sub('', word)
    w = w.lower()
    return w

#tokenizes a listof words
def tokenize_word_list(wordlist):
    i = 0
    while i < len(wordlist):
        wordlist[i] = tokenize(wordlist[i])
        i = i + 1
    return wordlist
	
	

#####Main######


invertedIndex = {}

#charater frequenct array
#charFreq[0] represents the character a
#charFreq[1] represents the character b
#....
#charFreq[25] represents the character z
global charFreq = [0] * 26

#n is the size of the n-gram 
global n

text1 = give_word_list('austen-emma.txt')
print tokenize_word_list(text1)
calcCharFreq(charFreq, "cattttt")
print charFreq

