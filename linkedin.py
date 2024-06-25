import pandas as pd

# Creating a Series
series = pd.Series([1, 2, 3, 4, 5])
print(series)

# Creating a DataFrame
d = {"a":[1,2,3,4,5], "b":[1,2,3,4,5]}
var1 = pd.DataFrame(d)
print(var1)

# Loading DataFrame
a = pd.read_csv("tips.csv")
a


#--> Data Cleaning Methods
a = pd.read_csv("tips1.csv")
a.dropna()
# drop the  rows with NaN values
a.fillna('fill')
#  NaN values walii be repalced with 'fill'

#--> transforming method
a.replace(to_replace='No', value = 'aqsa')
a.replace("[A-Z]","Python" , regex=True)
a.replace('Female', method='ffill', inplace=True) # change in original data

# Merging method
a = pd.DataFrame({"A": [1, 2, 3,4], "B": [5, 6, 7, 8]})
b = pd.DataFrame({"A": [1, 2, 5, 6], "C": [10, 20, 30, 40]})
pd.merge(a, b, on="A")

# Data Manipulation
b = a.loc[[204, 205], ["total_bill", "sex"]] # to get specific data with loc
print(b)
a.iloc[0,1]# iloc  gives the data of specific location
# Group by
a = pd.DataFrame({"A": ["a", "b", "c", "b", "c",  "d", "a", "a" ],
                  "S_1": [10,11, 12, 10, 11, 12,13, 15],
                  "S_2": [16, 17, 18, 19, 20, 21, 20, 22]})
b = a.groupby("S_1")
for x, y in b:
    print(x)
    print(y)
    print(" ")

# Working with Time series
# Creating a date range
date_range = pd.date_range(start='1/1/2020', periods=5)
print(date_range)

# Converting a column to datetime
df['Date'] = pd.to_datetime(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04'])
print(df)


# Boosting Performancce
# Converting data type
df['Age'] = df['Age'].astype('int32')
print(df.dtypes)
# Vectorized operations
df['Age'] = df['Age'] * 2
print(df)


