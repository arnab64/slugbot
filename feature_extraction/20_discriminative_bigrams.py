import numpy as np

class discriminative:
	def __init__(self):
		self.pool={}

	def extractbigrams(self,fname):
		inf=open(fname,'r')
		inl=inf.readlines()
		for line in inl:
			elx=line.split()
			if self.pool.get((elx[0],elx[1]),-1)==-1:
				self.pool[(elx[0],elx[1])]=[float(elx[2])]
			else:
				self.pool[(elx[0],elx[1])].append(float(elx[2]))

	def extractunigrams(self,fname):
		inf=open(fname,'r')
		inl=inf.readlines()
		for line in inl:
			elx=line.split()
			if self.pool.get(elx[0],-1)==-1:
				self.pool[elx[0]]=[float(elx[1])]
			else:
				self.pool[elx[0]].append(float(elx[1]))				

	def print_bigrams(self,top):
		bigs=[]
		ofile1=open('intermediate/tbbt_bigram_relative_frequencies.txt','w')
		ofile2=open('intermediate/tbbt_discriminative_bigrams.txt','w')
		for key in self.pool.keys():
			elllx=self.pool[key]
			ofile1.write(str(key)+"	"+str(np.std(elllx))+"	"+str(elllx)+"\n")
			#print(key,np.std(elllx))
			bigs.append((key,np.std(elllx)))
		bigs.sort(key=lambda tup: tup[1],reverse=True)
		print("numbers are:",len(bigs))
		count=0
		print("selecting the top 1000")
		for j in range(1000):	#len(bigs)):
			holx=bigs[j]
			bigr=holx[0]
			bigt=holx[1]
			if count<top:
				ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
			elif bigt==0:
				ofile2.write(bigr[0]+'	'+bigr[1]+'\n')
			count+=1

obj=discriminative()
lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
	inf='intermediate/cbigrams_'+el.lower()+'.txt'
	obj.extractbigrams(inf)
obj.print_bigrams(1000)