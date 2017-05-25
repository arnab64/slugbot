import csv

def countit(fname,format):
	if format=='txt':
		infile=open(fname,'r')
		inlines=infile.readlines()
		for line in inlines:
			print(len(line.split(',')))
	else:
		with open(fname,"r") as f:
			reader = csv.reader(f)          #reading using CSV reader coz numpy doesn't read text 
			row=next(reader)
			for j in range(2):
				print(len(row))


if __name__=='__main__':
	lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel','Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
	for el in lx:
		fname='liwc_'+el.lower()+'.csv'
		countit(fname,'csv')
