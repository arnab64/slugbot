import numpy as np
import sentiment_average_fast as saf
from nltk import pos_tag
from nltk import word_tokenize
import sys, os

class verb_strength:
	def __init__(self):
		self.infile=open('character_data/just_chandler.txt','r')
		self.inlines=self.infile.readlines()
		self.verblist=['VB','VBZ','VBD','VBN','VBP']
		self.saff=saf.sentiment()
		self.ofile=open('data_central/verb_strength_chandler.txt','w')

	def extract_verbs(self,text):
		txt1=word_tokenize(text)
		y=pos_tag(txt1)
		verbs_found=[]
		tpos,tneg=0,0
		count=0
		for el in y:
			if el[1] in self.verblist:
				word=el[0]
				verbs_found.append(word)
				p,q=self.saff.makesense(word)
				tpos+=float(p)
				tneg+=float(q)
				count+=1
		try:
			lpos=tpos/count
		except:
			lpos=0
		try:
			lneg=tneg/count
		except:
			lneg=0
		self.ofile.write(str(lpos)+"	"+str(lneg)+"\n")
		return verbs_found

	def perform_all(self):
		self.all_verbs=[]
		totalx=len(self.inlines)
		cntx=0
		print("\nExtracting verbs!! ......")
		for line in self.inlines:
			lx=self.extract_verbs(line)
			self.all_verbs.extend(lx)
			cntx+=1
			frax=cntx/totalx
			self.drawProgressBar(frax)

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

	def all_sentiment(self):
		self.perform_all()
		'''
		senti=saf.sentiment()
		pos_scr=0
		neg_scr=0
		count=0
		lenx=len(self.all_verbs)
		print("\nExtracting sentiment scores .....")
		for wordx in self.all_verbs:
			a,b=senti.makesense(wordx)
			pos_scr+=float(a)
			neg_scr+=float(b)
			count+=1
			frac=count/lenx
			self.drawProgressBar(frac)
		print("\nverb_strength_positive",pos_scr/count)
		print("\nverb_strength_negative",neg_scr/count)
		'''

vs=verb_strength()
vs.all_sentiment()