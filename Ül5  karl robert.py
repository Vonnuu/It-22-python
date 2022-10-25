# Karl Robert Masing
# 25.10.2022
# Harjutus 5



#õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in opilased:
    print(f"{jrk}. {i}")
    jrk+=1
a=int(input("mitmendat tahad muuta?"))
a-=1
num=input("milleks muudab?")
opilased.index(a)
opilased.insert(num)
print(opilased)

    
    
    
    


#Nimede Lisamine Loendisse

nimed=[]
for i in range(5):
    nimi=input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"viimati lisatud nimi: {nimed[-1]}")