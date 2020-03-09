import sys
city=""

for line in sys.stdin:
    if city != line.split("\t")[0]:
       print(line.split("\t")[0]+"\t"+ line.split("\t")[1])
       city=line.split("\t")[0]


