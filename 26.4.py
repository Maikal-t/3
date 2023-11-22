import json
with open("F5.txt", "r", encoding="utf-8") as file:
    final=[]
    profit={}
    average_profit={}
    avg = 0
    kol=0
    for line in file:
        l=line.split()
        pr=int(l[2]) - int(l[3])
        profit[l[0]] = pr
        if (pr>=0):
            avg += pr
            kol += 1
    avg = avg / kol
    average_profit["average_profit"]=avg
    final.append(profit)
    final.append(average_profit)
with open("Final.json", "w") as write_f:
    json.dump(final, write_f)