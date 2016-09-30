#enter in the terminal: "python possplit.py [POS] < file.txt"
#this script inserts a line break in the text 
#at the position of a specific part of speech [POS]

import sys
from textblob import TextBlob as tb

output = ""
choice = sys.argv[1]
text = sys.stdin.read().decode('utf-8')
text = tb(text)

for thing in text.pos_tags:
	if thing[1] == choice:
		output += "{}\n".format(thing[0].encode('utf-8'))
	else:
		output += "{} ".format(thing[0].encode('utf-8'))

print output