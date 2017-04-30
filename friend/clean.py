import os,glob

outfile=open('clean_S01E01.txt','a')
outfile2=open('phoebe_all.txt','a')


def allfiles(foldername):			#returns the name of all files inside the source folder. 		
	owd = os.getcwd()
	fld = foldername + "/"
	os.chdir(fld)					#this is the name of the folder from which the file names are returned.
	arr = []						#empty array, the names of files are appended to this array, and returned.
	for file in glob.glob("*.txt"):
		arr.append(file)
	os.chdir(owd)
	return arr

def extract_chandler(fname):
	infile = open(fname,'r')
	intext = infile.read()
	textx=intext.split()

	bufferx=[]
	temp=None
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
				if temp=='Phoebe':
					outfile2.write("Phoebe : "+sntx+'\n')
				#outfile.write(temp+" : "+sntx+'\n')
			else:
				outfile.write(sntx+'\n')
			temp=temp2
			bufferx=[]

everyfile= allfiles('friends_scripts')
for ef in everyfile:
	print(ef)
	newfname="friends_scripts/"+ef
	extract_chandler(newfname)

