import csv

ofile=open('wospaces.txt','w')


def write_csv(filename, rows, header_fields=None):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        if header_fields:
            writer.writerow(header_fields)
        for row in rows:
            writer.writerow(row)

def writeit(elx):
    strx=""
    for el in elx:
        strx+=str(el)
        strx+=','
    strx=strx[:-1]
    ofile.write(strx+'\n')    

def engine():
    with open("chandler_output.csv","r") as f:
        reader = csv.reader(f)          #reading using CSV reader coz numpy doesn't read text 
        #row=next(reader)                #skip the first row
        count=0
        for k in range(13042):
            row=next(reader)
            if len(row)==0:
                continue;
            else:
                row=row[1:]
                writeit(row)
            count+=1
            #drawProgressBar(count/13042)

engine()