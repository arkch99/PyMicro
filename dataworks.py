import csv
import os
import datetime as dt

fields = ("First name", "Middle name", "Last name", "DoB", "Gender", "Eating", "Hobby", "Phy", "Chem", "Maths", "Total", "Percentage", "Phone", "Mail", "Country",  "State", "City","Locality", "District", "Post Office","Police Station", "PIN", "TCountry",  "TState", "TCity","TLocality", "TDistrict", "TPost Office", "TPolice Station",  "TPIN", "Guardian's Name", "Guardian's Relation", "Guardian's Occupation", "Guardian's Phone", "Guardian's Mail", "Guardian's Country",  "Guardian's State", "Guardian's City","Guardian's Locality", "Guardian's District", "Guardian's Post Office","Guardian's Police Station" , "Guardian's PIN")

states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnatak', 'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

mandatory = ("First name", "Last name", "DoB", "Gender", "Eating", "Phy", "Chem", "Maths", "Phone","Country",
"State", "City","Locality", "District", "Post Office", "Police Station", "PIN", "Guardian's Name", "Guardian's Relation", "Guardian's Phone", "Guardian's Country",  "Guardian's State", "Guardian's City","Guardian's Locality", "Guardian's District", "Guardian's Post Office", "Guardian's Police Station" , "Guardian's PIN")

def validate(suspDict):
    invalids = list()
    for key in mandatory:
        if suspDict[key] == "":
            invalids.append(key)
        elif key == "Phone" or key == "Guardian's Phone" or key == "PIN" or key == "Guardian's PIN" or key == "Phy" or key == "Chem" or key == "Maths":
            try:
                test = float(suspDict[key])
                if (key == "Phy" or key == "Chem" or key == "Maths") and test > 100.0:
                    raise ValueError
            except ValueError: #if those are not purely numeric
                invalids.append(key)
        elif key == "DoB":
            date = suspDict[key].split("-")
            try:
                date = list(map(int, date))
                if len(date) != 3:
                    raise ValueError
                testDate = dt.datetime(date[2], date[1], date[0])
            except (ValueError, TypeError):
                invalids.append(key)               
        else:
            for ch in suspDict[key]:
                if ch.isdigit():
                    invalids.append(key)
                    break
    return invalids       
                


def newRecord(varDict): #varList is in the order maintained in new_entry
    #print(varDict)
    varDict["Total"] = float(varDict["Phy"]) + float(varDict["Chem"]) + float(varDict["Maths"])
    varDict["Percentage"] = float(varDict["Total"]) / 3
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