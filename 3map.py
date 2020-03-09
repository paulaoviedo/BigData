import sys
for line in sys.stdin:
    if not "Transaction" in line:
        valores=line.strip().split(",")
        print(valores[6]+"\t"+valores[1]+"\t1")
