import nltk,sys

class more_preprocessing:
	def __init__(self,infname,outfname):
		self.infile=open(infname,'r')
		self.ofile=open(outfname,'w')
		self.inlines=self.infile.readlines()

	def remove_name(self,sentx):
		sx=sentx.split()
		rx=sx[2:]
		removd=" ".join(rx)
		return(removd)

	def remove_desc(self,sentx):
		comma=0
		resx=[]
		for chr in sentx:
			if comma==0:
				if chr!='(':
					resx.append(chr)
				else:
					comma=1
			else:
				if chr==')':
					comma=0	
		return "".join(resx)

	def remove_desc_second(self,sentx):
		comma=0
		resx=[]
		for chr in sentx:
			if comma==0:
				if chr!='[':
					resx.append(chr)
				else:
					comma=1
			else:
				if chr==']':
					comma=0	
		return "".join(resx)		

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

	def justdoit(self):
		#ofile=open(self.outfile,'w')
		n=len(self.inlines)
		for k in range(n):
			linex=self.inlines[k]
			a=self.remove_name(linex)
			b=self.remove_desc(a)
			c=self.remove_desc_second(b)
			self.ofile.write(c+'\n')
			frac=k/n
			self.drawProgressBar(frac)

char_listx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in char_listx:
	print("\nprocessing ",el,'.....')
	infname='character_data/'+el+'_all.txt'
	outfname='character_data/just_'+el.lower()+'.txt'		
	prep=more_preprocessing(infname,outfname)
	prep.justdoit()