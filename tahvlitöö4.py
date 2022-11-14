#karl robert masing

#mündid
def mundid(qw):
    
    




#Tervitused motisklustega
def tervitus(s):
    for i in range(s):
        print("Tana",i+1,". kord tervitada, motiskleb voorustaja.")
        print("Kylaline: \"Tere, suur tanu kutse eest!\"")
        print("voorustaja: \"Tere!\"")
ew=int(input("Sisesta mitu korda tahad tervitada: "))
tervitus(ew)

print("------------------------------------------")
#Peo eelarve
def eelarve(kj):
    eelarve=10*kj+55
    return eelarve
y=int(input("osalejate arv: "))
t=int(input("kinnitatud osalejad: "))
print(eelarve(y),"€", "maksimaalne")
print(eelarve(t),"€", "minimaalne")

print("------------------------------------------")
#Ounamahla tegemine
def mahlapakk(o):
    m=round(o*0.4/3)
    return m
k=float(input("Sisesta õunad: "))
print(mahlapakk(k))
print("------------------------------------------")
#banner
def banner(a):
    a=a.upper()
    return a

n=input("Sisesta reklaam sona: ")
m=int(input("Mitu korda soovite reklaami kuvada?: "))
for i in range(m):
    print(n.upper())

print("------------------------------------------")

a="Osta ja sa ei kahetse"
print(a.upper())
banner(a)
