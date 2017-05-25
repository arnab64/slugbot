import numpy as np

class discriminative:
	def __init__(self):
		self.pool={}
		self.pool2={}
		self.pool3={'Monica':[],'Phoebe':[],'Ross':[],'Chandler':[],'Joey':[],'Rachel':[]}

	def extractbigrams(self,name):
		fname='intermediate/bigrams_'+name.lower()+'.txt'
		inf=open(fname,'r')
		inl=inf.readlines()				#reading all bigrams for a character
		for line in inl:							
			elx=line.split()	
			#print("elx=",elx)	
			if self.pool.get((elx[0],elx[1]),-1)==-1:
				self.pool[(elx[0],elx[1])]=[float(elx[2])]
				#self.pool2[(elx[0],elx[1])]=[name]
			else:
				self.pool[(elx[0],elx[1])].append(float(elx[2]))
				#self.pool2[(elx[0],elx[1])].append(name)

	def extractunigrams(self,name):
		fname='intermediate/cunigrams_'+name.lower()+'.txt'
		inf=open(fname,'r')
		inl=inf.readlines()
		for line in inl:
			elx=line.split()
			if self.pool.get(elx[0],-1)==-1:
				self.pool[elx[0]]=[float(elx[1])]
			else:
				self.pool[elx[0]].append(float(elx[1]))				

	def print_unique_bigrams(self,top):
		bigs=[]
		ofile1=open('intermediate/friends_unigram_relative_frequencies.txt','w')
		ofile2=open('intermediate/friends_discriminative_unigrams_1.txt','w')
		ofile3=open('intermediate/friends_discriminative_unigrams_2.txt','w')
		for key in self.pool.keys():
			#print("key=",key)
			elllx=self.pool[key]
			if len(elllx)==1:
				charac1=self.pool2[key]
				character=charac1[0]
				self.pool3[character].append((key,elllx[0]))
			ofile1.write(str(key)+"	"+str(np.std(elllx))+"	"+str(elllx)+"\n")
			#print(key,np.std(elllx))
			bigs.append((key,np.std(elllx)))
		bigs.sort(key=lambda tup: tup[1],reverse=True)
		#print("numbers are:",len(bigs))
		count=0
		#print("selecting the top 1000")
		for j in range(len(bigs)):
			holx=bigs[j]
			#print(holx)
			bigr=holx[0]
			bigt=holx[1]
			#if count<top:
			#	ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
			if bigt==0:
				#print(holx)
				ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
				count+=1
		print(count,"unique bigrams extracted!")
		for key in self.pool3.keys():
			#print(key,"\n",self.pool3[key])
			ofilexxx=open("unique_"+key+".txt",'w')
			lolx=self.pool3[key]
			lolx.sort(key=lambda tup: tup[1])
			for j in range(100,200):
				alex=lolx[j]
				pang=alex[0]
				#print(alex)
				ofilexxx.write(pang[0]+"	"+pang[1]+'\n')

	def print_bigrams(self):
		bigs=[]
		ofile1=open('intermediate/friends_bigram_relative_frequencies.txt','w')
		ofile2=open('intermediate/friends_discriminative_bigrams_fourth.txt','w')
		for key in self.pool.keys():
			elllx=self.pool[key]
			ofile1.write(str(key)+"	"+str(np.std(elllx))+"	"+str(elllx)+"\n")
			bigs.append((key,np.std(elllx)))
		bigs.sort(key=lambda tup: tup[1],reverse=True)
		print("numbers are:",len(bigs))
		count=0
		print("selecting the top 100 discriminative!")
		for j in range(300,400):
			holx=bigs[j]
			bigr=holx[0]
			bigt=holx[1]
			#if count<top:
			ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
			#	count+=1
		'''		elif bigt==0:
				ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
				count+=1
		print(count,"unique bigrams extracted!")
		'''

	def print_unigrams(self,top):
		bigs=[]
		ofile1=open('intermediate/friends_unigram_relative_frequencies.txt','w')
		ofile2=open('intermediate/friends_discriminative_unigrams.txt','w')
		for key in self.pool.keys():
			elllx=self.pool[key]
			ofile1.write(str(key)+"	"+str(np.std(elllx))+"	"+str(elllx)+"\n")
			bigs.append((key,np.std(elllx)))
		bigs.sort(key=lambda tup: tup[1],reverse=True)
		#print("numbers are:",len(bigs))
		print("selecting the top 100")
		for j in range(top):
			wordx=bigs[j][0]
			ofile2.write(wordx+' ')
		

obj=discriminative()
#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
	obj.extractbigrams(el)
obj.print_bigrams()