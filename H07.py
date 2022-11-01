# Karl Robert Masing
# 25.10.2022
# Harjutus 7
import math

def kuup(a):
    print(f"kuubi ruumala on {a**3}")

def koonus(r,h):
    print(f"Koonuse ruumala on {(math.pi*r**2)*h/3}")

def kera(j):
    print(f"kera ruumala on {4/3*math.pi*(j**3)}")

def silinder(l,k):
    print(f"Silindri ruumala on {math.pi*(l**2)*k}")


print("************ LEIAME RUUMALA ***************")
loop = 1
while loop==1:
    print("Vali kujund : \n1.kuup \n2.koonus \n3.Kera \n4.Silinder")
    kujund = int(input("Lisa Kujundi Number 1-4: "))
    if kujund==1:
        x = int(input("Sisesta kuubi üks külg"))
        kuup(x)
    if kujund==2:
        r = int(input("Sisesta koonuse raadius"))
        h = int(input("Sisesta koonuse kõrgus"))
        koonus(r,h)
    if kujund==3:
        j = int(input("Sisesta kera raadius"))
        kera(j)
    if kujund==4:
        l=int(input("sisesta silindri raadius"))
        k=int(input("sisesta silindri kõrgus"))
        silinder(l,k)
    else:
        print("*******\nPalun tee valik 1-4\n*******")






#Tervita kasutajat ta nimega

#nimi=input("sisesta oma nimi")
#print("Tere", nimi)
def tervita(a="unknown", b="ge"):
    if b=="et":
        print(f"Tere {a}")
    elif b=="en":
        print(f"hi {a}")
    else:
        print(f"Hallo {a}")
tervita("karl")
