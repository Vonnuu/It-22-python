#Karl Robert Masing
#Palkade võrdlus - Loo palk.txt fail töötajate nime, soo ja palganumbriga (10 töötajat).
#Koosta programm, mis analüüsib kas firmas toimub diskrimineerimist soo järgi
#Selleks võrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kõige kõrgemat
#palka. Programm peab tegema otsuse. Programm ja txt mailile.file
def palgadok():
    ty=0
    y=0
    kl=0
    ml=0
    a=open("Palgad.txt")
    b=a.readlines()
    for line in b:
        e,p,s,pl=line.split(" ")
        if s=="m":
            y+=1
            kl+=int(pl)
    keskmineM=kl/y
    for line in b:
        e,p,s,pl=line.split(" ")
        if s=="n":
            ty+=1
            ml+=int(pl)
    keskmineN=ml/ty
    if keskmineM>keskmineN:
        print("Naisi ahistatakse")
    else:
        print("Mehi ahistatakse")
palgadok()
        