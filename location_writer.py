import csv
from uszipcode import ZipcodeSearchEngine

## adds in latitude and longitude by zipcode

if __name__ == "__main__":
    search = ZipcodeSearchEngine()
    infile = open('clv_fixed.csv','r')
    outfile = open('clv_geo.csv','a')

    reader = csv.reader(infile, delimiter=',')
    writer=csv.writer(outfile, delimiter=',')
    i=0
    for row in infile:
        try:
            if i == 0:
                writer.writerow(row + ['latitude', 'longitude'])
                print(i)
                continue
            row = row.split(',')
            if len(str(int(row[-1]))) == 5:
                zipcode = str(int(row[-1]))
            else:
                zipcode = '0' + str(int(row[-1]))
            data = search.by_zipcode(zipcode)
            row.append(data['Latitude'])
            row.append(data['Longitude'])
            writer.writerow(row)
            i += 1
            print(i)
        except:
            print("Error at: {}".format(i))
            continue

    infile.close()
    outfile.close()