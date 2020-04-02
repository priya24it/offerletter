import pandas as pd
import numpy as np

Product1 = {'Cars': ['Hero Honda','Maruthi','Suzuki','Nissan'],
             'Price':[100,200,300,400]
            }

df1 = pd.DataFrame(Product1)
print("Print Data Frame1")
print(df1)

Product1 = {'Cars': ['Hero Honda','Maruthi','Suzuki','Nissan'],
             'Price':[200,200,100,500]
            }
print("Print Data Frame2")
df2 = pd.DataFrame(Product1)
print(df2)

'''
df1['Pricefromdf2'] = df2['Price']
print(df1)

df1['pricemismatch']= np.where(df1.Price == df2.Price,True,False)
print(df1) '''

print("Single Filter")
dffilter = df1[df1.Cars == 'Nissan']
print(dffilter)

print("Multiple Filters")
dffilter1 = df1.loc[(df1.Cars == 'Hero Honda') & (df1.Price == 100)]
print(dffilter1)



Boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
        }

df = pd.DataFrame(Boxes, columns= ['Color','Shape','Price'])

color_and_shape = df.loc[(df.Color == 'Green') & (df.Shape == 'Rectangle')]
print (color_and_shape)



