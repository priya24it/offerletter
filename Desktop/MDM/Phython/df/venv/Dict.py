import pandas as pd
# Dict is nothing but UnOrdered collection(Which holds mixed datatypes) and changeable (By using add(insert,append,extend) methods and remove,popup methods) and unIndexed

# scenario 1 : Integer data type , we can define the Dict using curel brackets
# we define Dict using Key ,value pairs
Dict = {'Name':['Adam','Gile','Sandra'],'Salary':[10,20,30],'Age':[25,30,45] }
print(Dict)

# Display data using Dict
for i in Dict:
    print(i)

# Display data using Data Frames
df =pd.DataFrame(Dict)
print(df)

# Accessing one elemnt using Key name
print(df['Name'])

# Deleting the Key in a Dictionary
del Dict['Salary']
df =pd.DataFrame(Dict)
print(df)


Dict['Color'] = {"Red","Green","Blue"}
# Display data using Data Frames


#
Pop
Popitem
Del





