import pandas as pd
import numpy as np

path = r"Left.xlsx"

x3 = np.random.randn(100, 2)
df3 = pd.DataFrame(x3)

x4 = np.random.randn(100, 2)
df4 = pd.DataFrame(x4)

writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
df3.to_excel(writer, sheet_name = 'x3')
df4.to_excel(writer, sheet_name = 'x4')
writer.save()
writer.close()