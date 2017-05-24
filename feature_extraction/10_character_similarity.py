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
			fname='data_central/train_test/train_'+name+'.txt'
			finx = np.loadtxt(fname, delimiter=",")
			fin=finx[:,1:]
			mx=np.mean(fin,axis=0)
			sx=np.std(fin,axis=0)
			self.mean_vectors[name]=mx
			if k==0:
				self.data=fin
			else:
				self.data=np.concatenate((self.data,fin),axis=0)
				
		self.mnx=np.mean(self.data,axis=0)
		self.sdx=np.std(self.data,axis=0)
		for name in names:
			self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])	

	def print_zscores(self):
		for name in self.names:
			print(self.zvectors[name])

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

#lx=['Chandler','Joey','Rachel',
lx=['Sheldon','Penny','Leonard']
zzz=zscore(lx)
zzz.print_zscores()
zzz.testitout()
