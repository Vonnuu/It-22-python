#karl robert masing

#kuupaev
def kuunimi(yt):
    kuud=[ "","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    return kuud[yt]

def kuupaev(ty):
    print(f"{w}.{ty}.{r}. a")

ewr=input("lisa kuupäev: ")
w,e,r=ewr.split(".")
kuupaev(kuunimi(int(e)))

#mündid
tri=[]
lop=input("sisesta faili nimi: ")
tre=open(lop)
for i in tre:
    tri.append(int(i.strip("\n"))) 
def mundids(r):
    for i in r:
        r[:]=[x for x in r if x<=5]
    print(f"Müntide summa on  {sum(r)}")
mundids(tri)

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