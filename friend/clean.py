import os,glob

outfile=open('clean_S01E01.txt','a')



def preprocess(fname):
	ofname="processed/"+fname
	ofile=open(ofname,'w')
	infile = open(fname,'r')
	intext = infile.read()
	textx=intext.split(':')
	stry=" : ".join(textx)
	ofile.write(stry)


def allfiles(foldername):			#returns the name of all files inside the source folder. 		
	owd = os.getcwd()
	fld = foldername + "/"
	os.chdir(fld)					#this is the name of the folder from which the file names are returned.
	arr = []						#empty array, the names of files are appended to this array, and returned.
	for file in glob.glob("*.txt"):
		arr.append(file)
	os.chdir(owd)
	return arr

def extract_chandler(fname,cname):
	infile = open(fname,'r')
	intext = infile.read()
	textx=intext.split()
	ofname=cname+'_all.txt'
	outfile2=open(ofname,'a')

	bufferx=[]
	temp=None
	count=0
	for el in textx:
		if el !=':':
			bufferx.append(el)
		else:
			try:
				temp2=bufferx.pop()
			except:
				temp2=" "
			sntx=" ".join(bufferx)
			#print(temp,sntx)
			if temp:
				if temp==cname:
					outfile2.write(cname+" : "+sntx+'\n')
					count+=1
				#outfile.write(temp+" : "+sntx+'\n')
			else:
				outfile.write(sntx+'\n')
			temp=temp2
			bufferx=[]
	#print(count,"instances for",cname)
	return(count)


def justdoit(cname):
	everyfile= allfiles('processed/friends_scripts')
	countx=0
	for ef in everyfile:
		#print(ef)
		newfname="processed/friends_scripts/"+ef
		countx+=extract_chandler(newfname,cname)
		#preprocess(newfname)
	print(countx,"instances for",cname)

#preprocess("friends_scripts/S01E01.txt")
#extract_chandler("processed/friends_scripts/S01E01.txt")

lx=['Joey','Chandler','Phoebe','Rachel','Ross','Monica']
for el in lx:
	justdoit(el)