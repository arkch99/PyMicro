from tkinter import*
import tkinter.font as font
import dataworks as dw

root = Tk()
root.title("Admission form")

def show_st(event, root, country, state):
    if country.get() == "India":
        enState = OptionMenu(root, state, *dw.states)
        enState.grid(row=1, column=3)
    else:
        enState = Entry(root, textvariable=state)
        enState.grid(row=1,column=3)
 
def entry():
    h = font.Font(family='Courier', size=50, weight='bold')
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    f1=Frame(root,bg="blue").pack(side=TOP,fill=X)
    #photo = PhotoImage(file = "ABC-Logo.jpg")
    #Label(f1,image=photo).pack(side=TOP)
    Label(f1,text="ABC School of Engineering",font=h,bg="blue",fg="white",height=2).pack(side=TOP,fill=X)
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

def Sub(attVarList):    
    d = dict()
    c = 0
    for i in range(len(dw.fields)):
        if i == 10 or i == 11: #10 and 11 are Total and Average, so skip them
            continue
        f = dw.fields[i]        
        v = attVarList[i].get()
        d[f] = v
        c += 1
    print(d)
    print("Validation failed for:") #testing
    print(dw.validate(d))
    if not len(dw.validate(d)): #invalids has 0 items if all fields are valid
        dw.newRecord(d)
    #else: display message box with items from invalid

def populate(container):
    
    h1 = font.Font(family='Courier', size=30, weight='bold')
    sub = font.Font(family='Courier', size=20)
    
    l = [StringVar() for i in range(len(dw.fields))]
    #Student's details:
    heading=Label(container,text="Student details:-",font=h1).grid(row=0,pady=8,padx=100)
    
    lbFName=Label(container,text="First name: ",font=sub).grid(row=1,sticky=W,pady=4)
    enFName=Entry(container, textvariable=l[0])
    enFName.grid(row=1,column=1)

    lbMName=Label(container,text="Middle name: ",font=sub).grid(row=2,sticky=W,pady=4)
    enMName=Entry(container, textvariable=l[1]).grid(row=2,column=1)
    
    lbLName=Label(container,text="Last name: ",font=sub).grid(row=3,sticky=W,pady=4)
    enLName=Entry(container, textvariable=l[2]).grid(row=3,column=1)
    
    lbDOB=Label(container,text="Date of Birth: ",font=sub).grid(row=4,sticky=W,pady=4)
    enDOB=Entry(container, textvariable=l[3]).grid(row=4,column=1)
        
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
    enPhone=Entry(container, textvariable=l[12]).grid(row=12,column=1)

    lbMail=Label(container,text="Email address: ",font=sub).grid(row=13,sticky=W,pady=4)
    enMail=Entry(container, textvariable=l[13]).grid(row=13,column=1)

    lbLocal=Label(container,text="Locality: ",font=sub).grid(row=14,sticky=W,pady=4)
    enLocal=Entry(container, textvariable=l[14]).grid(row=14,column=1)

    lbDis=Label(container,text="District: ",font=sub).grid(row=15,sticky=W,pady=4)
    enDis=Entry(container, textvariable=l[15]).grid(row=15,column=1)

    lbCity=Label(container,text="City: ",font=sub).grid(row=16,sticky=W,pady=4)
    enCity=Entry(container, textvariable=l[16]).grid(row=16,column=1)

    lbPO=Label(container,text="Post Office: ",font=sub).grid(row=17,sticky=W,pady=4)
    enPO=Entry(container, textvariable=l[17]).grid(row=17,column=1)

    lbPol=Label(container,text="Police Station: ",font=sub).grid(row=18,sticky=W,pady=4)
    enPol=Entry(container, textvariable=l[18]).grid(row=18,column=1)

    lbCountry=Label(container,text="Country: ",font=sub).grid(row=19,sticky=W,pady=4)
    enCountry=Entry(container, textvariable=l[20])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=container, country=l[20], state=l[19]: show_st(event, root, country, state))
    enCountry.grid(row=19,column=1)
    
    lbState=Label(container,text="State: ",font=sub).grid(row=20,sticky=W,pady=4)
    ##enState=Entry(container, textvariable=l[18]).grid(row=20,column=1)


    lbPin=Label(container,text="PINCODE: ",font=sub).grid(row=21,sticky=W,pady=4)
    enPin=Entry(container, textvariable=l[21]).grid(row=21,column=1)
    
    #Guardians details
    lbGuard=Label(container,text="Guardian details:-",font=h1).grid(row=22,pady=8,padx=100)

    lbGName=Label(container,text="Guardian's name: ",font=sub).grid(row=23,sticky=W,pady=4)
    enGName=Entry(container, textvariable=l[22]).grid(row=23,column=1)

    lbGRel=Label(container,text="Relation: ",font=sub).grid(row=24,sticky=W,pady=4)
    enGRel=Entry(container, textvariable=l[23]).grid(row=24,column=1)

    lbGOcc=Label(container,text="Occupation: ",font=sub).grid(row=25,sticky=W,pady=4)
    enGOcc=Entry(container, textvariable=l[24]).grid(row=25,column=1)

    lbGPhone=Label(container,text="Phone: ",font=sub).grid(row=26,sticky=W,pady=4)
    enGPhone=Entry(container, textvariable=l[25]).grid(row=26,column=1)

    lbGMail=Label(container,text="Email: ",font=sub).grid(row=27,sticky=W,pady=4)
    enGMail=Entry(container, textvariable=l[26]).grid(row=27,column=1)

    
    bSubmit = Button(container, text="Submit", font="Courier 26", command=lambda:Sub(l))
    bSubmit.config(width=20)
    bSubmit.grid(row=28, column=1, sticky=W)
 
