import nltk,sys
import sentiment_average_fast as saf

class extract_sentiment:
	def __init__(self):
		self.dx={}	

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

	def primary(self,infname,outfname):								#main function
		infile = open(infname,'r')
		ofile = open(outfname,'w')
		inlines=infile.readlines()
		n=len(inlines)
		for k in range(n):			
			sentence=inlines[k]
			sentence2 = "".join(c for c in sentence if c not in ('!','.',':',',','?',';','``','&','-','"','(',')','[',']','0','1','2','3','4','5','6','7','8','9'))
			senti=saf.justsentiment(sentence2)			
			ofile.write(str(senti[0])+"	"+str(senti[1])+'\n')
			frac=k/n
			self.drawProgressBar(frac)

posx=extract_sentiment()
lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
	print("Processing",el,".....")
	infname='character_data/justtwo_'+el.lower()+'.txt'
	outfname='data_central/sentiment_scores_'+el.lower()+'.txt'
	posx.primary(infname,outfname)