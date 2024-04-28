#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.edge.options import Options
#設定Chrome Driver的執行檔路徑
options = Options()
options.edge_executable_path = 'C:\python-training\msedgedriver.exe'
#建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Edge(options=options)
driver.maximize_window() #視窗最大化
driver.get('https://www.google.com/')
driver.save_screenshot("screenshot_google.png") #網頁截圖
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screenshot_ntu.png")
driver.close()