def populate(container):
    h1 = font.Font(family='Courier', size=30)
    sub = font.Font(family='Courier', size=16)

    l = [StringVar() for i in range(len(dw.fields))]
    
    #Student's details:
    student = LabelFrame(container, text="Student details", font=h1)
    student.grid(row=0,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Labels
    Label(student,text="    First name*: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(student, textvariable=l[0]).grid(row=1,column=1)

    Label(student,text="    Middle name: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(student, textvariable=l[1]).grid(row=1,column=3)

    Label(student,text="    Last name*: ",font=sub).grid(row=1,column=4,sticky=W,pady=4)
    Entry(student, textvariable=l[2]).grid(row=1,column=5)

    Label(student,text="    Date of Birth: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(student, textvariable=l[3]).grid(row=2,column=1)

    Label(student,text="    Gender*: ",font=sub).grid(row=3,sticky=W,pady=4)    
    Radiobutton(student, text = "Male", font=sub, variable = l[4],value = "Male").grid(row=3,column=1)   
    Radiobutton(student, text = "Female", font=sub, variable = l[4],value = "Female").grid(row=3,column=2)

    Label(student,text="    Eating Preferences*: ",font=sub).grid(row=4,sticky=W,pady=4)
    Radiobutton(student, text = "Veg", font=sub,variable = l[5],value = "Veg").grid(row=4,column=1)
    Radiobutton(student, text = "Non-Veg", font=sub,variable = l[5],value = "Non-Veg").grid(row=4,column=2)

    Label(student,text="    Hobbies: ",font=sub).grid(row=5,sticky=W,pady=4)
    Entry(student, textvariable=l[6]).grid(row=5,column=1)

    Label(student,text="    Physics marks*: ",font=sub).grid(row=8,sticky=W,pady=4)
    Entry(student, textvariable=l[7]).grid(row=8,column=1)

    Label(student,text="    Chemistry marks*: ",font=sub).grid(row=8,column=2,sticky=W,pady=4)
    Entry(student, textvariable=l[8]).grid(row=8,column=3)

    Label(student,text="    Maths marks*: ",font=sub).grid(row=8,column=4,sticky=W,pady=4)
    Entry(student, textvariable=l[9]).grid(row=8,column=5)

    #Contact details
    contact = LabelFrame(container, text="Contact details", font=h1)
    contact.grid(row=1,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    
    #Labels
    Label(contact,text="    Phone no*: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(contact, textvariable=l[12]).grid(row=1,column=1)
    
    Label(contact,text="    Email address: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(contact, textvariable=l[13]).grid(row=1,column=3)

    address_1 = LabelFrame(contact, text="Address 1", font=h1)
    address_1.grid(row=2,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    
    Label(address_1,text="    Country*: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_1, textvariable=l[14])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_1, country=l[14], state=l[15]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    
    Label(address_1,text="    State*: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    
    Label(address_1,text="    City*: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[16]).grid(row=2,column=1)
    
    Label(address_1,text="    Locality*: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[17]).grid(row=2,column=3)
    
    Label(address_1,text="    District*: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_1, textvariable=l[18]).grid(row=2,column=5)
    
    Label(address_1,text="    Post Office*: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_1, textvariable=l[19]).grid(row=3,column=1)
    
    Label(address_1,text="    Police Station*: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[20]).grid(row=3,column=3)
    
    Label(address_1,text="    PINCODE*: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_1, textvariable=l[21]).grid(row=3,column=5)


    #Address 2
    address_2 = LabelFrame(contact, text="Address 2", font=h1)
    address_2.grid(row=3,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    Label(address_2,text="    Country: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_2, textvariable=l[22])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_2, country=l[22], state=l[23]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    
    Label(address_2,text="    State: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    
    Label(address_2,text="    City: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[24]).grid(row=2,column=1)
    
    Label(address_2,text="    Locality: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[25]).grid(row=2,column=3)
    
    Label(address_2,text="    District: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_2, textvariable=l[26]).grid(row=2,column=5)
    
    Label(address_2,text="    Post Office: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_2, textvariable=l[27]).grid(row=3,column=1)
    
    Label(address_2,text="    Police Station: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[28]).grid(row=3,column=3)
    
    Label(address_2,text="    PINCODE: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_2, textvariable=l[29]).grid(row=3,column=5)
    
    Checkbutton(address_2, text="Same as address 1",font=sub).grid(row=4,column=1,sticky=W)
    #for input to checkbox use variable or textvariable

    #Guardians details
    guardian = LabelFrame(container, text="Guardian details", font=h1)
    guardian.grid(row=2,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Labels
    Label(guardian,text="   Guardian's name*: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(guardian, textvariable=l[30]).grid(row=1,column=1)
    
    Label(guardian,text="   Relation*: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[31]).grid(row=1,column=3)
    
    Label(guardian,text="   Occupation: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[32]).grid(row=2,column=1)
    
    Label(guardian,text="   Phone*: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(guardian, textvariable=l[33]).grid(row=3,column=1)
    
    Label(guardian,text="   Email: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[34]).grid(row=3,column=3)

    address_3 = LabelFrame(guardian, text="Address", font=h1)
    address_3.grid(row=4,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    Label(address_3,text="    Country*: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_3, textvariable=l[35])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_3, country=l[35], state=l[36]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    
    Label(address_3,text="    State*: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Label(address_3,text="    City*: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[37]).grid(row=2,column=1)
    
    Label(address_3,text="    Locality*: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[38]).grid(row=2,column=3)
    
    Label(address_3,text="    District*: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_3, textvariable=l[39]).grid(row=2,column=5)
    
    Label(address_3,text="    Post Office*: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_3, textvariable=l[40]).grid(row=3,column=1)
    
    Label(address_3,text="    Police Station*: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[41]).grid(row=3,column=3)
    
    Label(address_3,text="    PINCODE*: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_3, textvariable=l[42]).grid(row=3,column=5)
    Checkbutton(address_3, text="Same as address 1",font=sub).grid(row=4,column=1,sticky=W)

    Button(container, text="Submit", command=lambda:Sub(l), width=20).grid(row = 4, column=3)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

if __name__=="__main__":
   entry()
