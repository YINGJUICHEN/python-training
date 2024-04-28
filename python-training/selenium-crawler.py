#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
#設定Chrome Driver的執行檔路徑
options=Options()
options.edge_executable_path="C:\python-training\msedgedriver.exe"
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Edge(options=options)
#連線到PTT股票版
#取得股票版中的標題
driver.get("https://www.ptt.cc/bbs/Stock/index5002.html")
#print(driver.page_source) #取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME, "title") #搜尋class屬性是title的所有標籤
for tag in tags:
    print(tag.text)
#取得上一頁的文章標題
link=driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click() #模擬使用者點擊標籤
tags=driver.find_elements(By.CLASS_NAME, "title") #搜尋class屬性是title的所有標籤
for tag in tags:
    print(tag.text)
driver.close()
