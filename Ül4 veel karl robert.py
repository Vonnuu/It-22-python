# Karl Robert Masing
# 11.10.2022
# harjutus 4
import random

#ruutude ja kuupide tabel











#pank

konto=10000
intress=0.05
periood=5

for i in range(1,periood+1):
    print(f"{i} {konto} {round(konto*intress,2)} {round(konto+konto*intress,2)}")
    konto=konto+konto*intress
print(f"Konto seis: {round(konto,2)}")
print(f"kasum: {round(konto-10000,2)}")




print("-----------------------------------------------")
#arvamismäng
loop=1
skoor=0
while loop==1:
    a=random.randint(1,11)
    for i in range(3):
        valik=int(input("vali arv 1-10: "))
        if valik==a:
            print("võitja")
            punktid+=1
            break
        else:
            print("kaotasid")
    loop = int(input("Tahad veel mängida (1/0?) "))
print("game over")
print(f"punktid {skoor}")                  







print("-----------------------------------------------")

#viisikud
for i in range(1,101):
    if i%5==0:
        print(i)
        






print("-----------------------------------------------")
#pisike korrutustabel
arv = 5
for i in range(1,11):
    summa = arv * i
    print(f"{arv}X{i}={summa}")
    




print("-----------------------------------------------")
#paaris paaritu
for i in range(1,11):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")





#loto
for i in range(5):
    suv = random.randint(0,9)
    print(suv, end=" ")







print("-----------------------------------------------")
#tsükkel

arv = 5
for i in range(5):
    print("* " * arv)
    arv -=1


arv=1
for i in range(5):
    print("* "* arv)
    arv = arv+1



nr = 5
for i in range(nr):
    print("* " * nr)






print("-----------------------------------------------")
#Jalgpalli meeskond
Vanus = 17
sugu = "m"

if Vanus>=16 and Vanus<=18 and sugu=="m":
    print("sobib meeskonda")
else:
    print("ei sobi")


print("-----------------------------------------------")
#Müük
hind = 20
if hind<=10:
    ale = 0.1
else:
    ale=0.2
summa=hind-hind*ale
print(f"Summa: {summa}€")





print("-----------------------------------------------")
#juubel
sunna = input("sisesta synnipäev: ")
k1,p1,a1 = sunna.split(".")
aasta = 2022


vanus = aasta-int(a1)

#print(vanus)
if vanus%5==0:
    print("juubel")
else:
    print("ei ole juubel")
    



print
print("-----------------------------------------------")

#matemaatika
a = int(input("sisesta arv 1: "))
b = int(input("sisesta arv 2: "))
c = input("märk (* / + -): ")

if c=="*":
        vastus= a * b
elif c=="/":
    vastus = a/b
elif c=="+":
    vastus = a+b
elif c=="-":
    vastus = a-b



print(f"{a}{c}{b}={vastus}")
print("----------------------------------------------------")



#ruut
a = int(input("sistesta külg 1: "))
b = int(input("sistesta külg 2: "))

if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
else:
    print(f"{a} ja {b} moodustavad ristküliku")