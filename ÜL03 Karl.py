# Karl Robert Masing
# 11.10.2022
# harjutus 3



#palindroom
x= input('sisesta palindroom:')

if x[::]==x[::-1]:

    print('on palindroom.')

else:

    print('ei ole palindroom.')





#tundide ajad
algus = "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":")
minutid1 = int(hh1)*60+int(mm1)
hh2,mm2 = lopp.split(":")
minutid2 = int(hh2)*60+int(mm2)

minutid = minutid2-minutid1 #ajavahe
hh= minutid//60 #täisarvuline jagamine
mm = minutid%60 #jääk

print(f"ajaline vahe on {hh}:{mm}")




#emaili kontroll
email=input("sisesta email kontrollimiseks; ")
print("@" in email)




#vandumine - teksti asendamine
v = input("Vannu siia 'kurat küll!': ")
print(v.lower().replace("kurat","*****"))




#korralik nimi
nimi = input("sisesta nimi: ")
puh_nimi = nimi.strip().capitalize()

print("tere,", puh_nimi+"!")