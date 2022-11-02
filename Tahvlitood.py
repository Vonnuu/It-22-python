#karl robert masing
import math



#tervitus
print("Tere, maailm!")

#Aasta Liblikas

aasta=2020
liblikas="teelehe-mosaiikliblikas"
lause_keskosa=". aasta liblikas on "
lause=str(aasta)+lause_keskosa+liblikas
print(lause)

#pilved
b=6
a=int(input("Pilvede aluse kõrgused: "))
if a > b:
    print("ülemised pilved")
elif a < b:
    print("ei ole ülemised pilved")
    
    
#bussid

a=int(input("Kui palju inimesi läheb bussiga?: "))
b=int(input("bussides kohti?: "))
c=a/b
print(f"Busse on vaja {math.ceil(c)}")
v=a%b
if v==0:
    print(f"Viimases bussis on kohti{b}.")
else:
    print(f"Viimases bussis on inimesi {v}.")