import pandas as pd

# List is nothing but Ordered collection(Which holds mixed datatypes) and changeable (By using add(insert,append,extend) methods and remove,popup methods)

# scenario 1 : Integer data type , we can define the list using square brackets
# definition of a single list , homogenous  type.
t1 = (1,2,3,4,5)
print(tuple) # print statement is used to print the data as it is

# accessing elements using for loop
for i in t1:
    print(i)  # using for loop we can print the data line by line

# displaying elements using using pandas
df = pd.DataFrame(t1)
print(df) # using data frame we can print the data in tabular format.

print("Accessing an element using Index.")
print(t1[3])

list1 = list(t1)
list1.extend([10])
t1 = tuple(list1)
df = pd.DataFrame(t1)
print(df)

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
