# Karl Robert Masing
# 11.10.2022
# harjutus 4












#juubel
sunna = input("sisesta synnipäev: ")
k1,p1,a1 = sunna.split(".")
aasta = 2022


vanus = aasta-int(a1)

#print(vanus)
if vanus%5==0:
    print("juubel")
else:
    print("ei ole juubel")
    



print
print("-----------------------------------------------")

#matemaatika
a = int(input("sisesta arv 1: "))
b = int(input("sisesta arv 2: "))
c = input("märk (* / + -): ")

if c=="*":
        vastus= a * b
elif c=="/":
    vastus = a/b
elif c=="+":
    vastus = a+b
elif c=="-":
    vastus = a-b



print(f"{a}{c}{b}={vastus}")
print("----------------------------------------------------")



#ruut
a = int(input("sistesta külg 1: "))
b = int(input("sistesta külg 2: "))

if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
else:
    print(f"{a} ja {b} moodustavad ristküliku")