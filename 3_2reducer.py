import sys 
city=""
cont=0
price=0

for line in sys.stdin:
    if city == line.split("\t")[0]:
        if price> int(line.split("\t")[1]):
            price=int(line.split("\t")[1])
            print("entro")
    else:
        print(city+"\t"+ str(price))
        city=line.split("\t")[0]
        price=int(line.split("\t")[1])
        cont=1
