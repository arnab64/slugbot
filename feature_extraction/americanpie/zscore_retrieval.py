import numpy as np
import math
from scipy import spatial

class zscore:
	def __init__(self,names):
		self.names=names
		self.data=None
		self.mean_vectors={}
		self.sd_vectors={}
		self.median_vectors={}
		self.zvectors={}
		for k in range(len(names)):
			name=names[k]
			fname='../train_test/friends/train_'+name+'.txt'
			#fname='data_central/_'+name+'.txt'
			finx = np.loadtxt(fname, delimiter=",")
			fin=finx[:,1:]
			mx=np.mean(fin,axis=0)
			sx=np.std(fin,axis=0)
			medx=np.percentile(fin,50,axis=0)
			self.mean_vectors[name]=mx
			self.sd_vectors[name]=sx
			self.median_vectors[name]=medx
			if k==0:
				self.data=fin
			else:
				self.data=np.concatenate((self.data,fin),axis=0)
			#print(fin.shape,self.data.shape)
		self.mnx=np.mean(self.data,axis=0)
		self.sdx=np.std(self.data,axis=0)
		#print(self.mnx.shape,self.sdx.shape)
		for name in names:
			#self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])
			self.zvectors[name]=self.compute_zvector(self.mean_vectors[name])
		self.infileyy=open('americanpie.txt','r')
		self.utterances=self.infileyy.readlines()

	def compute_mv_zdist(self):
		self.chardx={'Chandler':[],'Joey':[],'Rachel':[]}
		for k in range(len(self.names)):
			name=self.names[k]
			fname='../train_test/friends/train_'+name+'.txt'
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
		print("length of self.mnx/vecx",len(self.mnx),len(vecx))
		subx=np.subtract(self.mnx,vecx) 			#difference from the mean
		divx1=np.divide(subx,self.sdx)				#divide by the standard deviation
		divx2=np.absolute(divx1)
		#floored=np.floor(divx2)
		return divx1

	def compute_zvector_individual(self,vec1,sdx1,vec2):
		subx=np.subtract(vec1,vec2) 
		divx1=np.divide(subx,sdx1)
		#divx2=np.absolute(divx1)
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

	def writeout_utterances(self,uno):
		line1=self.utterances[uno].strip()
		self.cfile.write(line1+'\n')

	def testitout_retrieval(self,characterx):
		#fname='../train_test/friends/testing.txt'
		fname='americanpie_liwc.txt'
		ofname2='results/zscore_retrieval.txt'
		cfilename='results/'+characterx+'_utterances_from_americanpie.txt'
		self.cfile=open(cfilename,'w')
		ofile2=open(ofname2,'a')
		infile=open(fname)
		self.characterinlines=infile.readlines()
		correct=0
		listx=[]
		for k in range(len(self.characterinlines)):	#len(inlines)):
			this1=self.characterinlines[k]
			this2=this1.split(',')
			#this3=this2[1:-1]
			#character=this2[-1].strip()				#actual character
			vect=[float(el) for el in this2]
			print(k,len(vect))
			zv=self.compute_zvector(vect)
			cosdistance1=self.euclidean(self.median_vectors[characterx],vect)			#distance from median vector
			cosdistance2=self.euclidean(self.zvectors[characterx],zv)	
			cosdistance3=self.euclidean(self.median_vectors[characterx],vect)			#
			listx.append((k,cosdistance3))
		listx.sort(key=lambda tup: tup[1])
		chand=0
		count=0
		for el in listx:
			unumx=el[0]
			self.writeout_utterances(unumx)

			#cfile.write(el)
			print(el)
			pred=el[0]
			if pred==characterx:
				chand+=1
			count+=1
			if count==1000:
				break;
		print(characterx,":",chand,"extracted out of 1000!",chand/1000*100,"percent!")
		ofile2.write(characterx+','+str(chand/10)+'\n')
		return(chand/1000)


	def testitout_classification(self):
		ofname1='results/zscore_classification.txt'
		ofile1=open(ofname1,'a')
		fname='../train_test/friends/testing.txt'
		infile=open(fname)
		inlines=infile.readlines()
		correct=0
		correctdx={'Rachel':0,'Monica':1,'Phoebe':2,'Ross':3,'Chandler':4,'Joey':5}
		#correctdx={'Chandler':0,'Joey':1}
		#correctdx={'Raj':0,'Leonard':0,'Sheldon':0,'Penny':0,'Bernadette':0,'Amy':0}

		for k in range(len(inlines)):	#len(inlines)):
			this1=inlines[k]
			this2=this1.split(',')
			this3=this2[1:-1]
			character=this2[-1].strip()
			vect=[float(el) for el in this3]
			zv=self.compute_zvector(vect)
			temparr1=[]
			temparr2=[]
			temparr3=[]
			for name in self.names:
				scr1=self.cosine(self.zvectors[name],zv)				#method2
				scr2=self.cosine(self.median_vectors[name],vect)	
				#scr3=self.cosine(self.mean_vectors[name],vect)		#this the best	
				scr3=self.euclidean(self.mean_vectors[name],vect)		#this the best			#method3
				#scr=self.euclidean(self.zvectors[name],vect)
				#scr=spatial.distance.cosine(self.zvectors[name],zv)
				temparr1.append((name,scr1))
				temparr2.append((name,scr2))
				temparr3.append((name,scr3))
			temparr1.sort(key=lambda tup: tup[1])
			temparr2.sort(key=lambda tup: tup[1])	
			temparr3.sort(key=lambda tup: tup[1])
			predicted=temparr3[0]
			pred=predicted[0]
			if pred==character:
				correct+=1
				correctdx[pred]+=1
		for key in correctdx.keys():
			print(key,":",correctdx[key],"extracted out of 1000!",correctdx[key]/10,"percent!")
			ofile1.write(key+','+str(correctdx[key]/10)+'\n')
		ofile1.write("\n")

#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#lx=['Rachel','Monica','Phoebe','Ross','Chandler','Joey']	
lx=['Chandler','Monica']	#,'Joey']	
#lx=['Raj','Leonard','Sheldon','Penny','Bernadette','Amy']
zzz=zscore(lx)
tscr=0
for el in lx:
	scr=zzz.testitout_retrieval(el)
	tscr+=scr
print("total score=",tscr)
print("----------------------------------------")
#zzz.compute_mv_zdist()
#zzz.print_zscores()
#zzz.testitout_classification()
