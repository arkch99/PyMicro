import csv
import os

fields = ("First name", "Middle name", "Last name", "DoB", "Gender", "Eating", "Hobby", "Phy", "Chem", "Maths", "Phone", "Mail", "Locality", "District", "City", "PO", "PS", "State", "Country", "PIN", "GName", "GRelation", "GOcc", "GPhone", "GMail")

def newRecord(varDict): #varList is in the order maintained in new_entry
    #print(varDict)
    firstFlag = False
    if not os.path.exists("records.csv"):
        open("records.csv", "x")
        firstFlag = True
               
    with open("records.csv", "a", newline="") as db:
        if firstFlag:
            headWriter = csv.writer(db)
            headWriter.writerow(fields)
        writer = csv.DictWriter(db, fields, restval = "")
        writer.writerow(varDict)