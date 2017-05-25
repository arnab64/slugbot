import numpy as np
from nltk import pos_tag
from nltk import word_tokenize
import sys, os

class count_words:
	def __init__(self,infname,outfname):
		self.infile=open(infname,'r')
		self.inlines=self.infile.readlines()
		self.ofile=open(outfname,'w')

	def countit(self):
		for line in self.inlines:
			lenx=len(line.split())
			self.ofile.write(str(lenx)+'	'+str(lenx)+'\n')

lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
	print("\nProcessing",el,".....")
	infname='character_data/justtwo_'+el.lower()+'.txt'
	outfname='data_central/countwords_'+el.lower()+'.txt'
	vs=count_words(infname,outfname)
	vs.countit()
