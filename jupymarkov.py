#to run this in the terminal type "python jupymarkov.py [order-level] [num-output] < file-name.txt"
#
#[order-level] refers to how many characters the script looks at at a time,
#so a lower number means less coherent output but more variable content,
#while a higher number will create more coherent content but will end up
#duplicating some of the input text--try 5 to start as that is the average
#length of a word in english
#
#[num-output] refers to how many characters of output you want
#
#make sure your input file is a plain text format (.txt)

from collections import *
from random import random
import sys

def train_char_lm(fname, order):
    data = fname
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in xrange(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.iteritems()]
    outlm = {hist:normalize(chars) for hist, chars in lm.iteritems()}
    return outlm

def generate_letter(lm, history, order):
    history = history[-order:]
    dist = lm[history]
    x = random()
    for c,v in dist:
        x = x - v
        if x <= 0: return c

def generate_text(lm, order, nletters, seed="~"):
    if seed == "~":
        history = seed * order
    else:
        history = seed
    out = []
    for i in xrange(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)

theOrder = int(sys.argv[1])
theAmount = int(sys.argv[2])
lm = train_char_lm(sys.stdin.read(), theOrder)
print generate_text(lm, theOrder, theAmount)
