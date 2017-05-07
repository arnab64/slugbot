import nltk,sys

class more_preprocessing:
	def __init__(self):
		self.infile=open('Chandler_all.txt','r')
		self.inlines=self.infile.readlines()

	def remove_name(self,sentx):
		sx=sentx.split()
		rx=sx[2:]
		self.removd=" ".join(rx)
		return(self.removd)

	def remove_desc(self,sentx):
		comma=0
		resx=[]
		for chr in self.removd:
			if comma==0:
				if chr!='(':
					resx.append(chr)
				else:
					comma=1
			else:
				if chr==')':
					comma=0	
		return "".join(resx)

	def drawProgressBar(self,percent, barLen = 100):
	    sys.stdout.write("\r")
	    progress = ""
	    for i in range(barLen):
	        if i<int(barLen * percent):
	            progress += "="
	        else:
	            progress += " "
	    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
	    sys.stdout.flush()

	def justdoit(self):
		#for linex in self.inlines:
		ofile=open('just_chandler.txt','w')
		n=len(self.inlines)
		for k in range(n):
			linex=self.inlines[k]
			a=self.remove_name(linex)
			#print(a)
			b=self.remove_desc(a)
			ofile.write(b+'\n')
			frac=k/n
			#print(frac)
			self.drawProgressBar(frac)
			#print(b)		

prep=more_preprocessing()
prep.justdoit()