import numpy as np

'''
This code knits various data files together!
'''

class knit:
	def __init__(self,fnames,ofilename):
		if len(fnames)==0:
			print("You need to have atleast one filename")
		elif len(fnames)==1:
			print("Just one file, nothing to knit!")
		else:
			arrx=[]
			for j in range(len(fnames)):
				arrx.append(np.loadtxt(fnames[j]))
			temp=arrx[0]
			for k in range(1,len(arrx)):
				temp=np.concatenate((temp,arrx[k]),axis=1)
			print(temp.shape)
			np.savetxt(ofilename, temp, delimiter=',',fmt='%7.6f')

listx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']

for el in listx:
	f1='data_central/sentiment_scores_'+el.lower()+'.txt'
	f2='data_central/verb_strength_'+el.lower()+'.txt'
	of='data_central/combined_'+el.lower()+'.txt'
	knx=knit([f1,f2],of)
	
