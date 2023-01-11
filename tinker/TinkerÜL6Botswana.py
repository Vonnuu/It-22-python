from tkinter import *

#akna seaded
aken = Tk()
aken.title('Botswana')
#aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=500, height=300)
louend.pack()

#kujundite loomine

louend.create_rectangle(0, 0, 500, 100, fill="lightblue", width=0)
louend.create_rectangle(0, 100, 500, 110, fill="white", width=0)
louend.create_rectangle(0, 110, 500, 190, fill="black", width=0)
louend.create_rectangle(0, 190, 500, 200, fill="white", width=0)
louend.create_rectangle(0, 200, 500, 300, fill="lightblue", width=0)


aken.mainloop()