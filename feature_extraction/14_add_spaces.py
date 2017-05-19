import csv

class remspace:
    def __init__(self,infile,ofile,lenx):
        self.infile=infile
        self.ofile=open(ofile,'w')
        self.lenx=lenx

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
            #row=next(reader)                #skip the first row
            count=0
            for k in range(self.lenx):
                row=next(reader)
                if len(row)==0:
                    continue;
                else:
                    row=row[1:]
                    self.writeit(row)
                count+=1
            #drawProgressBar(count/13042)


lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
nos=[13052,11436,14138,13044,12958,14624]
for j in range(len(lx)):
    el=lx[j]
    print("Processing....",el)
    infname='intermediate/liwc_'+el.lower()+'.csv'
    outfname='data_central/liwc_'+el.lower()+'.txt'
    r=remspace(infname,outfname,nos[j])
    r.engine()