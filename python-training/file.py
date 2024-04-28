'''
#儲存檔案
file=open("data.txt", mode="w", encoding="utf-8") #開啟
file.write("測試中文\nSecond Line") #操作
file.close() #關閉
'''
'''
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
#讀取檔案
#把檔案中的數字資料，一行一行讀取，計算總和
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)
'''
#使用JSON格式讀取，複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
data["name"]="New Name" #修改變數的資料
#把最新資料複寫回檔案
with open("config.json", mode="w") as file:
    json.dump(data, file)