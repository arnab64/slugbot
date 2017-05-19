import numpy as np



def extract_find(name):
	fname='data_central/combined_'+name.lower()+'.txt'
	#fin=np.loadtxt(fname,'r')
	fin = np.genfromtxt (fname, delimiter=",")
	mnx=np.mean(fin,axis=0)
	sdx=np.std(fin,axis=0)
	return mnx,sdx

listx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
ofile_mean=open('data_central/mean_all.txt','w')
ofile_sd=open('data_central/sd_all.txt','w')

'''
for el in listx:
	a,b=extract_find(el)
	print(el,"		",a,b)
	#ofile_mean.write(a)
	#ofile_mean.write()
'''

def test_accuracy(cname):
	ch_0,ch_1=extract_find(cname)		#ch_0 is mean, ch_1 is standard deviation

	fin=open('data_central/testing.txt','r')
	ofile=open('data_central/chandler_zscore_results.txt','w')
	flines=fin.readlines()
	results=[]
	for j in range(1,len(flines)):
		itx=flines[j].split(',')
		z_avg=0
		char=itx[5]
		charx=char[:-1]
		for k in range(1,5):
			lol=float(itx[k])
			z_scr=(lol-ch_0[k-1])/ch_1[k-1]
			z_avg+=z_scr
		tupx=(j,charx,abs(z_scr))
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
	print(el,"	",extract_find(el))
print("\n\n")
listy=['Chandler','Joey','Rachel']
for el in listy:
	#print(el)
	test_accuracy(el)