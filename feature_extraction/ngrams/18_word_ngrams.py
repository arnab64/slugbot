import string, os
import csv
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords

 
class bigrams:				
	def __init__(self,infile,outfile):
		self.dx={}
		self.infile=infile
		self.outfile=outfile
		self.stop = set(stopwords.words('english'))

	def strip_punct(self):			#removes the functions
		exclude = set(string.punctuation)	 
		f = open(self.infile,'r',encoding='utf8')
		text = f.readlines()
		f.close()
		self.removed=[]
		for x in range(0,len(text)):
			s = text[x]
			s = s.replace('-',' ')
			s1 = ''.join(ch for ch in s if ch not in exclude)
			s1=s1.lower()
			self.removed.append(s1)

	def return_unigrams(self):		#extracts the bigrams from every line 
		for line in self.removed: 
			remd=[i for i in line.split() if i not in self.stop]		#removing the stopwords
			line2=" ".join(remd)
			token = nltk.word_tokenize(line2)
			
			unigrams = ngrams(token,1)
			for el in unigrams:	
				if self.dx.get(el,-1)==-1:
					self.dx[el]=1
				else:
					self.dx[el]+=1

	def return_bigrams(self):		#extracts the bigrams from every line 
		for line in self.removed: 
			remd=[i for i in line.split() if i not in self.stop]
			line2=" ".join(remd)
			token = nltk.word_tokenize(line2)
			
			bigrams = ngrams(token,2)
			for el in bigrams:
				#print("el=",el)	
				if self.dx.get(el,-1)==-1:
					self.dx[el]=1
				else:
					self.dx[el]+=1

	def sortit(self):				#extracts the 
		self.ofile=open(self.outfile,'w')
		self.lx=[]
		for key in self.dx.keys():
			self.lx.append((key,self.dx[key]))
		self.lx.sort(key=lambda tup: tup[1],reverse=True)
		lenx=len(self.lx)
		for itx in self.lx[:1000]:			#extract just the top 1000
			#print(itx)
			word1=itx[0][0]
			word2=itx[0][1]
			self.ofile.write(word1+'	'+word2+'	'+str(itx[1]/lenx*100)+'\n')

if __name__=="__main__":
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
	#lx=['Sheldon']
	#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
	for el in lx:
		print("\n..doing..",el)
		inf='character_data/just_'+el.lower()+'.txt'
		outf='intermediate/bigrams_'+el.lower()+'.txt'
		big=bigrams(inf,outf)
		big.strip_punct()
		big.return_bigrams()
		big.sortit()

