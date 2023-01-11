from tkinter import *

#akna seaded
aken = Tk()
aken.title('Botswana')
#aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=500, height=300)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 150, fill="white", width=0)
louend.create_arc(10, 160, 200, 240, extent=135)
louend.create_arc(10, 160, 200, 240, extent=135)
louend.create_rectangle(0, 150, 500, 300, fill="red", width=0)



aken.mainloop()