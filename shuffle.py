#python shuffle.py [num-lines-of-ouput] file1.txt [weight1] file2.txt [weight 2] ...
#the weight should be between 0-1 and refers to how much you should draw
#from this text relative to the others

from numpy.random import choice
import random
import sys

collect = list()

texts = sys.argv[2:][::2]
weights = sys.argv[3:][::2]

for i in range(int(sys.argv[1])):
	with open(choice(texts, p=weights)) as f:
		print random.choice(f.readlines())
