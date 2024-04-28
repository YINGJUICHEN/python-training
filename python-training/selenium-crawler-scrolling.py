#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
#設定Chrome Driver的執行檔路徑
options = Options()
options.chrome_executable_path="C:\python-training\msedgedriver.exe"
#建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Edge(options=options)
#連線到Linkedin工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0") #捲動視窗到底部
#捲動視窗並等待瀏覽器在入更多內容
n=0
while n<3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # 等待3秒
    n+=1
#取得網頁中的工作標題
titletags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titletag in titletags:
    print(titletag.text)



