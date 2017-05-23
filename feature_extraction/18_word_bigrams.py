import string, os
import csv
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
 
class bigrams:
	def __init__(self,infile,outfile):
		self.dx={}
		self.infile=infile
		self.outfile=outfile

	def strip_punct(self):
		exclude = set(string.punctuation)	 
		f = open(self.infile,'r')
		text = f.readlines()
		f.close()
		self.removed=[]
		for x in range(0,len(text)):
			s = text[x]
			s = s.replace('-',' ')
			s1 = ''.join(ch for ch in s if ch not in exclude)
			self.removed.append(s1)

	def return_bigrams(self):
		for line in self.removed: 
			token = nltk.word_tokenize(line)
			bigrams = ngrams(token,2)
			for el in bigrams:	
				if self.dx.get(el,-1)==-1:
					self.dx[el]=1
				else:
					self.dx[el]+=1
		count=0
		for key in self.dx.keys():
			count+=1
			if count==10:
				break;

	def sortit(self):
		self.ofile=open(self.outfile,'w')
		self.lx=[]
		for key in self.dx.keys():
			self.lx.append((key,self.dx[key]))
		self.lx.sort(key=lambda tup: tup[1],reverse=True)
		for itx in self.lx[:25]:
			itxx=itx[0]
			self.ofile.write(itxx[0]+'	'+itxx[1]+'	'+str(itx[1])+'\n')

	def count_bigrams(self):
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

if __name__=="__main__":
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
	for el in lx:
		inf='character_data/justtwo_'+el.lower()+'.txt'
		outf='intermediate/cbigrams_'+el.lower()+'.txt'
		big=bigrams(inf,outf)
		big.strip_punct()
		big.return_bigrams()
		big.sortit()

