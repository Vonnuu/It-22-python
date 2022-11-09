#karl robert masing
import re

a=open("rebased.txt",encoding="UTF-8")
vastuvoetud=[]
aastad=[2011,2012,2013,2014,2015,2016,2017,2018,2019]
for rida in a:
    vastuvoetud.append(int(rida))
aasta=int(input("mis aastat soovite: "))
index=aastad.index(aasta)
print(vastuvoetud[index])

a.close()