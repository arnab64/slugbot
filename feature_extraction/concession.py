import re
import nltk
import nltk.data
'''
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp1 = open('test.txt','r')
fp2= open('output.txt','w')
data = fp1.read()
fp2.write('\n'.join(tokenizer.tokenize(data)))
'''
conc=open('conc.txt','r')

for word in conc:
    b = word.split()

print (b)


f=open('output.txt','r')

for line in f:
    m = re.split("|".join(b), line) 
    m.remove(m[0])
    print(m)

f.close()
fp1.close() 
fp2.close()
conc.close()