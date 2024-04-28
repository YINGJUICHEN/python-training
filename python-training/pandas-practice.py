#載入pandas模組
import pandas as pd
#建立Series
data=pd.Series([20,10,15])
#基本Series操作
'''
print(data)

print("Max", data.max())
print("Median", data.median())
data=data*2
print(data)

data=data==20
print(data)
'''
#建立DataFrame
data=pd.DataFrame({
    "name":["Apple", "Banana", "Candy"],
    "salary":[3000, 5000, 4000]
})
#基本DataFrame操作
'''
print(data)

print(data["salary"])
'''
#取得特定的列
print(data)
print("------------------")
print(data.iloc[0])