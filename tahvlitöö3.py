#karil robert masing
import re
import datetime
#tahvli juurde
t=input("Sisesta failinimi(txt): ")
u=open(t)
opilased=[]
for i in u:
    opilased.append(i)
aeg = datetime.datetime.now()


print(opilased[int(aeg.strftime("%d"))])



#jukebox
o=input("Sisesta Laul(txt) (jukebox.txt, 80ndad.txt, eesti_muusika.txt, edm.txt): ")
i=open(o)
jrk=1
for line in i:
    if re.search("", line):
        print(f"{jrk}.{line}",end="")
    jrk+=1
i.close()
p=int(input("\nsisesta laulu number: "))
y=open(o)
lugu=1
for line in y:
    if p==lugu:
        print("Mängitav muusikapala on: ", line)
    lugu+=1
    
print("--------------------------------")
#sissetulekud
k=open("konto.txt")
for line in k:
    if re.search("^[0-9]", line):
        print(line,end="")

print("--------------------------------")
#murelik lapsevanem 2
ringid=int(input("mitu ringi jooksid: "))
ring=0
porgand=0
for i in range(ringid):
    ring+=1
    if ring % 2==0:
        porgand+=ring
print(f"porgandite koguarv on:{porgand}")

print("--------------------------------")
#ülikooli

a=open("rebased.txt",encoding="UTF-8")
vastuvoetud=[]
aastad=[2011,2012,2013,2014,2015,2016,2017,2018,2019]
for rida in a:
    vastuvoetud.append(int(rida))
aasta=int(input("mis aastat soovite: "))
index=aastad.index(aasta)
print(vastuvoetud[index])

a.close()