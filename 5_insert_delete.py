import pandas as pd
a = pd.DataFrame({"a":[2,4,6,8], "b":[1,2,3,4]})
a.insert(1, "python", a["a"]) #length should be same
# a.insert(1, "python", [2,3,4,5])
a.insert(3, "c", a["a"][:3])
print(a)
# 1
a1 = a.pop('python')
# print(a1)
# 2
del a["c"]
print(a)