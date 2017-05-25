infile=open('liwc_rachel.txt','r')
inlines=infile.readlines()
for line in inlines:
	print(len(line.split(',')))