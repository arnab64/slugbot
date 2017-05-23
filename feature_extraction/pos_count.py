import re
import nltk
import collections
from nltk import pos_tag
from nltk import word_tokenize
from collections import Counter

'''
tagged = word_tokenize("And now for something completely different")
text = nltk.pos_tag(tagged)
print (text)
counts = Counter(tag for word,tag in text)
print (counts)
'''

target= open('pos_count_chandler.txt','w')

with open('character_data/justtwo_chandler.txt','r') as f:
    for line in f:
        tagged = word_tokenize(line)
        text = nltk.pos_tag(tagged)
        #print (text)
        counts = Counter(tag for word,tag in text)
        target.write(str(counts))
        target.write("\n")
        
target.close()
f.close()