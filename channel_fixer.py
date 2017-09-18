import csv



 if __name__ == "__main__":
    marketing_ids = []
    infile = open('clv_labeled.csv','r')
    j=0
    for row in infile:
        row = row.split(',')
        if j=0:
            j += 1
            continue
        marketing_ids.append(row[5])
    infile.close()
    infile = open('clv_labeled.csv','r')
    print(len(marketing_ids))
    marketing_ids = set(marketing_ids)
    print(len(marketing_ids))
    outfile = open('clv_newchannel.csv','w')

    reader = csv.reader(infile, delimiter=',')
    writer=csv.writer(outfile, delimiter=',')
    i=0
    for row in reader:
        try:
            if i == 0:
                writer.writerow(row[1:])
                i += 1
                continue
            
            #writer.writerow(row)
            i += 1
            print(i)
        except:
            print("Error at: {}".format(i))
            continue

    infile.close()
    outfile.close()