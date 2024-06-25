# csv contains plain text and wellknown format..
import pandas as pd
a = pd.DataFrame({"a":[2,4,6,8], "b":[1,2,3,4]})
a.to_csv("file.csv", index = False, header = ["newa", "newb"])

a = sns.load_dataset('penguins').head(20)

# --------Read Csv File --------
a = pd.read_csv("tips.csv")
print(a)
# -->to get specific number of rows
a1 = pd.read_csv("tips.csv", nrows=3)
# print(a1)

# -->to get specific coulmn
a2 = pd.read_csv("tips.csv", usecols=['sex', 'total_bill'])
# print(a2)

# --> also get coulmn by index number
a3 = pd.read_csv("tips.csv", usecols=[0,1])
# print(a3)

# --> to skip rows
a4 = pd.read_csv("tips.csv", skiprows=[0,1,2])
# print(a4)

# -->"To represent a column as an index."
a5 = pd.read_csv("tips.csv", index_col= 'total_bill')
# print(a5)

# -->to represent row as header
a6 = pd.read_csv("tips.csv", header= [2])
# print(a6)

# -->chg the headings
a7 = pd.read_csv("tips.csv",names =['Abc', 'Def', 'Ghi','Jkl','Mno','Pqr','Stu'])
# print(a7)

# -->Remove the existing headings and give the new
# a8 = pd.read_csv("tips.csv",  header=None, prefix="X_") #prefix not working
# print(a8)

# -->chg dataType
a8 = pd.read_csv("tips.csv", dtype={'size':'float'})
print(a8)