#Iterable 資料型態
#字串、列表、集合、字典

#for迴圈
#for 變數名稱 in 可疊代的資料:
'''
dic={"a":3, "x":5}
for key in {"a":3, "x":5}:
    print(key)
    print(dic[key])
'''
#內建函式
#max(可疊代資料)
'''
result=max([10, 2, 30, 1])
print(result)
result=max("mdfkmgr")
print(result)
result=max((5,92,88,74))
print(result)
result=max({"x":3,"a":5}) #看字典中的key
print(result)
'''

#sorted(可疊代資料)
result=sorted("cab")
print(result)
result=sorted({10,99,8,-98,-5})
print(result)


