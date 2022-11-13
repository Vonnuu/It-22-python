#karl robert masing

#Tervitused motisklustega
r=int(input("sisesta kylaliste arv: "))
arv=0
for i in range(r):
    arv+=1
    print("Tana",arv,". kord tervitada, motiskleb voorustaja.")
    print("Kylaline: \"Tere, suur tanu kutse eest!\"")
    print("voorustaja: \"Tere!\"")


#Peo eelarve
y=int(input("osalejate arv: "))
t=int(input("kinnitatud osalejad: "))
eelarve=10*y
elarve=10*t
print(eelarve,"€", "maksimaalne")
print(elarve,"€", "minimaalne")




#Ounamahla tegemine
u=float(input("sisesta ounte kogus kilogrammides: "))
arvutus = round(u*0.4/3)
print(arvutus)

#banner
n=input("Sisesta reklaam sona: ")
m=int(input("Mitu korda soovite reklaami kuvada?: "))
for i in range(m):
    print(n.upper())

print("------------------------------------------")

a="Osta ja sa ei kahetse"
print(a.upper())
