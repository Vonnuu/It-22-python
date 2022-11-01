# Karl Robert Masing
# 25.10.2022
# Harjutus 9
import datetime
import locale


#Tekita tänane kuupäev ning esita kujul 16. June 2016
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B. %Y"))


#Kuva eestistatud kuupäev kujul 16. juuni 2016
locale.setlocale(locale.LC_ALL, "et_EE")
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B. %Y"))

#Eralda ikukoodist sünnikuupäev ja leia isiku vanus
ik="50602020276"

sp=datetime.date(int("20"+ik[1:3]),int(ik[3:5]),int(ik[5:7]))
print(sp)
a="2022"
print(f"{int(20+ik[1:3])} - {a}") 