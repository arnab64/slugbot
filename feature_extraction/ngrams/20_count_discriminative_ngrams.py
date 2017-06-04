import string, os, sys
import csv
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords
import codecs

 
class count_ngrams:				
	def __init__(self,infile,outfile,ngrams,pos):
		self.dx={}
		self.pos=pos
		self.infile=infile
		self.outfile=outfile
		self.stop = set(stopwords.words('english'))		
		self.discriminative_bigs={}
		self.dblist=[]
		if ngrams==2:
			if pos==0:
				inf=open('ngramdata/friends_discriminative_bigrams.txt',"r",encoding='utf-8',errors='ignore')
			else:
				inf=open('ngramdata/friends_pos_discriminative_bigrams.txt',"r",encoding='utf-8',errors='ignore')
		else:
			if pos==0:
				#inf=open('ngramdata/friends_discriminative_unigrams_third100.txt',"r",encoding='utf-8',errors='ignore')
				inf=open('ngramdata/friends_discriminative_unigrams_top100.txt',"r",encoding='utf-8',errors='ignore')
			else:
				inf=open('ngramdata/friends_pos_discriminative_unigrams.txt',"r",encoding='utf-8',errors='ignore')
		if pos==1:
			limitx=20
		else:
			limitx=100
		if ngrams==2:
			inl=inf.readlines()
			for j in range(limitx):						#for top 100 discrimative bigrams, 20 for POS bigrams
				line=inl[j]
				err=line.split()
				self.discriminative_bigs[(err[0],err[1].strip())]=j
				self.dblist.append(err[0]+'-'+err[1].strip())
		else:
			intext=inf.read()
			self.dblist=intext.split()
			for j in range(limitx):						#for top 100 discrimative bigrams
				self.discriminative_bigs[self.dblist[j]]=j
				

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

	def return_possent(self,sent):
		sent=nltk.word_tokenize(sent)
		postag=nltk.pos_tag(sent)
		justtags=[el[1] for el in postag]
		return " ".join(justtags)

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

	def count_bigrams(self):		#extracts the bigrams from every line 
		ofile=open(self.outfile,'w',encoding='utf8')
		strx=",".join(self.dblist)
		ofile.write(strx+'\n')
		lenx=len(self.removed)
		for i in range(lenx):
			line=self.removed[i] 
			remd=[i for i in line.split() if i not in self.stop]
			line2=" ".join(remd)
			vecx=[0]*100
			if self.pos==1:
				poxsent=self.return_possent(line2)
				token = nltk.word_tokenize(poxsent)
			else:
				token = nltk.word_tokenize(line2)
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

	def count_unigrams(self):		#extracts the bigrams from every line 
		ofile=open(self.outfile,'w',encoding='utf8')
		strx=",".join(self.dblist)
		ofile.write(strx+'\n')
		lenx=len(self.removed)
		for i in range(lenx):
			line=self.removed[i] 
			remd=[i for i in line.split() if i not in self.stop]
			line2=" ".join(remd)			
			if self.pos==1:
				vecx=[0]*20
			else:	
				vecx=[0]*100
			if self.pos==1:
				poxsent=self.return_possent(line2)
				token = nltk.word_tokenize(poxsent)
			else:
				token = nltk.word_tokenize(line2)
			for el in token:
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
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']

	#word bigrams
	print("\nword Bigram vectors!!")
	for el in lx:
		print("\nprocessing....",el)
		inf='../character_data/just_'+el.lower()+'.txt'
		outf='ngramdata/bigram_vectors_'+el.lower()+'.txt'
		big=count_ngrams(inf,outf,2,0)			
		big.strip_punct()
		big.count_bigrams()
	
	#lx=['Sheldon']	#,'Leonard','Penny','Bernadette','Amy','Raj']
	print("\nWord unigram vectors!!")
#word unigrams	
	for el in lx:
		print("\nprocessing....",el)
		inf='../character_data/just_'+el.lower()+'.txt'
		outf='ngramdata/unigram_vectors_'+el.lower()+'.txt'
		big=count_ngrams(inf,outf,1,0)			
		big.strip_punct()
		big.count_unigrams()

#pos unigrams
'''	print("\nPOS unigrams!")
	for el in lx:
		print("\nprocessing....",el)
		inf='character_data/just_'+el.lower()+'.txt'
		outf='data_central/tagged/pos_unigram_vectors_'+el.lower()+'.txt'
		big=count_ngrams(inf,outf,1,1)			
		big.strip_punct()
		big.count_unigrams()
#pos bigrams
	print("\nPOS bigrams!")
	for el in lx:
		print("\nprocessing....",el)
		inf='character_data/just_'+el.lower()+'.txt'
		outf='data_central/tagged/pos_bigram_vectors_'+el.lower()+'.txt'
		big=count_ngrams(inf,outf,2,1)			
		big.strip_punct()
		big.count_bigrams()'''
