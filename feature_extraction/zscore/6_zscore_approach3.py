import numpy as np
import math
from scipy import spatial

class zscore:
	def __init__(self,names):
		self.names=names
		self.data=None
		self.mean_vectors={}
		self.zvectors={}
		self.znumbers={}
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

		#computes the average z vectors for all of the characters 
		for name in names:
			self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])	
			self.znumbers[name]=self.compute_znumber(self.mean_vectors[name])

	def print_zscores(self):
		for name in self.names:
			#print(self.zvectors[name])
			print(name,"znumber=",self.znumbers[name])

	def compute_zvector(self,vecx):
		subx=np.subtract(self.mnx,vecx) 
		divx=np.divide(subx,self.sdx)
		divx=np.absolute(divx)
		return divx

	def compute_znumber(self,vecx):
		zn=0
		subx=np.subtract(self.mnx,vecx)
		divx1=np.divide(subx,self.sdx)
		divx2=np.absolute(divx1)
		floored=np.floor(divx2)
		#return np.sum(floored)
		return floored

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

	def testitout(self):
		fname='data_central/train_test/tbbt_testing_sec.txt'
		infile=open(fname)
		inlines=infile.readlines()
		correct=0
		shelcount=0
		pennycount=0
		leonardcount=0
		for k in range(len(inlines)):	#len(inlines)):
			this1=inlines[k]
			this2=this1.split(',')
			this3=this2[1:-1]
			character=this2[-1].strip()
			vect=[float(el) for el in this3]
			zv=self.compute_zvector(vect)
			temparr=[]
			for name in self.names:
				#scr1=self.cosine(self.zvectors[name],vect)
				scr=spatial.distance.cosine(self.zvectors[name],vect)
				#print(scr1,scr)
				temparr.append((name,scr))
			temparr.sort(key=lambda tup: tup[1])
			#print(temparr)
			predicted=temparr[0]
			pred=predicted[0]
			#print(pred,character)
			if pred==character:
				correct+=1
				if pred=='Sheldon':
					shelcount+=1
				elif pred=='Penny':
					pennycount+=1
				elif pred=='Leonard':
					leonardcount+=1

				#print(pred)
		print("correct:",correct,"out of",k," / percent=",correct/(k+1)*100)		
		print("Sheldon:",shelcount,"/ Penny:",pennycount," / Leonard:",leonardcount)	
#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#lx=['Chandler','Joey','Rachel']
lx=['Sheldon','Penny','Leonard']
zzz=zscore(lx)
zzz.print_zscores()
zzz.testitout()
