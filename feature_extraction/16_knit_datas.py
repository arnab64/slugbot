import numpy as np

'''
This code knits various data files together!
'''

class knit:
	def __init__(self,fnames,delimited,transpose,ofilename):
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
			print("fnames=",fnames)
			for j in range(len(fnames)):
				spx=fnames[j].split('.')
				if delimited[j]==0:
					temp=np.loadtxt(fnames[j])	
				elif delimited[j]==1:
					temp=np.loadtxt(fnames[j],delimiter=',')
				if transpose[j]==1:
					temp=np.transpose(temp)
				arrx.append(temp)
			temp=arrx[0]
			print("Shapes are:")
			for el in arrx:
				print(el.shape)
			for k in range(1,len(arrx)):
				temp=np.concatenate((temp,arrx[k]),axis=1)
				print("shape is now",temp.shape)
			print(temp.shape)
			np.savetxt(ofilename, temp, delimiter=',',fmt='%7.6f')

#listx=['Monica','Phoebe','Ross',
listx=['Chandler','Joey','Rachel']
for el in listx:
	#f1='data_central/sentiment_scores_'+el.lower()+'.txt'
	#f2='data_central/verb_strength_'+el.lower()+'.txt'
	#f4='data_central/liwc_'+el.lower()+'.txt'
	f3='data_central/countwords_'+el.lower()+'.txt'
	#f4='data_central/tag_questions_'+el.lower()+'.txt'
	of='data_central/combined_'+el.lower()+'.txt'
	knx=knit([f1,f2,f3],[0,0,0,1],[0,0,0,0],of)
	
