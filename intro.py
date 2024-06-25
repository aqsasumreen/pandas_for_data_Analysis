# In data analysis, extracting useful information from data and handling missing information,
# the process includes cleaning, inspecting, transforming, and modeling data.
# Data handling, data clarification, data manipulation.
# ---------- Pandas Data Structures-----------
# Series --> One-dimensional labeled arrays, pd.Series(data)
# DataFrames --> Two-dimensional data structure with columns, similar to a table.
# Panel --> 3D container of data.
import pandas as pd
a = [2,4,6,8,10,12]
a1 = pd.Series(a, index=['a', 'b', 'c','d', 'e', 'f'], dtype='float', name='Python')
# print(a1)
# print(type(a1))

dict = {"name": ["python", "c++", "java"], "rank": [1,4,3], "pop":[10,7,18]}
a2 = pd.Series(dict)
print(a2)

a3 = pd.Series(10)
print(a3)

a4 = pd.Series(10, index=[1,2,3,4,5])
# print(a4)
a5 = pd.Series(14, index=[1,2,3])
print(a4+a5)

# at index 4,5 show NaN but when wo work in numpy , that shows error of broadcasting.