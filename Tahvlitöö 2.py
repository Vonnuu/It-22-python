#karl robert masing
import random

#õunad
m=int(input("mitu pöialpoissi tahab õunu?(1-7): "))
ü=0
for i in range(m):
    n=random.randint(1,2)
    print(n)
    ü+=n  
summa=14-ü
print(f"lumivalgeke saab endale {summa} ")
        
    

print("----------------------------------------")
#male

rt=int(input("sisesta täisarv: "))
tera=0.5
t=0
while t<rt:
    t+=1
    #x=t*(i+1)/2
    tera*=2
    
    
print(tera)
    





print("----------------------------------------")
#täringud

b=int(input("Sisesta mitu täringut: "))

for i in range(b):
    c=random.randint(1,6)
    print(c)
      
print("----------------------------------------")
#murelikud lapsevanemad
ringid=int(input("mitu ringi jooksid"))
ring=0
porgand=0
while ring < ringid:
    ring+=1
    if ring % 2==0:
        porgand+=ring
print(f"porgandite koguarv on:{porgand}")



print("----------------------------------------")
#äratus

a=int(input("Mitu Korda tahad äratada: "))

for i in range(a):
    print("Tõuse ja sära!")
    