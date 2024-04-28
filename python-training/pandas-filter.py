#載入pandas模組
import pandas as pd
#篩選練習-Series
'''
data=pd.Series([30,15,20])
condition=data>18
print(condition)
filteredData=data[condition]
print(filteredData)
'''
'''
data=pd.Series(["你好","Python","Pandas"])
condition=data.str.contains("P")
print(condition)
filteredData=data[condition]
print(filteredData)
'''
#篩選練習-DataFrame
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charlie"],
    "salary":[30, 50, 40]
})
#print(data)
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)

