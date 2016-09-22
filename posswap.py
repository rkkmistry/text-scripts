#python posswap.py source-text.txt [pos] injected-text.txt [pos] [prob]
#[pos] refers to Part of Speech 
#if you put in "noun_phrases" however, 
#you will get those (only works for injected though)
#[prob] refers to how often it will make
#the replacement, put 1 if you want it
#to do it everytime and more if you want it do it less

import sys
import random
from textblob import TextBlob as tb

source = open(sys.argv[1], 'r').read()
source_pos = sys.argv[2]

inject = open(sys.argv[3], 'r').read()
inject_pos = sys.argv[4]

prob = int(sys.argv[5])

#gets a particular part of speech from a string
def getPOS(pos, text):
	final = list()
	for sent in tb(text.decode('utf-8')).sentences:
		for tag in sent.tags:
			if tag[1] == pos:
				final.append(tag[0])
	return final

#gets noun phrases from a string
def getNPhrases(text):
	final = list()
	for np in tb(text.decode('utf-8')).noun_phrases:
		final.append(np)
	return final

#replaces certain POS by drawing (potentially at random) from a list of words
def replacePOS(pos, text, insert, prob=1):
	final = list()
	for sent in tb(text.decode('utf-8')).sentences:
		sentcollect = []
		for tag in sent.tags:
			if tag[1] == pos and random.randint(1, prob) == 1:
				sentcollect.append(random.choice(insert))
			else:
				sentcollect.append(tag[0])
		final.append(sentcollect)
	return final

#prints out a list of lists of words in a nice way
def nestedprint(text):
	playnice = ""
	for sentence in text:
		playnice += ' ' + ' '.join(sentence) + '.'
	print playnice

if inject_pos == "noun_phrases":
	inject = getNPhrases(inject)
else:
	inject = getPOS(inject_pos, inject)

output = replacePOS(source_pos, source, inject, prob)
nestedprint(output)




