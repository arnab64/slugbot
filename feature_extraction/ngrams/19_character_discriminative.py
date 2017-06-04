import numpy as np

class characterwise:
	def __init__(self,names):
		self.names=names

	def extractit(self):
		for name in self.names:
			fname='ngramdata/unigrams_'+name.lower()+'.txt'
			ofile=open('ngramdata/friends_'+name.lower()+'_unigrams.txt','w')
			inf=open(fname,'r')
			inl=inf.readlines()
			lx=[]
			for j in range(101):	#len(inl)):
				line=inl[j]
				elx=line.split()
				lx.append(elx[0])
			finalstr=" ".join(lx)
			ofile.write(finalstr)

#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
cw=characterwise(lx)
cw.extractit()