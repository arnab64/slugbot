import csv

class remspace:
    def __init__(self,infile,ofile):
        self.infile=infile
        self.ofile=open(ofile,'w')

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
            for k in range(13044):
                row=next(reader)
                if len(row)==0:
                    continue;
                else:
                    row=row[1:]
                    self.writeit(row)
                count+=1
            #drawProgressBar(count/13042)
r=remspace('data_central/liwc_chandler.csv','data_central/liwc_chandler.txt')
r.engine()