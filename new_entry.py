from tkinter import*
import tkinter.font as font
import dataworks

def populate(container):
    h1 = font.Font(family='Courier', size=30, weight='bold')
    sub = font.Font(family='Courier', size=20)

    dvars = dict()
    dvars = dvars.fromkeys(dataworks.fields, "")
    l = [StringVar() for i in range(len(dataworks.fields))]
    #Student's details:
    heading=Label(container,text="Student details:-",font=h1).grid(row=0,pady=8,padx=100)
    
    lbFName=Label(container,text="First name: ",font=sub).grid(row=1,sticky=W,pady=4)
    enFName=Entry(container, textvariable=l[0]).grid(row=1,column=1)

    lbMName=Label(container,text="Middle name: ",font=sub).grid(row=2,sticky=W,pady=4)
    enMName=Entry(container, textvariable=l[1]).grid(row=2,column=1)
    
    lbLName=Label(container,text="Last name: ",font=sub).grid(row=3,sticky=W,pady=4)
    enLName=Entry(container, textvariable=l[2]).grid(row=3,column=1)
    
    lbDOB=Label(container,text="Date of Birth: ",font=sub).grid(row=4,sticky=W,pady=4)
    enDOB=Entry(container, textvariable=l[3]).grid(row=4,column=1)
    
    #v1 = StringVar()    #String Variable for Gender  
    #v2 = StringVar()    #String Variable for Eating Preferences
    
    lbGen=Label(container,text="Gender: ",font=sub).grid(row=5,sticky=W,pady=4)    
    rbMGen=Radiobutton(container, text = "Male", font=sub, variable = l[4],value = "Male").grid(row=5,column=1)   
    rbFGen=Radiobutton(container, text = "Female", font=sub, variable = l[4],value = "Female").grid(row=5,column=2)
    
    lbEat=Label(container,text="Eating Preferences: ",font=sub).grid(row=6,sticky=W,pady=4)
    rbVeg=Radiobutton(container, text = "Veg", font=sub,variable = l[5],value = "Veg").grid(row=6,column=1)
    rbNVeg=Radiobutton(container, text = "Non-Veg", font=sub,variable = l[5],value = "Non-Veg").grid(row=6,column=2)
    
    lbHob=Label(container,text="Hobbies: ",font=sub).grid(row=7,sticky=W,pady=4)
    enHob=Entry(container, textvariable=l[6]).grid(row=7,column=1)
    
    lbPhy=Label(container,text="12th Physics marks: ",font=sub).grid(row=8,sticky=W,pady=4)
    enPhy=Entry(container, textvariable=l[7]).grid(row=8,column=1)
    
    lbChem=Label(container,text="12th Chemistry marks: ",font=sub).grid(row=9,sticky=W,pady=4)
    enChem=Entry(container, textvariable=l[8]).grid(row=9,column=1)
    
    lbMath=Label(container,text="12th Maths marks: ",font=sub).grid(row=10,sticky=W,pady=4)
    enMath=Entry(container, textvariable=l[9]).grid(row=10,column=1)

    #Contact details
    lbCon=Label(container,text="Contact details:-",font=h1).grid(row=11,pady=8,padx=100)

    lbPhone=Label(container,text="Phone no: ",font=sub).grid(row=12,sticky=W,pady=4)
    enPhone=Entry(container, textvariable=l[10]).grid(row=12,column=1)

    lbMail=Label(container,text="Email address: ",font=sub).grid(row=13,sticky=W,pady=4)
    enMail=Entry(container, textvariable=l[11]).grid(row=13,column=1)

    lbLocal=Label(container,text="Locality: ",font=sub).grid(row=14,sticky=W,pady=4)
    enLocal=Entry(container, textvariable=l[12]).grid(row=14,column=1)

    lbDis=Label(container,text="District: ",font=sub).grid(row=15,sticky=W,pady=4)
    enDis=Entry(container, textvariable=l[13]).grid(row=15,column=1)

    lbCity=Label(container,text="City: ",font=sub).grid(row=16,sticky=W,pady=4)
    enCity=Entry(container, textvariable=l[14]).grid(row=16,column=1)

    lbPO=Label(container,text="Post Office: ",font=sub).grid(row=17,sticky=W,pady=4)
    enPO=Entry(container, textvariable=l[15]).grid(row=17,column=1)

    lbPol=Label(container,text="Police Station: ",font=sub).grid(row=18,sticky=W,pady=4)
    enPol=Entry(container, textvariable=l[16]).grid(row=18,column=1)

    lbState=Label(container,text="State: ",font=sub).grid(row=19,sticky=W,pady=4)
    enState=Entry(container, textvariable=l[17]).grid(row=19,column=1)

    lbCountry=Label(container,text="Country: ",font=sub).grid(row=20,sticky=W,pady=4)
    enCountry=Entry(container, textvariable=l[18]).grid(row=20,column=1)

    lbPin=Label(container,text="PINCODE: ",font=sub).grid(row=21,sticky=W,pady=4)
    enPin=Entry(container, textvariable=l[19]).grid(row=21,column=1)
    
    #Guardians details
    lbGuard=Label(container,text="Guardian details:-",font=h1).grid(row=22,pady=8,padx=100)

    lbGName=Label(container,text="Guardian's name: ",font=sub).grid(row=23,sticky=W,pady=4)
    enGName=Entry(container, textvariable=l[20]).grid(row=23,column=1)

    lbGRel=Label(container,text="Relation: ",font=sub).grid(row=24,sticky=W,pady=4)
    enGRel=Entry(container, textvariable=l[21]).grid(row=24,column=1)

    lbGOcc=Label(container,text="Occupation: ",font=sub).grid(row=25,sticky=W,pady=4)
    enGOcc=Entry(container, textvariable=l[22]).grid(row=25,column=1)

    lbGPhone=Label(container,text="Phone: ",font=sub).grid(row=26,sticky=W,pady=4)
    enGPhone=Entry(container, textvariable=l[23]).grid(row=26,column=1)

    lbGMail=Label(container,text="Email: ",font=sub).grid(row=27,sticky=W,pady=4)
    enGMail=Entry(container, textvariable=l[24]).grid(row=27,column=1)
    #print(dvars)
    #print(len(dataworks.fields))
    bSubmit = Button(container, text="Submit", command=lambda d = {dataworks.fields[i]:l[i].get() for i in range(25)}:dataworks.newRecord(d))
    bSubmit.grid(row = 28, column=3)

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
