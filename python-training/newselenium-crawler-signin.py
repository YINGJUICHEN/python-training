# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 設定Edge Driver的執行檔路徑
options = Options()
options.edge_executable_path = "C:\python-training\msedgedriver.exe"

# 建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Edge(options=options)

# 連線到Leetcode登入頁面
driver.get("https://leetcode.com/accounts/login/")

# 輸入帳號密碼，按下登入按鈕
username_input = driver.find_element(By.ID, "id_login")
password_input = driver.find_element(By.ID, "id_password")
username_input.send_keys("560628chen@gmail.com")
password_input.send_keys("qaz2013*")

# 使用WebDriverWait等待登入按鈕可見並可點擊
signin_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signin_btn")))
signin_btn.click()

# 等待登入完成
time.sleep(5)

# 連線到登入後才能取得資料的頁面，並取得想要的資料
driver.get("https://leetcode.com/problemset/")
time.sleep(3)

# 找到顯示問題狀態的元素並列印其文字
status_element = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
print(status_element.text)
columns=status_element.text.split("\n")
print("已完成刷提數量", columns[1])
# 關閉瀏覽器視窗
#driver.close()
