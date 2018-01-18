import re
global charFreq = [0] * 26


def ngrams(n, text):
    newtext = [x for x in text if x.isalpha()]
    return newtext

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


#calcCharFreq(charFreq, word) calculates the character frequency 
def calcCharFreq(charFreq,token):
	for x in token:
		charFreq[rank(x)] += 1

#calculates position of character c in charFreq array
#rank('a') = 0
def rank(c):
	return ord(c) - 97

#returns list of words from file called filename
def give_word_list(filename):
    f = open(filename, 'r')
    words = [token for line in f for token in line.split()]
    return words

"""calc_ngrams_charfreq(?,?,?,?) Please document :)
def calc_ngrams_charfreq(invertedIndex, freqArray, text, n):
    for i in text:
        text[i] = tokenize(text[i])
    return"""

#tokenizes a word
def tokenize(word):
    regex = re.compile('[^a-zA-Z]')
    w = regex.sub('', word)
    w = w.lower()
    return w

def tokenize_word_list(wordlist):
    i = 0
    while i < len(wordlist):
        wordlist[i] = tokenize(wordlist[i])
        i = i + 1
    return wordlist

#print tokenize('Cow.')

#Main
invertedIndex = {}

global n
text1 = give_word_list('austen-emma.txt')
print tokenize_word_list(text1)
calcCharFreq(charFreq, "cattttt")
print charFreq
