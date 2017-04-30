infile = open('S01E01.txt','r')
intext = infile.read()

textx=intext.split()
#textx=textx[:250]
#print(textx[:100])

outfile=open('clean_S01E01.txt','a')

bufferx=[]
temp=None
for el in textx:
	if el !=':':
		bufferx.append(el)
	else:
		temp2=bufferx.pop()
		sntx=" ".join(bufferx)
		print(temp,sntx)
		if temp:
			outfile.write(temp+" : "+sntx+'\n')
		else:
			outfile.write(sntx+'\n')
		temp=temp2
		bufferx=[]
