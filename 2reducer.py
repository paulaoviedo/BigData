import sys 
city=""
cont=0
price=0
pro=0
for line in sys.stdin:
    if city == line.split("\t")[0]:
       cont+=1
       price+=int(line.split("\t")[1])
    elif cont!=0:
       pro=price/cont
       print(city+"\t"+str(pro))
       city=line.split("\t")[0]
    else:
       city=line.split("\t")[0]
       cont=1
