import pandas as pd

Sat2017 = pd.read_csv("sat_2017.csv")
Sat2017 = pd.DataFrame(Sat2017)
print("Number of rows in Sat_2017 CSV" + str(Sat2017.shape))

Act2017 = pd.read_csv("act_2017.csv")
Act2017 = pd.DataFrame(Sat2017)
print("Number of rows in Act_2017 CSV" + str( Act2017.shape))


Sat2018 = pd.read_csv("sat_2018.csv")
Sat2018 = pd.DataFrame(Sat2017)
print("Number of rows in Sat_2018 CSV" + str(Sat2018.shape))

Act2018 = pd.read_csv("act_2018.csv")
Act2018 = pd.DataFrame(Sat2017)
print("Number of rows in Sat_2017 CSV" + str(Act2018.shape))

SatAct2017 = pd.read_csv("sat_act_17.csv")
SatAct2017 = pd.DataFrame(Sat2017)
print("Number of rows in SatAct2017 CSV" + str(SatAct2017.shape))

SatAct2018 = pd.read_csv("sat_act_18.csv")
SatAct2018 = pd.DataFrame(Sat2018)
print("Number of rows in SatAct2018 CSV" + str(SatAct2018.shape))


Sat2017 = pd.read_csv("sat_2017.csv")
Sat2017 = pd.DataFrame(Sat2017)
print("Top 5 rows in  the dataframe")
print(Sat2017.head())
print(Sat2017["State"].value_counts())




