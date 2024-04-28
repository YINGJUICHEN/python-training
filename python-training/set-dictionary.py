#集合的運算
'''
s1={3,4,5}
print(3 in s1)
'''
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集
s3=s1|s2 #聯集
s3=s1-s2 #差集
s3=s1^s2 #反交集
print(s3)

s=set("Hello") #set(字串)
print(s)

#字典的運算 

dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])

dic={"apple":"蘋果","bug":"蟲蟲"}
print("apple" not in dic) #判斷key是否存在

dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic)
del dic["apple"] #刪除字典中的鍵值對
print(dic)

dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)