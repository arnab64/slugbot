import string, os, sys
import csv
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
import codecs

 
class bigrams:				
	def __init__(self,infile,outfile):
		self.dx={}
		self.infile=infile
		self.outfile=outfile
		self.discriminative_bigs={}
		self.dblist=[]
		inf=open('intermediate/tbbt_discriminative_bigrams.txt',"r",encoding='utf-8',errors='ignore')
		#inf=open(file_name, "r",encoding='utf-8', errors='ignore')
		inl=inf.readlines()
		for j in range(len(inl)):
			line=inl[j]
			err=line.split()
			self.discriminative_bigs[(err[0],err[1].strip())]=j
			self.dblist.append(err[0]+'-'+err[1].strip())
		#print(self.discriminative_bigs)
		#print("....loaded discriminative bigrams....")

	def strip_punct(self):			#removes the functions
		exclude = set(string.punctuation)	 
		f = open(self.infile,'r',encoding='utf-8',errors='ignore')
		text = f.readlines()
		f.close()
		self.removed=[]
		for x in range(0,len(text)):
			s = text[x]
			s = s.replace('-',' ')
			s1 = ''.join(ch for ch in s if ch not in exclude)
			s1=s1.lower()
			self.removed.append(s1)

	def drawProgressBar(self,percent, barLen = 50):			#just a progress bar so that you dont lose patience
	    sys.stdout.write("\r")
	    progress = ""
	    for i in range(barLen):
	        if i<int(barLen * percent):
	            progress += "="
	        else:
	            progress += " "
	    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
	    sys.stdout.flush()

	def return_bigrams(self,posbgs=False):		#extracts the bigrams from every line 
		ofile=open(self.outfile,'w',encoding='utf8')
		strx=",".join(self.dblist)
		#ofile.write(strx+'\n')
		lenx=len(self.removed)
		for i in range(lenx):
			line=self.removed[i] 
			if posbgs==True:
				vecx=[0]*18
			else:
				vecx=[0]*37
			token = nltk.word_tokenize(line)
			if posbgs==True:
				pos_1 = nltk.pos_tag(token)
				pos_list=[]
				for element in pos_1:
					pos_list.append(element[1])
				bigrams=ngrams(pos_list,2)
			else:
				bigrams=ngrams(token,2)
			for el in bigrams:
				if self.discriminative_bigs.get(el,-1)!=-1:
					indx=self.discriminative_bigs[el]
					vecx[indx]=1
				else:
					continue;
			vecxstr=[str(elx) for elx in vecx]
			finalx=",".join(vecxstr)
			ofile.write(finalx+'\n')
			self.drawProgressBar(i/lenx)	

if __name__=="__main__":
	#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
	lx=['Sheldon','Leonard','Penny','Bernadette','Amy','Raj']
	for el in lx:
		print("\nprocessing....",el)
		inf='character_data/just_'+el.lower()+'.txt'
		outf='data_central/posb_vectors_'+el.lower()+'.txt'
		big=bigrams(inf,outf)
		big.strip_punct()
		big.return_bigrams(posbgs=True)

