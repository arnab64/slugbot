import numpy as np

'''
This code knits various data files together!
'''

class knit:
	def __init__(self,fnames,ofilename):
		'''
		if the data is delimited with commas, then put delimited=1
		if the data is just one column, then put transpose=1
		'''
		if len(fnames)==0:
			print("You need to have atleast one filename")
		elif len(fnames)==1:
			print("Just one file, nothing to knit!")
		else:
			arrx=[]
			#print("fnames=",fnames)
			for j in range(len(fnames)):
				temp=np.loadtxt(fnames[j],delimiter=',')
				arrx.append(temp)
			temp=arrx[0]
			#print("Shapes are:")
			#for el in arrx:
				#print(el.shape)
			for k in range(1,len(arrx)):
				temp=np.concatenate((temp,arrx[k]),axis=1)
				#print("shape is now",temp.shape)
			print(temp.shape)
			np.savetxt(ofilename, temp, delimiter=',',fmt='%7.6f')

#listx=['Monica','Phoebe','Ross',
listx=['Chandler','Joey','Rachel','Monica','Ross','Phoebe']
for el in listx:
	f1='data_central/sentiment_scores_'+el.lower()+'.txt'
	f2='data_central/verb_strength_'+el.lower()+'.txt'
	f3='data_central/liwc_'+el.lower()+'.txt'
	f4='data_central/unigram_vectors_'+el.lower()+'.txt'
	f5='data_central/bigram_vectors_new_'+el.lower()+'.txt'
	f6='data_central/pos_unigram_vectors_'+el.lower()+'.txt'
	f7='data_central/pos_bigram_vectors_'+el.lower()+'.txt'
	of='data_central/combined_new_'+el.lower()+'.txt'
	knx=knit([f1,f2,f3,f4,f5,f6,f7],of)
	
