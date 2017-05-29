import string, os
import csv
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords

 
class termfreq:				
	def __init__(self,infile,outfile):
		self.dx={}
		self.infile=infile
		self.outfile=outfile
		self.ofile=open(self.outfile,'w')
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
			for el in token:
				if self.dx.get(el,-1)!=-1:
					self.dx[el]+=1
				else:
					self.dx[el]=1
		for key in self.dx.keys():
			strx=key+"	"+str(self.dx[key])+'\n'	
			self.ofile.write(strx)	


class inversedocfreq:
	def __init__(self,names):
		self.names=names
		self.idfdx=[]
		for j in range(len(names)):
			dx={}
			name=names[j]
			fname='ngramdata/tf_'+name.lower()+'.txt'
			infile=open(fname,'r')
			inlines=infile.readlines()
			for k in range(len(inlines)):
				thisline=inlines[k]
				a,b=thisline.split()
				b=b.strip()
				dx[a]=int(b)
			self.idfdx.append(dx)
			print("read entire",fname)
		for k in range(6):
			print(len(self.idfdx[k].keys()))

	def tfidf(self):
		for j in range(1):
			name=self.names[j]
			fname='ngramdata/tf_'+name.lower()+'.txt'
			print("reading from",fname)
			infile=open(fname,'r')
			inlines=infile.readlines()
			for k in range(len(inlines)):		
				thisline=inlines[k]
				a,b=thisline.split()
				b=b.strip()
				count=0
				for l in range(len(self.names)):
					if self.idfdx[l].get(a,-1)!=-1:
						#print("got",a,"in",l,'with count',self.idfdx[l][a])
						count+=1
				print(a,b,count)


				
if __name__=="__main__":
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
	#lx=['Sheldon']
	#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
	for el in lx:
		print("\n..doing..",el)
		inf='../character_data/just_'+el.lower()+'.txt'
		outf='ngramdata/tf_'+el.lower()+'.txt'
		big=termfreq(inf,outf)
		big.strip_punct()
		big.return_unigrams()
	idf=inversedocfreq(lx)
	idf.tfidf()

