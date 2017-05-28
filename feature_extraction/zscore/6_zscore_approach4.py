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
			#fname='data_central/_'+name+'.txt'
			finx = np.loadtxt(fname, delimiter=",")
			fin=finx[:,1:]
			mx=np.mean(fin,axis=0)
			sx=np.std(fin,axis=0)
			self.mean_vectors[name]=mx
			
			if k==0:
				self.data=fin
			else:
				self.data=np.concatenate((self.data,fin),axis=0)
			print(fin.shape,self.data.shape)
		self.mnx=np.mean(self.data,axis=0)
		self.sdx=np.std(self.data,axis=0)
		for name in names:
			self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])	

	def compute_mv_zdist(self):
		self.chardx={'Chandler':[],'Joey':[],'Rachel':[]}
		for k in range(len(self.names)):
			name=self.names[k]
			fname='data_central/train_test/train_'+name+'.txt'
			#fname='data_central/_'+name+'.txt'
			finx = np.loadtxt(fname, delimiter=",")
			fin=finx[:,1:]
			depth=fin.shape[0]
			width=fin.shape[1]	
			for j in range(depth):
				vecx=fin[j,:]
				self.chardx[name].append(self.zdistance(vecx))
		for key in self.chardx.keys():
			print(key,"mean/sd=",np.mean(self.chardx[key]),np.std(self.chardx[key]))

	def print_zscores(self):
		for name in self.names:
			gr=self.zvectors[name]	
			#print(gr)
			#print(len(gr))

	def compute_similarity_chars(self):
		lot=[]
		ofile=open("similarity_results.txt",'w')
		for j in range(len(self.names)):
			for k in range(j+1,len(self.names)):
				jname=self.names[j]
				kname=self.names[k]
				jzv=self.zvectors[jname]
				kzv=self.zvectors[kname]
				#scr=self.cosine(jzv,kzv)
				scr=1-spatial.distance.cosine(jzv,kzv)				#1 - distance = similarity
				scr2=self.euclidean(jzv,kzv)
				#print(jname,kname,scr,scr2)
				lot.append((jname,kname,scr,scr2))
		lot.sort(key=lambda tup: tup[2])
		for el in lot:
			print(el)
			ofile.write(el[0]+"-"+el[1]+"	"+str(el[2])+"	"+str(el[3])+"\n")
		#print(lot)

	def zdistance(self,vecx):
		subx=np.subtract(self.mnx,vecx)
		divx=np.absolute(subx)
		#mulx=np.multiply(divx,self.sdx)
		sumx=np.sum(divx)
		return sumx

	def compute_zvector(self,vecx):
		subx=np.subtract(self.mnx,vecx) 
		divx1=np.divide(subx,self.sdx)
		divx2=np.absolute(divx1)
		#floored=np.floor(divx2)
		return divx1

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
		fname='data_central/train_test/testing.txt'
		infile=open(fname)
		inlines=infile.readlines()
		correct=0
		#correctdx={'Monica':0,'Phoebe':0,'Ross':0,'Chandler':0,'Joey':0,'Rachel':0}
		correctdx={'Raj':0,'Leonard':0,'Sheldon':0,'Penny':0,'Bernadette':0,'Amy':0}

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
				correctdx[pred]+=1
				#print(pred)
		print("correct:",correct,"out of",k," / percent=",correct/(k+1)*100)		
		#print("Sheldon:",shelcount,"/ Penny:",pennycount," / Leonard:",leonardcount)	
		for key in correctdx.keys():
			print(key,correctdx[key])

#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
lx=['Chandler','Joey','Rachel']
#lx=['Sheldon','Penny']	#,'Leonard']
#lx=['Chandler','Joey','Rachel','Monica','Ross','Phoebe']		
#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
zzz=zscore(lx)
zzz.compute_mv_zdist()
#zzz.print_zscores()
#zzz.testitout()
