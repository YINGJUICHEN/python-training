#例外處理情境:轉換資料型態失敗
#使用者如果輸入的資料格式不能轉成數字，請他重新輸入，直到輸入成功為止
while True:
    data=input("Enter")
    try:
        number = int(data)
        break
    except Exception:
        print("Invalid")
number=number*2
print(number)
