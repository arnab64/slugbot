import numpy as np
import math
from scipy import spatial

class zscore:
	def __init__(self,names):
		self.names=names
		self.data=None
		self.mean_vectors={}
		self.zvectors={}
		for k in range(len(names)):
			name=names[k]
			#fname='data_central/test_train/bigbang/train_'+name.lower()+'.txt'
			fname='data_central/liwc_'+name.lower()+'.txt'
			fin = np.loadtxt(fname, delimiter=",")
			#fin=finx[:,:]
			mx=np.mean(fin,axis=0)
			sx=np.std(fin,axis=0)
			self.mean_vectors[name]=mx
			if k==0:
				self.data=fin
			else:
				self.data=np.concatenate((self.data,fin),axis=0)		
		self.mnx=np.mean(self.data,axis=0)
		self.sdx=np.std(self.data,axis=0)
		print(self.mnx)
		print(self.sdx)
		for name in names:
			self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])	
			print(self.zvectors[name])

	def print_zscores(self):
		zv1=self.zvectors['Chandler']
		for el in zv1:
			print(el)

	def compute_zvector(self,vecx):
		subx=np.subtract(self.mnx,vecx) 
		divx=np.divide(subx,self.sdx)
		divx=np.absolute(divx)
		return divx

	def euclidean(self,arr_1,arr_2):
		diffx=np.subtract(arr_1,arr_2)
		sqrd=np.multiply(diffx,diffx)
		sum_sqrd=np.sum(sqrd)
		distx=math.sqrt(sum_sqrd)
		return(distx)

	def cosine(self,arr_1,arr_2):	
		arr_12=np.multiply(arr_1,arr_2)
		arr_1s=np.multiply(arr_1,arr_1)
		arr_2s=np.multiply(arr_2,arr_2)
		lsum=np.sum(arr_1s)
		rsum=np.sum(arr_2s)
		usum=np.sum(arr_12)
		lsqrt=math.sqrt(lsum)
		rsqrt=math.sqrt(rsum)
		distx=usum/(lsqrt*rsqrt)
		return(1-distx)

	def measure_distances(self):
		ofile=open('distances_cosine.txt','w')
		self.distances=[]
		for j in range(len(self.names)):
			for k in range(j+1,len(self.names)):
				name1=self.names[j]
				name2=self.names[k]
				#distx=self.euclidean(self.zvectors[name1],self.zvectors[name2])
				#distx=self.cosine(self.zvectors[name1],self.zvectors[name2])
				distx=self.euclidean(self.zvectors[name1],self.zvectors[name2])
				self.distances.append((name1,name2,distx))
		self.distances.sort(key=lambda tup: tup[2])
		for el in self.distances:
			print(el)
			ofile.write(el[0]+' & '+el[1]+','+str(el[2])+'\n')

	def testitout(self,character):
		fname='data_central/test_train/testing.txt'
		infile=open(fname)
		inlines=infile.readlines()
		correct=0
		temparr=[]
		for k in range(5):	#len(inlines)):
			this1=inlines[k]
			this2=this1.split(',')
			this3=this2[1:-1]
			character=this2[-1].strip()
			vect=[float(el) for el in this3]
			#print(len(vect)
			zv=self.compute_zvector(vect)	
			#for el in zv:
			#	print(type(el))
			print(len(zv))
			scr=spatial.distance.cosine(self.zvectors[character],vect)
			temparr.append((name,scr))
		temparr.sort(key=lambda tup: tup[1])
		#print(temparr)

		#print("correct:",correct,"out of",k," / percent=",correct/(k+1)*100)		
		#print("Sheldon:",shelcount,"/ Penny:",pennycount," / Leonard:",leonardcount)	

#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#lx=['Chandler','Joey','Rachel','Monica']
#lx=['Sheldon','Penny','Leonard','Raj','Amy','Bernadette',
lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
zzz=zscore(lx)
#zzz.print_zscores()
zzz.measure_distances()
#zzz.testitout('Chandler')
