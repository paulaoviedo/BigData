import sys
for line in sys.stdin:
    if not "Transaction" in line:
        valores=line.strip().split(",")
        print(valores[2].split('-')[0]+"\t1")

