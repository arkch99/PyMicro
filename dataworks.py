import csv
import os

fields = ("First name", "Middle name", "Last name", "DoB", "Gender", "Eating", "Hobby", "Phy", "Chem", "Maths", "Phone", "Mail", "Locality", "District", "City", "PO", "PS", "State", "Country", "PIN", "GName", "GRelation", "GOcc", "GPhone", "GMail")

def newRecord(varDict): #varList is in the order maintained in new_entry
    print(varDict)
    if not os.path.exists("records.csv"):
        open("records.csv", "x")
    with open("records.csv", newline="") as database:
        writer = csv.DictWriter(database, fields, restval = "")
        writer.writerow(varDict)