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
			tfname='friends/train_unigrams_'+self.cnames[j].lower()+'.txt'
			pf=open(tfname,'w')
			self.ofiles.append(pf)
		self.instx=instx
		self.train_ofile=open('friends/training_monica_rest.txt','w')
		self.test_ofile=open('friends/testing.txt','w')
		csvfile1=open('phoebe_rest.csv', 'w',newline='')
		self.csvfile=csv.writer(csvfile1,delimiter=',')

	def prinitit(self,separate=True):
		#self.train_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")
		#self.test_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")		
		if separate==False:
			for j in range(len(self.train)):
				#print(self.train[j])
				#print(self.train[j])
				#self.train_ofile.write(str(j+1)+','+self.train[j]+'\n')
				self.csvfile.writerow(self.train[j])
		else:
			for j in range(len(self.train)):
				spx=self.train[j].split(',')
				character=spx[-1]
				toprint=",".join(spx[:-1])
				indxxx=self.cnames.index(character)
				self.ofiles[indxxx].write(str(j+1)+','+toprint+'\n')
		for k in range(len(self.test)):
			self.test_ofile.write(str(k+1)+','+self.test[k]+'\n')	

	def processfiles(self):
		arrx=[]
		#cdict={'Chandler':1,'Rachel':2,'Joey':3}
		#cdict={'Sheldon':1,'Leonard':2,'Penny':3}
		#cdict={'Sheldon':1,'Penny':2,'Bernadette':3,'Amy':4,'Raj':5,'Leonard':6}
		#cdict={'Chandler':0,'Joey':1,'Rachel':2,'Ross':4,'Monica':5,'Phoebe':6}
		for j in range(len(self.cnames)):
			el=self.cnames[j]
			fname='../ngrams/ngramdata/unigram_vectors_'+el.lower()+'.txt'
			filex=open(fname,'r',encoding='utf8')
			flines=filex.readlines()
			labels=flines[0]
			labels=labels.split(',')
			if j==0:
				self.csvfile.writerow(labels)
				print("labels=",labels)
			flines=flines[1:]
			random.shuffle(flines)
			temp=[]
			for k in range(len(flines)):
				thisline=flines[k]
				q1=thisline[:-1]
				q2=q1[:-1]

				#print(q1)
				#print("q1=",q1)
				toadd=q1.split(",")
				if el!='Phoebe':
					el='Other'
				toadd.append(el.strip())
				'''
				if k<self.instx:
					self.test.append(toadd)
				else:
					self.train.append(toadd)'''
				if el=='Phoebe':
					self.train.append(toadd)
				else:
					#print("added",el)
					temp.append(toadd)
		print("length of train initially",len(self.train))
		print("length of temp",len(temp))
		
		#random.shuffle(self.train)
		#random.shuffle(self.test)
		#random.shuffle(temp)
		
		if len(self.train)>len(temp):
			self.train=self.train[:len(temp)]
			self.train.extend(temp)
		else:
			self.train.extend(temp[:len(self.train)])
		random.shuffle(self.train)
		print("Training:",len(self.train))
		print("Testing:",len(self.test))
		self.prinitit(separate=False)

listx=['Chandler','Joey','Rachel','Ross','Monica','Phoebe']
#listx=['Sheldon','Penny','Leonard',]
#listx=['Sheldon','Penny','Bernadette','Amy','Raj','Leonard']
tt = traintest(listx)
tt.processfiles()
