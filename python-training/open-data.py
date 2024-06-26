#網路連線

import urllib.request as request
src="https://www.youtube.com/" #yt
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") #台大網站原始碼(HTML、CSS、JS)
print(data)


#串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
#取得公司名稱，列表出來
clist=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")