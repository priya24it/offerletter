import pandas as pd
import function as f


Excel = pd.ExcelWriter('MDMBusinessTables.xlsx')
l1 = {1,2.0,"priya"}
df = pd.DataFrame(l1)
print(df)
df.to_excel(Excel, sheet_name='Main')

l2 = {1,2.0,3}
df1 = pd.DataFrame(l2)
df1.to_excel(Excel, sheet_name='Main_Multiple')
df1.to_excel('MDMBackuptableQuieres.xlsx')

df1.style.apply(f.mul(5))
#df1 = df1.sort_values(by=[''],inplace=True)
j = 5
print('value of a function' + str(f.mul(5)))
print(df1)
Excel.save()



