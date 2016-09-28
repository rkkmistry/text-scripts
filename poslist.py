#to use in terminal type "python poslist.py < file.txt"
#this script will print a dictionary that contains lists
#that are grouped by parts of speech and all the unique
#words that are part of each

import sys
from textblob import TextBlob as tb
import pprint

poslist = dict()
text = sys.stdin.read().decode('utf-8')

for word in tb(text).tags:
	if word[1] not in poslist.keys():
		poslist[word[1]] = [word[0]]
	elif word[0] not in poslist[word[1]]:
		poslist[word[1]].append(word[0])



pp = pprint.PrettyPrinter(indent=4)
pp.pprint(poslist)

# print poslist
