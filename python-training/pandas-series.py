#載入panda模組
import pandas as pd
#資料索引
data=pd.Series([5,6,-8,9,4], index=["a", "b", "c", "d", "e"])
'''
print(data)

'''
#觀察資料
'''
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)
'''
#取得資料:根據順序、根據索引
'''
print(data[2], data[0])
print(data["e"], data["d"])
'''
#數字運算:基本、統計、順序
'''
print("最大值", data.max())
print("總和", data.sum())
print("標準差", data.std())
print("中位數", data.median())
print("最大的三個數", data.nlargest(3))
print("最小的三個數", data.nsmallest(3))
'''

data=pd.Series(["你好", "Python", "Pandas"])
#字串運算:基本、串接、搜尋、取代
print(data.str.lower())
print(data.str.len())
print(data.str.cat(sep="、"))
print(data.str.contains("P"))
print(data.str.replace("你好", "hello"))
