#隨機模組
import random
#隨機選取

data=random.sample([1,5,6,10,20],3)
print(data)

#隨機調換順序(洗牌)

data=[1,5,8,20]
random.shuffle(data)
print(data)

#隨機取得亂數

data=random.uniform(60, 100) #0-1隨機亂數
print(data)

#取得常態分配亂數
#平均數100，標準差10，多數90-110
#data=random.normalvariate(100, 10)
#平均數0，標準差5，多數-5~5

data=random.normalvariate(0, 5)
print(data)

#統計模組
import statistics as stat
data=stat.stdev([1,4,5,8,100,101,102,103,104])
print(data)

