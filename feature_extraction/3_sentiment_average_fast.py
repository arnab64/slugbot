import sys,os
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn

class sentiment:
	def __init__(self):
		self.infname='data_central/sentiment_cache.txt'
		infile=open(self.infname,'r')
		self.cache={}
		if infile:
			print("Loading sentiment cache .....")
			inlines=infile.readlines()
			lenx=len(inlines)
			countx=0
			for line in inlines:
				tupx=line.split()
				self.cache[tupx[0]]=(tupx[1:])
				countx+=1
				self.drawProgressBar(countx/lenx)
			print("\n")

	def makesense(self,word):
		if self.cache.get(word,-1)==-1:
			x1=wn.synsets(word)			#finding the similar wordnet synsets
			lenx=len(x1)
			pos1=0
			neg1=0
			sc=0
			res=[]
			
			if(lenx>3):
				lenx=3
			for i in range(lenx):		#loop to add the positive and negative scores for each synset
				x2=x1[i].name()		
				y1=swn.senti_synset(x2)
				try:
					pos2=y1.pos_score()
					neg2=y1.neg_score()
					sc=sc+1				
					pos1=pos1+pos2
					neg1=neg1+neg2

				except AttributeError:
					continue;
			if (sc!=0):
				positive=pos1/sc
				negative=neg1/sc
			else:	
				positive=0
				negative=0
			res.append(positive)
			res.append(negative)
			mytup=tuple(res)
			return mytup
		else:
			return self.cache[word]

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

	def makesense_sent(self,sentence):
		wordx=sentence.split()
		ofile=open(self.infname,'a',encoding='utf-16')
		tpos=0
		tneg=0
		#tlen=len(wordx)
		tlen=0
		for wrd in wordx:
			if self.cache.get(wrd,-1)==-1:
				rex=self.makesense(wrd)
				ofile.write(wrd+'	'+str(rex[0])+'	'+str(rex[1])+'\n')
			else:
				rex=self.cache[wrd]

			tpos+=float(rex[0])
			tneg+=float(rex[1])
			if tpos+tneg!=0:
				tlen+=1
		try:
			arx=[tpos/tlen,tneg/tlen]
		except:
			arx=[0,0]
		return arx

if __name__=='__main__':
	senti=sentiment()
	print(senti.makesense('bad'))
	print(senti.makesense_sent('i love the fact that you are so cute'))