import nltk,sys

class partofspeech:
	def __init__(self):
		self.dx={}	

	def justpos(self,sent):			#extract the part of speech for each token
		text = nltk.word_tokenize(sent)
		pos_1 = nltk.pos_tag(text)
		pos_list=[]
		for el in pos_1:
			pos_list.append(el[1])
		#print(pos_list)
		return pos_list

	def getpos_bigrams(self,poslist):		#extract the pos bigrams
		posbgs=[]
		for j in range(len(poslist)-1):
			posbgs.append(poslist[j]+'-'+poslist[j+1])
		#print(posbgs)
		return posbgs

	def count_posbgs(self,posbglist):		#count the pos bigrams
		for el in posbglist:			#this function returns a dictionary
			if self.dx.get(el,-1)==-1:
				self.dx[el]=1
			else:
				self.dx[el]+=1
		return(self.dx)

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

	def sort_and_write(self,ofname):				#takes the POS bigrams and their counts, puts those in a list-of-list and sorts it and writes it to a file
		ofile=open(ofname,'w')
		lol=[]
		for el in self.dx.keys():
			lol.append((el,self.dx[el]))
		lol.sort(key=lambda tup: tup[1],reverse=True)
		for gx in lol:
			strx=gx[0]+"	"+str(gx[1])+"\n"
			ofile.write(strx)
			print(gx)

	def primary(self):								#main function
		infile = open('just_chandler.txt','r')
		inlines=infile.readlines()
		n=len(inlines)
		for k in range(n):			
			el=inlines[k]
			a=self.justpos(el)
			b=self.getpos_bigrams(a)
			self.count_posbgs(b)
			frac=k/n
			self.drawProgressBar(frac)
		self.sort_and_write('pos_bigrams.txt')

posx=partofspeech()
posx.primary()