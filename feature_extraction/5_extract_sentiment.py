import nltk,sys
import sentiment_average_fast as saf

class partofspeech:
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

	def primary(self):								#main function
		infile = open('character_data/just_chandler.txt','r')
		ofile = open('data_central/sentiment_scores.txt','w')
		inlines=infile.readlines()
		n=len(inlines)
		for k in range(n):			
			sentence=inlines[k]
			sentence2 = "".join(c for c in sentence if c not in ('!','.',':',',','?',';','``','&','-','"','(',')','[',']','0','1','2','3','4','5','6','7','8','9'))
			senti=saf.justsentiment(sentence2)			
			ofile.write(str(senti[0])+"	"+str(senti[1])+'\n')
			frac=k/n
			self.drawProgressBar(frac)

posx=partofspeech()
posx.primary()