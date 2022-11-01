#P.Kiviorg
#25.10.2022
#Harjutus 6
fail=open("s6pru_l6ustaraamatus.txt","r")

sots = 0
kesk = 0
isamaa = 0
reform = 0
erakonnad = []

for i in fail.readlines():
    enimi,pnimi,erak,kyl = i.split()
    if erak == "SDE":
        sots+=1
    elif erak == "KE":
        kesk+=1
    elif erak == "IRL":
        isamaa+=1
    elif erak == "RE":
        reform+=1
    if erak not in erakonnad:
        erakonnad.append(erak)
    with open("nimed.txt","a") as nimedefail:
        nimedefail.write(f"{enimi} {pnimi}\n")

print(f"Erakondi kokku on {len(erakonnad)}")
print(f"Sotse on {sots}")
print(f"Kesikuid on {kesk}")
print(f"IRLikaid on {isamaa}")
print(f"Reformikaid on {reform}")


    

fail.close()