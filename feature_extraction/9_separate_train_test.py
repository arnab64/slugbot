import numpy as np
import random

class traintest:
	def __init__(self,cnames,instx=1000):
		self.train=[]
		self.test=[]
		self.cnames=cnames
		self.ofiles=[]
		for j in range(len(self.cnames)):
			tfname='data_central/train_test/train_'+self.cnames[j].lower()+'.txt'
			pf=open(tfname,'w')
			self.ofiles.append(pf)
		self.instx=instx
		self.train_ofile=open('data_central/train_test/training.txt','w')
		self.test_ofile=open('data_central/train_test/testing.txt','w')

	def prinitit(self,separate=True):
		#self.train_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")
		#self.test_ofile.write("ID,pos_sentiment,neg_sentiment,pos_verb,neg_verb\n")		
		if separate==False:
			for j in range(len(self.train)):
				self.train_ofile.write(str(j+1)+','+self.train[j]+'\n')
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
		cdict={'Sheldon':1,'Leonard':2,'Penny':3}
		for el in self.cnames:
			fname='data_central/liwc_'+el.lower()+'.txt'
			filex=open(fname,'r')
			flines=filex.readlines()
			flines=flines[1:]
			random.shuffle(flines)
			for k in range(len(flines)):
				thisline=flines[k]
				q1=thisline[:-1]	
				#q3=','.join(q1)
				toadd=q1+','+el
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
#listx=['Sheldon','Penny','Leonard']
tt = traintest(listx)
tt.processfiles()


