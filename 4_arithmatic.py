import pandas as pd
a = pd.DataFrame({"a":[2,4,6,8], "b":[1,2,3,4]})
a["c"] = a["a"] + a["b"]
# print(a)
a["d"] = a["c"]>=5
print(a)