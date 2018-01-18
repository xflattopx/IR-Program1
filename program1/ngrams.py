import re

def ngrams(n, text):
    newtext = [x for x in text if x.isalpha()]
    #newtext = [
    return newtext

#returns list of words from file called filename
def give_word_list(filename):
    f = open(filename, 'r')
    words = [token for line in f for token in line.split()]
    return words

def calc_ngrams_charfreq(invertedIndex, freqArray, text, n):
    for i in text:
        text[i] = tokenize(text[i])
        
    return

#tokenizes a word
def tokenize(word):
    regex = re.compile('[^a-zA-Z]')
    w = regex.sub('', word)
    w.lower()
    return w

def tokenize_word_list(wordlist):
    i = 0
    for i in wordlist:
        wordlist[i] = tokenize(wordlist[i])


text1 = give_word_list('austen-emma.txt')

print tokenize_word_list(text1)