import pandas as pd

s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
s3 = pd.Series([7,8,9])

#print(s1,s2,s3)

df = pd.DataFrame([s1,s2,s3])
#print(df)

df.columns = ["Geeks","For","Geeks"]
#print(df)

#df.to_csv("geeks.csv")


#df.to_excel("geeks1.xls")

df = pd.DataFrame([s1,s2,s3])
#print(df)






# Creating the first Dataframe using dictionary
df1 = df = pd.DataFrame({"a": [1, 2, 3, 4],
                         "b": [5, 6, 7, 8]})

# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a": [100,101,102,103],
                    "b": [101,102,103,104]})

# Print df1

#print(df1, "\n")

# Print df2
print(df2)
#df1.append(df2)
#print(df1)
#df2.to_excel("geeks1.xls")

# Importing pandas as pd

# Creating the first Dataframe using dictionary
df1 = pd.DataFrame({"a": [1, 2, 3, 4],
                    "b": [5, 6, 7, 8]})

# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a": [1, 2, 3],
                    "b": [5, 6, 7],
                    "c": [1, 5, 4]})

# for appending df2 at the end of df1
df.append(df2, ignore_index=True,sort=False)
print(df)





