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
		self.discriminative_bigs={}
		self.dblist=[]
		inf=open('intermediate/discriminative_bigrams.txt','r')
		inl=inf.readlines()
		for j in range(len(inl)):
			line=inl[j]
			err=line.split()
			self.discriminative_bigs[(err[0],err[1].strip())]=j
			self.dblist.append(err[0]+'-'+err[1].strip())
		print(self.discriminative_bigs)
		print("....loaded discriminative bigrams....")

	def strip_punct(self):			#removes the functions
		exclude = set(string.punctuation)	 
		f = open(self.infile,'r')
		text = f.readlines()
		f.close()
		self.removed=[]
		for x in range(0,len(text)):
			s = text[x]
			s = s.replace('-',' ')
			s1 = ''.join(ch for ch in s if ch not in exclude)
			s1=s1.lower()
			self.removed.append(s1)

	def return_bigrams(self):		#extracts the bigrams from every line 
		ofile=open(self.outfile,'w')
		strx=",".join(self.dblist)
		ofile.write(strx+'\n')
		for line in self.removed: 
			vecx=[0]*37
			token = nltk.word_tokenize(line)
			bigrams = ngrams(token,2)
			for el in bigrams:
				if self.discriminative_bigs.get(el,-1)!=-1:
					indx=self.discriminative_bigs[el]
					vecx[indx]=1
				else:
					continue;
			vecxstr=[str(elx) for elx in vecx]
			finalx=",".join(vecxstr)
			ofile.write(finalx+'\n')	

if __name__=="__main__":
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
	for el in lx:
		inf='character_data/justtwo_'+el.lower()+'.txt'
		outf='data_central/posbvectors_'+el.lower()+'.txt'
		big=bigrams(inf,outf)
		big.strip_punct()
		big.return_bigrams()

