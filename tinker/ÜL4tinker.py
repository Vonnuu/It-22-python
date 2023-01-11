from tkinter import *

#akna seaded
aken = Tk()
aken.title('Tkinter "ÜL3"')
aken.iconbitmap('favicon.ico')
aken.resizable(0,0)
aken.geometry("200x200")


tekst= Label(aken,text="Siia tuleb vastus kunagi", font="Tahoma 12", padx=2, pady=2)
tekst.grid(row=0, column=0, columnspan=4)

#nupud 4 rida
nupp0 = Button(aken, text="0", width=4, font="Tahoma 12")
nupp0.grid(row=4, column=0, padx=2, pady=2)

nuppkom = Button(aken, text=",", width=4, font="Tahoma 12")
nuppkom.grid(row=4, column=1, padx=2, pady=2,)

nuppsum = Button(aken, text="=", width=4, font="Tahoma 12")
nuppsum.grid(row=4, column=2, padx=2, pady=2)

nuppplus = Button(aken, text="+", width=4, font="Tahoma 12")
nuppplus.grid(row=4, column=3, padx=2, pady=2)

#nupud 3 rida
nupp1 = Button(aken, text="1", width=4, font="Tahoma 12")
nupp1.grid(row=3, column=0, padx=2, pady=2)

nupp2 = Button(aken, text="2", width=4, font="Tahoma 12")
nupp2.grid(row=3, column=1, padx=2, pady=2)

nupp3 = Button(aken, text="3", width=4, font="Tahoma 12")
nupp3.grid(row=3, column=2, padx=2, pady=2)

nuppmin = Button(aken, text="-", width=4, font="Tahoma 12")
nuppmin.grid(row=3, column=3, padx=2, pady=2)


#nupud 2 rida
nupp4 = Button(aken, text="4", width=4, font="Tahoma 12")
nupp4.grid(row=2, column=0, padx=2, pady=2)

nupp5 = Button(aken, text="5", width=4, font="Tahoma 12")
nupp5.grid(row=2, column=1, padx=2, pady=2)

nupp6 = Button(aken, text="6", width=4, font="Tahoma 12")
nupp6.grid(row=2, column=2, padx=2, pady=2)

nuppkor = Button(aken, text="*", width=4, font="Tahoma 12")
nuppkor.grid(row=2, column=3, padx=2, pady=2)



#nupud 1 rida
nupp7 = Button(aken, text="7", width=4, font="Tahoma 12")
nupp7.grid(row=1, column=0, padx=2, pady=2)

nupp8 = Button(aken, text="8", width=4, font="Tahoma 12")
nupp8.grid(row=1, column=1, padx=2, pady=2)

nupp9 = Button(aken, text="9", width=4, font="Tahoma 12")
nupp9.grid(row=1, column=2, padx=2, pady=2)

nupp10 = Button(aken, text="/", width=4, font="Tahoma 12")
nupp10.grid(row=1, column=3, padx=2, pady=2)



aken.mainloop()