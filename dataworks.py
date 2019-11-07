import csv
import os


fields = ("First name", "Middle name", "Last name", "DoB", "Gender", "Eating", "Hobby", "Phy", "Chem", "Maths", "Total", "Average", "Phone", "Mail", "Locality", "District", "City", "PO", "PS", "State", "Country", "PIN", "GName", "GRelation", "GOcc", "GPhone", "GMail")
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kasmir', 'Jharkhand', 'Karnatak', 'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']


def newRecord(varDict): #varList is in the order maintained in new_entry
    #print(varDict)
    varDict["Total"] = float(varDict["Phy"]) + float(varDict["Chem"]) + float(varDict["Maths"])
    varDict["Average"] = float(varDict["Total"]) / 3
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