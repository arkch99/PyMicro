from tkinter import*
import tkinter.font as font
import dataworks

root = Tk()
root.title("Admission form")

def show_st(event, root, country, state):
    if country.get() == "India":
        enState = OptionMenu(root, state, *dataworks.states)
        enState.grid(row=1, column=3)
    else:
        enState = Entry(root, textvariable=state)
        enState.grid(row=1,column=3)
 
def entry():
    h = font.Font(family='Courier', size=50, weight='bold')
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    f1=Frame(root,bg="blue").pack(side=TOP,fill=X)
    photo = PhotoImage(file = "ABC-Logo.jpg")
    Label(f1,image=photo).pack(side=TOP)
    Label(f1,text="ABC School of Engineering",font=h,bg="blue",fg="white",height=2).pack(side=LEFT)
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
    for i in range(len(dataworks.fields)):
        f = dataworks.fields[i]
        v = attVarList[i].get()
        d[f] = v
    #print(d)
    dataworks.newRecord(d)

def populate(container):
    h1 = font.Font(family='Courier', size=30)
    sub = font.Font(family='Courier', size=22)

    dvars = dict()
    dvars = dvars.fromkeys(dataworks.fields, "")
    l = [StringVar() for i in range(len(dataworks.fields))]
    
    #Student's details:
    student = LabelFrame(container, text="Student details", font=h1)
    student.grid(row=0,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Labels
    Label(student,text="    First name: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(student, textvariable=l[0]).grid(row=1,column=1)
    Label(student,text="    Middle name: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(student, textvariable=l[1]).grid(row=1,column=3)
    Label(student,text="    Last name: ",font=sub).grid(row=1,column=4,sticky=W,pady=4)
    Entry(student, textvariable=l[2]).grid(row=1,column=5)
    Label(student,text="    Date of Birth: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(student, textvariable=l[3]).grid(row=2,column=1)
    Label(student,text="    Gender: ",font=sub).grid(row=3,sticky=W,pady=4)    
    Radiobutton(student, text = "Male", font=sub, variable = l[4],value = "Male").grid(row=3,column=1)   
    Radiobutton(student, text = "Female", font=sub, variable = l[4],value = "Female").grid(row=3,column=2)
    Label(student,text="    Eating Preferences: ",font=sub).grid(row=4,sticky=W,pady=4)
    Radiobutton(student, text = "Veg", font=sub,variable = l[5],value = "Veg").grid(row=4,column=1)
    Radiobutton(student, text = "Non-Veg", font=sub,variable = l[5],value = "Non-Veg").grid(row=4,column=2)
    Label(student,text="    Hobbies: ",font=sub).grid(row=5,sticky=W,pady=4)
    Entry(student, textvariable=l[6]).grid(row=5,column=1)
    Label(student,text="    Physics marks: ",font=sub).grid(row=8,sticky=W,pady=4)
    Entry(student, textvariable=l[7]).grid(row=8,column=1)
    Label(student,text="    Chemistry marks: ",font=sub).grid(row=8,column=2,sticky=W,pady=4)
    Entry(student, textvariable=l[8]).grid(row=8,column=3)
    Label(student,text="    Maths marks: ",font=sub).grid(row=8,column=4,sticky=W,pady=4)
    Entry(student, textvariable=l[9]).grid(row=8,column=5)

    #Contact details
    contact = LabelFrame(container, text="Contact details", font=h1)
    contact.grid(row=1,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Labels
    Label(contact,text="    Phone no: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(contact, textvariable=l[10]).grid(row=1,column=1)
    Label(contact,text="    Email address: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(contact, textvariable=l[11]).grid(row=1,column=3)

    address_1 = LabelFrame(contact, text="Address 1", font=h1)
    address_1.grid(row=2,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    Label(address_1,text="    Country: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_1, textvariable=l[17])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_1, country=l[17], state=l[18]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    Label(address_1,text="    State: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Label(address_1,text="    City: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[14]).grid(row=2,column=1)
    Label(address_1,text="    Locality: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[12]).grid(row=2,column=3)
    Label(address_1,text="    District: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_1, textvariable=l[13]).grid(row=2,column=5)
    Label(address_1,text="    Post Office: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_1, textvariable=l[15]).grid(row=3,column=1)
    Label(address_1,text="    Police Station: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_1, textvariable=l[16]).grid(row=3,column=3)
    Label(address_1,text="    PINCODE: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_1, textvariable=l[19]).grid(row=3,column=5)
    
    address_2 = LabelFrame(contact, text="Address 2", font=h1)
    address_2.grid(row=3,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    Label(address_2,text="    Country: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_2, textvariable=l[17])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_2, country=l[17], state=l[18]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    Label(address_2,text="    State: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Label(address_2,text="    City: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[14]).grid(row=2,column=1)
    Label(address_2,text="    Locality: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[12]).grid(row=2,column=3)
    Label(address_2,text="    District: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_2, textvariable=l[13]).grid(row=2,column=5)
    Label(address_2,text="    Post Office: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_2, textvariable=l[15]).grid(row=3,column=1)
    Label(address_2,text="    Police Station: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_2, textvariable=l[16]).grid(row=3,column=3)
    Label(address_2,text="    PINCODE: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_2, textvariable=l[19]).grid(row=3,column=5)
    Checkbutton(address_2, text="Same as address 1",font=sub).grid(row=4,column=1,sticky=W)
    #for input to checkbox use variable or textvariable

    #Guardians details
    guardian = LabelFrame(container, text="Guardian details", font=h1)
    guardian.grid(row=2,columnspan=7,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Labels
    Label(guardian,text="   Guardian's name: ",font=sub).grid(row=1,sticky=W,pady=4)
    Entry(guardian, textvariable=l[20]).grid(row=1,column=1)
    Label(guardian,text="   Relation: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[21]).grid(row=1,column=3)
    Label(guardian,text="   Occupation: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[22]).grid(row=2,column=1)
    Label(guardian,text="   Phone: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(guardian, textvariable=l[23]).grid(row=3,column=1)
    Label(guardian,text="   Email: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(guardian, textvariable=l[24]).grid(row=3,column=3)

    address_3 = LabelFrame(guardian, text="Address", font=h1)
    address_3.grid(row=4,columnspan=6,sticky=W, padx=5, pady=5, ipadx=5, ipady=5)
    #Addrss details
    Label(address_3,text="    Country: ",font=sub).grid(row=1,sticky=W,pady=4)
    enCountry=Entry(address_3, textvariable=l[17])
    enCountry.bind("<KeyRelease-Return>", lambda event, root=address_3, country=l[17], state=l[18]: show_st(event, root, country, state))
    enCountry.grid(row=1,column=1)
    Label(address_3,text="    State: ",font=sub).grid(row=1,column=2,sticky=W,pady=4)
    Label(address_3,text="    City: ",font=sub).grid(row=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[14]).grid(row=2,column=1)
    Label(address_3,text="    Locality: ",font=sub).grid(row=2,column=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[12]).grid(row=2,column=3)
    Label(address_3,text="    District: ",font=sub).grid(row=2,column=4,sticky=W,pady=4)
    Entry(address_3, textvariable=l[13]).grid(row=2,column=5)
    Label(address_3,text="    Post Office: ",font=sub).grid(row=3,sticky=W,pady=4)
    Entry(address_3, textvariable=l[15]).grid(row=3,column=1)
    Label(address_3,text="    Police Station: ",font=sub).grid(row=3,column=2,sticky=W,pady=4)
    Entry(address_3, textvariable=l[16]).grid(row=3,column=3)
    Label(address_3,text="    PINCODE: ",font=sub).grid(row=3,column=4,sticky=W,pady=4)
    Entry(address_3, textvariable=l[19]).grid(row=3,column=5)
    Checkbutton(address_3, text="Same as address 1",font=sub).grid(row=4,column=1,sticky=W)

    Button(container, text="Submit", command=lambda:Sub(l), width=20).grid(row = 4, column=3)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

if __name__=="__main__":
   entry()
