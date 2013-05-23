"""
Nicholas Pezolano

simple t9 implemntation using a trie

usage: python src.py english.txt
"""

import time
import sys
import itertools
from Bio import trie #trie from the Biopython computational molecular biology library

run_time = time.time()

def t9_prediction(string, t9):
    """Return all the keys in the trie that match anywhere in the string."""
    for word in t.with_prefix(string):
        if len(word) == len(string):
            t9.append(word)
            return t9

#words = [line.strip() for line in open("/home/n/work/py/VR/t9/english.txt",  "rb")]

words = [line.strip() for line in open(sys.argv[1],  "rb")]

t = trie.trie()
for word in words:
    t[word] = 1

mapping = {1:["'"],  2:["a", "A", "b", "B", "c", "C"],          \
                     3:["d", "D", "e", "E", "f", "F"],          \
	             4:["g", "G", "h", "H", "i", "I"],          \
                     5:["j", "J", "k", "K", "l", "L"],          \
                     6:["m", "M", "n", "N", "o", "O"],          \
	             7:["p", "P", "q", "Q", "r", "R", "s","S"], \
                     8:["t", "T", "u", "U", "v", "V"],          \
                     9:["w", "W", "x", "X", "y", "Y", "z","Z"]} \

while True:
    try:
        my_inputs = [int(i) for i in raw_input("Enter space separated inputs: ").split()]
        break
    except:
        pass

digits = []
t9 = []
prediction = []
for numbers in my_inputs:
    digits = map(int, str(numbers))
    strings = [''.join(combo) for combo in itertools.product(*(mapping[d] for d in digits))]
    for string in strings:
        t9_prediction(string, t9)
filter (lambda a: a != [], t9)

D = {v:k for k, v in mapping.items() for v in v}
groups = itertools.groupby(t9, key=lambda x:D.get(x[0]))

print " \n"

for k, g in groups:
    g = list(g)
    if len(g)>1:
        print g,
    else:
        print g[0],

print " \n"
print "Program run time(S)",time.time()-run_time
