'''
import pandas as pd
#讀取資料
data = pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
#讀取資料
print(data)
'''

import pandas as pd
import chardet

# 读取文件并检测编码
with open("googleplaystore.csv", 'rb') as f:
    result = chardet.detect(f.read())

# 获取检测到的编码
encoding = result['encoding']

# 使用检测到的编码读取 CSV 文件
data = pd.read_csv("googleplaystore.csv", encoding=encoding)

# 觀察資料
print("資料數量",data.shape)
print("資料欄位", data.columns)
print("-------------------------")
'''
# 分析資料:評分的各種統計數據
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("前100個應用程式的平均", data["Rating"].nlargest(100).mean())
'''

# 將評分數據轉換為數字，將無效值轉換為NaN
data["Rating"] = pd.to_numeric(data["Rating"], errors='coerce')
'''
# 計算評分的各種統計數據
print("平均數:", data["Rating"].mean())
print("中位數:", data["Rating"].median())
print("前100個應用程式的平均評分:", data["Rating"].nlargest(100).mean())
'''
'''
print(data["Rating"].dtype)
print(data["Rating"].describe())
#data = data[(data["Rating"] >= 0) & (data["Rating"] <= 5)]

condition=data["Rating"]<=5
data = data[condition]
print(data)

print("平均數:", data["Rating"].mean())
print("中位數:", data["Rating"].median())
print("前1000個應用程式的平均評分:", data["Rating"].nlargest(1000).mean())
'''
#分析資料:安裝數量的各種統計數據
'''
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", "").replace("Photography", "").replace("Paid", ""))
print("平均數", data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數大於100000的應用程式有幾個", data[condition].shape[0])
'''
#基於資料的應用:關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword, case=False) #忽視大小寫
print("包含慣見字的應用程式資料", data[condition].shape[0])