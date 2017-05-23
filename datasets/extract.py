import os,sys,glob

class extract:
	def __init__(self,chars):
		self.dx={'Raj':[],'Leonard':[],'Sheldon':[],'Penny':[],'Howard':[],'Bernadette':[],'Amy':[]}
		self.chars=chars

	def allfiles(self,foldername):			#returns the name of all files inside the source folder. 		
		owd = os.getcwd()
		fld = foldername + "/"
		os.chdir(fld)					#this is the name of the folder from which the file names are returned.
		arr = []						#empty array, the names of files are appended to this array, and returned.
		for file in glob.glob("*.txt"):
			arr.append(file)
		os.chdir(owd)
		return arr

	def extract(self,fname,mincount):
		inf=open(fname,'r',encoding="utf8")
		inlines=inf.readlines()
		for line in inlines:
			elems0=line.split()
			if len(elems0)>0:
				elems1=elems0[0]
				elems2=elems1[:-1]					#character name
				if len(elems0[1:])>mincount:
					utterance=' '.join(elems0[1:])
					if elems2 not in self.chars:
						continue;
					else:
						self.dx[elems2].append(utterance)

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

	def processall(self):
		allfile=self.allfiles("tbbt")
		totalfiles=len(allfile)
		for j in range(totalfiles):
			thisfile=allfile[j]	
			fname='tbbt/'+thisfile	
			self.extract(fname,7)
			self.drawProgressBar((j+1)/totalfiles)

	def printall(self):
		for key in self.dx.keys():
			lx=self.dx[key]
			ofname='extracted_'+key.lower()+'.txt'
			ofile=open(ofname,'w',encoding="utf8")
			for line in lx:
				ofile.write(line+'\n')

characters=['Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
ex=extract(characters)
ex.processall()
ex.printall()
