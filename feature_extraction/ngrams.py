import nltk
import csv
import operator
from nltk.util import ngrams
from collections import Counter

fp1 = open('chandler_punct.txt','r')
data = fp1.read()

token = nltk.word_tokenize(data)
bigrams = ngrams(token,2)

csv_bigram = Counter(bigrams)

writefile = open('csv_bigram.csv', 'w', newline = '')
writer = csv.writer(writefile)

for key, count in csv_bigram.items():
    word1, word2 = key
    writer.writerow([word1, word2, count])

data = csv.reader(open('csv_bigram.csv'))
sortedlist = sorted(data, key=lambda x:int(x[2]),reverse=True)
with open('final_bigram.csv', 'w', newline = '') as f:
    fileWriter = csv.writer(f)
    for row in sortedlist:
        fileWriter.writerow(row)

fp1.close()
writefile.close()