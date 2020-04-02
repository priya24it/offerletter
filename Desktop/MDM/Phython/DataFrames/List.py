import pandas as pd

# List is nothing but Ordered collection(Which holds mixed datatypes) and changeable (By using add(insert,append,extend) methods and remove,popup methods)

# scenario 1 : Integer data type , we can define the list using square brackets
# definition of a single list , homogenous  type.
list1 = [1,2,3,4,5]
print(list1) # print statement is used to print the data as it is

# accessing elements using for loop
for i in list1:
    print(i)  # using for loop we can print the data line by line

# displaying elements using using pandas
df = pd.DataFrame(list1)
print(df) # using data frame we can print the data in tabular format.


# holding the string data types
listHetero  = ['Adam','Sheldon','Missy','Duke']
print(listHetero)
# accessing elements using for loop
for i in listHetero:
    print(i)
# displaying elements using using pandas
print('display string elements')
dfHetero = pd.DataFrame(listHetero)
print(dfHetero)

# definition of a multi single list i.e nothing but sub list
listHetero1 = ['Adam',1,'Sheldon',2,'Missy',3,'Duke',4]
print(listHetero1)
# accessing elements using for loop
for i in listHetero1:
    print(listHetero1)
# displaying elements using using pandas
# print('display heterogeneous elements')
dflistHetero1 = pd.DataFrame(listHetero1)
print(dflistHetero1)

#Adding elements using insert , Insert method will be useful to insert elements at specfic position.
listinsert = [1,2,3,4,5]
listinsert.insert(1,7) # insert elements at position 1
print(listinsert)
# displaying elements using using pandas
print('Inserting elements at position 1 ')
df = pd.DataFrame(listinsert)
print(df)

#Adding elements using extend , extend will add elements at the end of the list.
list1.extend([87,88,89]) # list should be added using square brackets.
print(list1)
# displaying elements using  pandas
df = pd.DataFrame(list1)
print(df)

# Append menthod , we can also add elements to the list using append method.
ListAppend = ['Invite','Cordinally','Perfect']
print('Printing ListAppend list')
df = pd.DataFrame(ListAppend)
print(df)
ListAppend.append("Wonderful")
print('Printing ListAppend list after adding elements')
df = pd.DataFrame(ListAppend)
print(df)




# accessing the last elements using negative index
listLast = ['a','b','c','d','e','f']
print(listLast)
print(listLast[-4])  # accessing the last 4th element.

#remove elements using remove menthod
ListRemove = [1,2,3,4,5,6,7]
print(ListRemove.remove(5)) # 5 is the data value and not the Index value.
print(ListRemove)

#remove elements using pop menthod
ListRemove = ['a','b','c','d','e','f','g']
print(ListRemove.pop())
print(ListRemove)



# We can remove the elements using range
#for i in range(1, 5):
#    List.remove(i)

# Displaying the range of elements using Slice operator :
ListSlice = ['a','b','c','d','e','f','g']
print(ListSlice[2:4])


# Changing elements in List
ListChangle = ['Adam','Sandra','Simbha']
print("Before changing the list")
df = pd.DataFrame(ListChangle)
print(df)
ListChangle[0] = 'Rayer'
print("After changing the list")
df = pd.DataFrame(ListChangle)
print(df)

# List  allow duplicates
ListDuplicate = ['Simbha','Sandra','Simbha']
print("Displaying Duplicate Values")
df = pd.DataFrame(ListDuplicate)
print(df)

#List  multi diemnsional array
ListMultiDimensional = [1,2,3,4,5,[7,8,9]]
print("Displaying multidimesnioanl list")
print(ListMultiDimensional)
print('Sub List of element1 '+str(ListMultiDimensional[5][0]))
print('Sub List of element2 '+str(ListMultiDimensional[5][1]))
print('Sub List of element3 '+str(ListMultiDimensional[5][2]))







