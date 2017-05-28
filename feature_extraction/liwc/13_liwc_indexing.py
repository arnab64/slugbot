import csv

class remspace:
	def __init__(self,infile,ofile,lenx,selected):
		self.infile=infile
		self.ofile=open(ofile,'w')
		self.lenx=lenx
		self.order={}
		self.finallength=len(selected)							#indexes = 
		for j in range(len(selected)):
			self.order[selected[j]]=j 
		#print(self.order)			

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
			onlyindexes=[]
			onlylabels=[]
			for j in range(len(row)):
				if self.order.get(row[j],-1)!=-1:
					onlyindexes.append(j)
					onlylabels.append(row[j])
			#print("indexes selected=",onlyindexes)
			#print("labels selected=",onlylabels)

			for k in range(self.lenx):	#for every utterance extracted.
				row=next(reader)
				lenrow=len(row)
				if lenrow==0:
					continue;
				else:
					finallist=[None]*self.finallength
					for j in range(len(onlyindexes)):
						indexnow=onlyindexes[j]
						#print("indexnow=",indexnow)
						featvalue=row[indexnow]
						#print("featvalue=",featvalue)
						featname=onlylabels[j]
						#print("featname=",featname)
						featindex=self.order[featname]
						#print("real index=",featindex)
						finallist[featindex]=row[j]
						#print("\n")
					finalstr=",".join(finallist)
					self.ofile.write(finalstr+'\n')

class getindexes:
	def __init__(self,names,keep,reject):
		self.names=names
		self.finalfeats=[]
		self.keep=keep
		self.reject=reject

	def getallfeatures(self,keepreject):
		for j in range(len(self.names)):
			name=self.names[j]
			infile='../intermediate/liwc_'+name.lower()+'.csv'
			with open(infile,"r") as f:
				reader = csv.reader(f)          #reading using CSV reader coz numpy doesn't read text 
				row=next(reader)	
				if j==0:
					self.finalfeats=row[:]
				else:
					self.finalfeats=[el for el in self.finalfeats if el in row]
		if keepreject==0:
			common=[el for el in self.finalfeats if el not in self.reject]		
		else:
			common=[el for el in self.finalfeats if el in self.keep]
		return common

#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#nos=[6138,5630,6748,6404,6416,7106]

#lx=['Chandler','Joey','Rachel','Monica','Ross','Phoebe']
#nos=[6405,6417,7107,6139,6750,5600]


#lx=['Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
#nos=[4540,8206,13282,6442,5602,2110,2872]

if __name__=='__main__':
	lx=['Chandler','Joey','Rachel','Monica','Ross','Phoebe','Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
	nos=[6405,6417,7107,6139,6748,5631,4540,8206,13282,6442,5602,2110,2872]


	#keep=['Adverbs','Articles','Swear Words','Question Marks','Impersonal Pronouns']
	keep=['Unique Words','Word Count','Words Per Sentence']
	#reject=['Anger']
	reject=[]

	labelfile='../data_central/liwc_labels.txt'
	lofile=open(labelfile,'w')
	lofile.write(",".join(keep))

	getx=getindexes(lx,keep,reject)
	featx=getx.getallfeatures(0)				#only select the attributes present in keep 
	print("featx=",featx)

	for j in range(len(lx)):
		el=lx[j]
		print("Processing....",el)
		infname='../intermediate/liwc_'+el.lower()+'.csv'
		outfname='../data_central/liwc_'+el.lower()+'.txt'

		r=remspace(infname,outfname,nos[j],featx)			#instance of classs
		r.engine()
