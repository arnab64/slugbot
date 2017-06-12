import numpy as np
import random
import csv

class traintest:
	def __init__(self,cnames,instx=0):		
		self.train=[]
		self.test=[]
		self.cnames=cnames
		self.ofiles=[]
		for j in range(len(self.cnames)):
			tfname='friends/train_'+self.cnames[j].lower()+'.txt'
			pf=open(tfname,'w')
			self.ofiles.append(pf)
		self.instx=instx
		self.train_ofile=open('friends/training.txt','w')
		self.test_ofile=open('friends/testing.txt','w')
		csvfile1=open('chandler_rest.csv', 'w',newline='')
		self.csvfile=csv.writer(csvfile1,delimiter=',')

	def prinitit(self,separate=True):
		if separate==False:
			for j in range(len(self.train)):
				#self.train_ofile.write(str(j+1)+','+self.train[j]+'\n')
				self.csvfile.writerow(self.train[j])
		else:
			for j in range(len(self.train)):
				spx=self.train[j]		#.split(',')
				character=spx[-1]
				toprint=",".join(spx[:-1])
				indxxx=self.cnames.index(character)
				self.ofiles[indxxx].write(str(j+1)+','+toprint+'\n')
		for k in range(len(self.test)):
			topprint=",".join(self.test[k])
			self.test_ofile.write(str(k+1)+','+topprint+'\n')	

	def processfiles(self):
		arrx=[]
		#cdict={'Chandler':1,'Rachel':2,'Joey':3}
		#cdict={'Sheldon':1,'Leonard':2,'Penny':3}
		#cdict={'Sheldon':1,'Penny':2,'Bernadette':3,'Amy':4,'Raj':5,'Leonard':6}
		#cdict={'Chandler':0,'Joey':1,'Rachel':2,'Ross':4,'Monica':5,'Phoebe':6}
		for j in range(len(self.cnames)):
			el=self.cnames[j]
			#fname='../ngrams/ngramdata/unigram_vectors_tfidf_'+el.lower()+'.txt'
			#fname='../liwc/liwcfeatures/liwc_'+el.lower()+'.txt'
			#fname='../data_central/combined_new_'+el.lower()+'.txt'
			#fname='../liwc/liwcfeatures/liwc_'+el.lower()+'.txt'
			fname='../intermediate/liwc_'+el.lower()+'.csv'
			filex=open(fname,'r',encoding='utf8')
			flines=filex.readlines()
			#labels='../liwc/liwcfeatures/liwc_'+el.lower()+'.txt'
			#labels=labels.split(',')
			if j==0:
				print("not doing shit!")
				#self.csvfile.writerow(labels)
				#print("labels=",labels)
			flines=flines[1:]
			random.shuffle(flines)
			for k in range(len(flines)):
				thisline=flines[k]
				q1=thisline[:-1]
				q2=q1[:-1]
				#print("q1=",q1)
				toadd=q1.split(",")
				#if el!='Chandler':
				#	el='Other'
				toadd.append(el.strip())
				#q3=','.join(q1)
				#toadd=q1+','+el
				#toadd=thisline[:-1]+','+el			#str(cdict[el])
				if k<self.instx:
					self.test.append(toadd)
				else:
					self.train.append(toadd)
		random.shuffle(self.train)
		random.shuffle(self.test)
		print("Training:",len(self.train))
		print("Testing:",len(self.test))
		self.prinitit()

listx=['Chandler','Joey','Rachel','Ross','Monica','Phoebe']
#listx=['Sheldon','Penny','Leonard',]
#listx=['Sheldon','Penny','Bernadette','Amy','Raj','Leonard']
tt = traintest(listx)
tt.processfiles()
