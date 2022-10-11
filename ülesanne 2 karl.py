# Karl Robert Masing
# 11.10.2022
# ülesanne 2
import math



#Kütusekulu
a = int(input("sisesta tangitud kütus: "))
b= int(input("sisesta läbitud kilomeetrid: "))
print("vastus", a/(b/100))





#arvusüsteem
a = int(input("sisesta täisarv: "))
print("2ndsysteemis:", bin(a))
print("16ndsysteemis:", hex(a))







#ajateisendus
aeg = int(input("Sisesta minutid: "))
tunnid = aeg//60 #täisarvuline jagamine
minutid = aeg%60 #jääk
print("Vastus:",minutid,"M",";",tunnid,"H")








#hüpotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2) + b**2),2)
print("Kolmnurga hüpotenuus on:",c)








#rulluisutajad
#11.96
kiirus = 29.9
aeg = 24
vastus = round(kiirus/60*aeg,2)
print("Sportlane jõuab",vastus,"km")







#pitsa
#4,73

hind = 12.90
tip = 0.1
kogus = 3
summa = (hind+hind*tip)/kogus
print("iga tüüp maksab",summa,"eurot")







#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus,"toote summa on",summa,"eurot")




#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a+b+c
print("kolmnurga ümbermõõt on: ", p)