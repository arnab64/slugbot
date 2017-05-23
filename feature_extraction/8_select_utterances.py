def select(name,threshold):
	fname='character_data/just_'+name.lower()+'.txt'
	infile=open(fname,'r')
	inlines=infile.readlines()
	ofname='character_data/justtwo_'+name.lower()+'.txt'
	ofile=open(ofname,'w')
	sel=0
	for j in range(len(inlines)):
		if len(inlines[j].split())>threshold:
			sel+=1
			ofile.write(inlines[j])
	print(sel/(j+1),"percent selected!")

lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
	select(el,7)
