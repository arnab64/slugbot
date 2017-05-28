import csv

class remspace:
	def __init__(self,infile,ofile,lenx,keep,reject):
		self.infile=infile
		self.ofile=open(ofile,'w')
		self.lenx=lenx
		self.indexes={}
		self.reject=reject
		self.keep=keep
		self.keepreject=0			#default is reject, 1 is keep
		if len(self.reject)==0:
			self.keepreject=1
		elif len(self.keep)

	def write_csv(self,filename, rows, header_fields=None):
		with open(filename, 'w') as csvfile:
			writer = csv.writer(csvfile)
			if header_fields:
				writer.writerow(header_fields)
			for row in rows:
				writer.writerow(row)

	def writeit(self,elx):
		strx=""
		for el in elx:
			strx+=str(el)
			strx+=','
		strx=strx[:-1]
		self.ofile.write(strx+'\n')    

	def engine(self):
		with open(self.infile,"r") as f:
			reader = csv.reader(f)          #reading using CSV reader coz numpy doesn't read text 
			row=next(reader)                #skip the first row
			for j in range(len(row)):
				self.indexes[j]=row[j]
			for k in range(self.lenx):	#for every utterance extracted.
				row=next(reader)
				lenx=len(row)
				if lenx==0:
					continue;
				else:
					keeping=[]
					if self.keepreject==0:
						for l in range(lenx):
							if self.indexes[l] not in self.reject:
								keeping.append(row[l])
					else:
						for l in range(lenx):
							if self.indexes[l] in self.keep:
								keeping.append(row[l])
					#print(keeping)	
					opx=",".join(keeping)
					#print(opx)
					self.ofile.write(opx+'\n') 				





'''	                    else:
							if self.indexes[j] in self.keep:
								selected.append(row[i])
							else:
								continue;
					self.writeit(selected)
'''



#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#nos=[6138,5630,6748,6404,6416,7106]

#lx=['Chandler','Joey','Rachel','Monica','Ross','Phoebe']
#nos=[6405,6417,7107,6139,6750,5600]

lx=['Chandler']	#,'Joey','Rachel','Monica','Ross','Phoebe','Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
nos=[6405]	#,6417,7107,6139,6748,5631,4540,8206,13282,6442,5602,2110,2872]

#lx=['Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
#nos=[4540,8206,13282,6442,5602,2110,2872]


keep=['Adverbs','Articles','Swear Words','Question Marks','Impersonal Pronouns']
#reject=['Anger']
reject=[]

labelfile='data_central/liwc_labels.txt'
lofile=open(labelfile,'w')
lofile.write(",".join(keep))

for j in range(len(lx)):
	el=lx[j]
	print("Processing....",el)
	infname='intermediate/liwc_'+el.lower()+'.csv'
	outfname='data_central/liwc_'+el.lower()+'.txt'

	r=remspace(infname,outfname,nos[j],keep,reject)
	r.engine()