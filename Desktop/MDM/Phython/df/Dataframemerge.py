import pandas as pd
import numpy as np


ContactExcel = pd.read_excel("Eloqua Validation ContactID.xlsx")
#ContactExcel = pd.read_excel("Left.xlsx")
ContactData =  pd.DataFrame(ContactExcel)
print("Number of rows", str(ContactData.shape))
#print(ContactData)
#ContactData = ContactData.set_index(0)

LastNameExcel = pd.read_excel("Eloqua Validation LastName.xlsx")
#LastNameExcel = pd.read_excel("Right.xlsx")
LastNameData = pd.DataFrame(LastNameExcel)
print("Number of rows", str(LastNameData.shape))
#print(LastNameData)
mergeC = pd.merge(ContactData,LastNameData,on='SRC_EMAILADDRESS')
print(mergeC.shape)

'''
#LastNameData = LastNameData.set_index(0)
print("Merge Process")
MergeContact = ContactData.merge(ContactData,LastNameData,on='SRC_EMAILADDRESS')
print("Number of rows", str(MergeContact.shape)) '''


