import numpy as np
import random

class traintest:
	def __init__(self,cnames,instx=1000):
		self.train=[]
		self.test=[]
		self.cnames=cnames
		self.instx=instx
		self.train_ofile=open('data_central/training.txt','w')
		self.test_ofile=open('data_central/testing.txt','w')

	def prinitit(self):
		self.train_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")
		self.test_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")		
		for j in range(len(self.train)):
			self.train_ofile.write(str(j+1)+','+self.train[j]+'\n')
		for k in range(len(self.test)):
			self.test_ofile.write(str(k+1)+','+self.test[k]+'\n')

	def processfiles(self):
		arrx=[]
		cdict={'Chandler':1,'Rachel':2,'Joey':3}
		for el in self.cnames:
			fname='data_central/combined_'+el.lower()+'.txt'
			filex=open(fname,'r')
			flines=filex.readlines()
			for k in range(len(flines)):
				thisline=flines[k]
				toadd=thisline[:-1]+','+el			#str(cdict[el])
				if k<self.instx:
					self.test.append(toadd)
				else:
					self.train.append(toadd)
		random.shuffle(self.train)
		random.shuffle(self.test)
		print(len(self.train))
		print(len(self.test))
		self.prinitit()

listx=['Chandler','Joey','Rachel']
tt = traintest(listx)
tt.processfiles()


