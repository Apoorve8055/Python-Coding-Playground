import csv
data = ["1,2,3,4,5,6,7,8,9".split(',')]
file = "csvOutputfile.csv"

with open(file,"w") as f :
    writerfile = csv.writer(f,delimiter=',')
    for line in data:
        writerfile.writerow(line)
f.close()