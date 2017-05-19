import numpy as np

def extract_find(name):
	fname='data_central/train_test/train_'+name+'.txt'
	#fin=np.loadtxt(fname,'r')
	fin = np.loadtxt (fname, delimiter=",")
	mnx=np.mean(fin,axis=0)
	sdx=np.std(fin,axis=0)
	return mnx,sdx

#listx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
listx=['Chandler']
ofile_mean=open('data_central/mean_all.txt','w')
ofile_sd=open('data_central/sd_all.txt','w')

def test_accuracy(cname):				#performs the operation for the cname character
	ch_0,ch_1=extract_find(cname)		#ch_0 is mean, ch_1 is standard deviation
	ofname='data_central/z_'+cname+'.txt'
	ofile=open(ofname,'w')
	fin=open('data_central/testing_sec.txt','r')
	ofile=open('data_central/chandler_zscore_results.txt','w')			#outputfile
	flines=fin.readlines()
	results=[]
	for j in range(1,len(flines)):			#for all the lines
		itx=flines[j].split(',')
		lenx=len(itx)
		z_avg=0
		char=itx[-1]			#the 5th item in the list, is the character i.e. Chandler, Joey etc.
		charx=char[:-1]		#strip
		seq=""
		z_total=0
		for k in range(1,lenx-1):			#for each attribute
			lol=float(itx[k])				#get the float
			z_scr=(lol-ch_0[k-1])/ch_1[k-1]	
			if k!=lenx-2:
				seq+=','
				seq+=str(z_scr)
			else:
				seq+='\n'
			z_total+=z_scr
		print(seq)
		z_avg+=z_scr
		ofile.write(seq)
		tupx=(j,charx,abs(z_avg))
		#print(tupx)
		results.append(tupx)
	results.sort(key=lambda tup: tup[2])
	cx=0
	for p in range(1000):
		thix=results[p]
		if thix[1]==cname:
			thix=results[p]
			cx+=1
	print(cname,":	",cx,"out of 1000 extracted!\n")
	for el in results:
		#print(el)
		ofile.write(str(el)+'\n')

for el in listx:
	a,b=extract_find(el)
	print(el,"		",a,b)
	#ofile_mean.write(a)
	#ofile_mean.write()

'''
listy=['Chandler','Joey','Rachel']
for el in listy:
	#print(el)
	test_accuracy(el) 
'''