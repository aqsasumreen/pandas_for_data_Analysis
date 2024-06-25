import pandas as pd
l = [2,3,4,5,6]
var = pd.DataFrame(l)
# print(var)
# print(type(var))

d = {"a":[1,2,3,4,5], "b":[1,2,3,4,5]}
# var1 = pd.DataFrame(d)
# print(var1)

# to check particular coulmn
var2 = pd.DataFrame(d, columns =['a'] )
# print(var2)

# particular index pr
var3 = pd.DataFrame(d)
# print(var3["a"][3])

# create through series
a = {"a":pd.Series([1,2,3,4]), "b":pd.Series([1,2,3,4])}
var4 = pd.DataFrame(a)
print(var4)