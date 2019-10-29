from tkinter import *
import tkinter.font as font
import new_entry as ne

root=Tk()

#Head:
root.title("Admission form")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#Defined frames:
top_frame=Frame(root,bg="blue")
top_frame.pack(fill=X)
separator = Frame(height=150, relief=SUNKEN)
separator.pack(fill=X)
bottom_frame=Frame(root)
bottom_frame.pack()

#Heading:
l1= Label(top_frame,text="Admission form",bg="blue")
l1.config(font=("Ubuntu Regular bold", 48))
l1.pack()

#buttons: 
myfont = font.Font(family='Courier', size=40, weight='bold')
b1=Button(bottom_frame,text="New Entry",command=ne.entry,height=4,width=30,font=myfont)
b2=Button(bottom_frame,text="View Table",height=4,width=30,font=myfont)
b3=Button(bottom_frame,text="Update Entry",height=4,width=30,font=myfont)
b1.pack()
b2.pack()
b3.pack()

root.mainloop()