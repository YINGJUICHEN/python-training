import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個Request物件，附加Request Headers的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

print(data)

#解析原始碼，取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser") #讓beautifulsuop協助我們解析HTML格式文件
titles=root.find_all("div", class_="title") #尋找class="title"的div標籤
print(titles) 
for title in titles:
    if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
        print(title.a.string)