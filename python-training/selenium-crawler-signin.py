#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

#設定Edge Driver的執行檔路徑
options=Options()
options.edge_executable_path="C:\python-training\msedgedriver.exe"
#建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Edge(options=options)
#連線到Leetcode登入頁面
driver.get("https://leetcode.com/accounts/login/")
#輸入帳號密碼，按下登入按鈕
usernameinput = driver.find_element(By.ID, "id_login")
passwordinput = driver.find_element(By.ID, "id_password")
usernameinput.send_keys("560628chen@gmail.com")
passwordinput.send_keys("az2013*")
signinbtn=driver.find_element(By.ID, "signin_btn")
signinbtn.send_keys(Keys.ENTER)
#等待登入完成
time.sleep(100)
#連線到登入後才能取得資料的頁面，並取得想要的資料
driver.get("https://leetcode.com/problemset/")
time.sleep(3)
statelement=driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
print(statelement.text)
driver.close()

