from tkinter import *


aken = Tk()
aken.title('ÜL5tinker')
aken.iconbitmap('favicon.ico')
aken.geometry("300x300")

#Oknupp
nupp0 = Button(aken, text="Ok", width=4, font="Tahoma 12")
nupp0.grid(row=7, column=1, padx=2, pady=2,sticky="e")

#pealkiri
tekst= Label(aken,text="Käibemaksukalkulaator", font="Tahoma 12", padx=4, pady=4)
tekst.grid(row=0, column=0, columnspan=4, sticky="w")

#joon
joon=Label(aken,text="_________________________________________",font="Tahoma 10",padx=2,pady=2)
joon.grid(row=4,column=0,columnspan=2)

#käibemaks
text=Label(aken, text="Käibemaks:", font="Tahoma 12", padx=4, pady=4)
text.grid(row=5,column=0, sticky="w")
text2=Label(aken, text="0.00€", font="Tahoma 12", padx=4, pady=4)
text2.grid(row=5, column=1)



#Hind käibemaksuga
text=Label(aken, text="Hind Käibemaksuga:", font="Tahoma 12", padx=4, pady=4)
text.grid(row=6,column=0,sticky="w")
text2=Label(aken, text="0.00€", font="Tahoma 12", padx=4, pady=4)
text2.grid(row=6, column=1)



#Määra valik
var = IntVar()
silt2=Label(aken, text="Käibemaksumäär: ",font="Tahoma 12", padx=4, pady=4)
silt2.grid(row=2,sticky="w")
valikukast1=Radiobutton(aken,text="9%", variable=var, value=1,font="Tahoma 12", padx=4, pady=4)
valikukast1.grid(row=2, column=1)
valikukast2=Radiobutton(aken,text="20%", variable=var, value=1,font="Tahoma 12", padx=4, pady=4)
valikukast2.grid(row=3, column=1)

#käibemaksuta hind
silt=Label(aken, text="Hind käibemaksuta: ",font="Tahoma 12", padx=4, pady=4)
silt.grid(row=1,sticky="w")

sisestus=Entry(aken)
sisestus.grid(row=1, column=1)

aken.mainloop()