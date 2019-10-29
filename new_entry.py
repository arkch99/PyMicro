from tkinter import*
import tkinter.font as font

def populate(container):
    h1 = font.Font(family='Courier', size=30, weight='bold')
    sub = font.Font(family='Courier', size=20)

    #Student's details:
    s=Label(container,text="Student details:-",font=h1).grid(row=0,pady=8,padx=100)
    s1=Label(container,text="First name: ",font=sub).grid(row=1,sticky=W,pady=4)
    s1e=Entry(container).grid(row=1,column=1)
    s2=Label(container,text="Middle name: ",font=sub).grid(row=2,sticky=W,pady=4)
    s2e=Entry(container).grid(row=2,column=1)
    s3=Label(container,text="Last name: ",font=sub).grid(row=3,sticky=W,pady=4)
    s3e=Entry(container).grid(row=3,column=1)
    s4=Label(container,text="Date of Birth: ",font=sub).grid(row=4,sticky=W,pady=4)
    s4e=Entry(container).grid(row=4,column=1)
    v1 = StringVar()    #String Variable for Gender  
    v2 = StringVar()    #String Variable for Eating Preferences
    s5=Label(container,text="Gender: ",font=sub).grid(row=5,sticky=W,pady=4)
    s5e1=Radiobutton(container, text = "Male", font=sub, variable = v1,value = "Male").grid(row=5,column=1)   
    s5e2=Radiobutton(container, text = "Female", font=sub, variable = v1,value = "Female").grid(row=5,column=2)
    s6=Label(container,text="Eating Preferences: ",font=sub).grid(row=6,sticky=W,pady=4)
    s6e1=Radiobutton(container, text = "Veg", font=sub,variable = v2,value = "Veg").grid(row=6,column=1)
    s6e2=Radiobutton(container, text = "Non-Veg", font=sub,variable = v2,value = "Non-Veg").grid(row=6,column=2)
    s7=Label(container,text="Hobbies: ",font=sub).grid(row=7,sticky=W,pady=4)
    s7e=Entry(container).grid(row=7,column=1)
    s8=Label(container,text="12th physics marks: ",font=sub).grid(row=8,sticky=W,pady=4)
    s8e=Entry(container).grid(row=8,column=1)
    s9=Label(container,text="12th chemistry marks: ",font=sub).grid(row=9,sticky=W,pady=4)
    s9e=Entry(container).grid(row=9,column=1)
    s10=Label(container,text="12th maths marks: ",font=sub).grid(row=10,sticky=W,pady=4)
    s10e=Entry(container).grid(row=10,column=1)

    #Contact details
    c=Label(container,text="Contact details:-",font=h1).grid(row=11,pady=8,padx=100)
    c1=Label(container,text="Phone no: ",font=sub).grid(row=12,sticky=W,pady=4)
    c1e=Entry(container).grid(row=12,column=1)
    c2=Label(container,text="Email address: ",font=sub).grid(row=13,sticky=W,pady=4)
    c2e=Entry(container).grid(row=13,column=1)
    c3=Label(container,text="Locality: ",font=sub).grid(row=14,sticky=W,pady=4)
    c3e=Entry(container).grid(row=14,column=1)
    c4=Label(container,text="District: ",font=sub).grid(row=15,sticky=W,pady=4)
    c4e=Entry(container).grid(row=15,column=1)
    c5=Label(container,text="City: ",font=sub).grid(row=16,sticky=W,pady=4)
    c5e=Entry(container).grid(row=16,column=1)
    c6=Label(container,text="Post Office: ",font=sub).grid(row=17,sticky=W,pady=4)
    c6e=Entry(container).grid(row=17,column=1)
    c7=Label(container,text="Police Station: ",font=sub).grid(row=18,sticky=W,pady=4)
    c7e=Entry(container).grid(row=18,column=1)
    c8=Label(container,text="State: ",font=sub).grid(row=19,sticky=W,pady=4)
    c8e=Entry(container).grid(row=19,column=1)
    c9=Label(container,text="Country: ",font=sub).grid(row=20,sticky=W,pady=4)
    c9e=Entry(container).grid(row=20,column=1)
    c10=Label(container,text="PINCODE: ",font=sub).grid(row=21,sticky=W,pady=4)
    c10e=Entry(container).grid(row=21,column=1)
    
    #Guardians details
    g=Label(container,text="Guardian details:-",font=h1).grid(row=22,pady=8,padx=100)
    g1=Label(container,text="Guardian's name: ",font=sub).grid(row=23,sticky=W,pady=4)
    g1e=Entry(container).grid(row=23,column=1)
    g2=Label(container,text="Relation: ",font=sub).grid(row=24,sticky=W,pady=4)
    g2e=Entry(container).grid(row=24,column=1)
    g3=Label(container,text="Occupation: ",font=sub).grid(row=25,sticky=W,pady=4)
    g3e=Entry(container).grid(row=25,column=1)
    g4=Label(container,text="Phone: ",font=sub).grid(row=26,sticky=W,pady=4)
    g4e=Entry(container).grid(row=26,column=1)
    g5=Label(container,text="Email: ",font=sub).grid(row=27,sticky=W,pady=4)
    g5e=Entry(container).grid(row=27,column=1)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def entry():
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    canvas =Canvas(root)
    frame = Frame(canvas)
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame)

    root.mainloop()

if __name__=="__main__":
    entry()
