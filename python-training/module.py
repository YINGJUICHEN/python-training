
#載入內建的sys模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

#建立geometry模組，載入使用
import geometry.line
result=geometry.line.len(1,1,5,5)
print(result)
import geometry.line
result=geometry.line.slope(1,2,5,6)
print(result)

#調整搜尋模組的路徑
import sys
sys.path.append("modules") #在模組的搜尋路徑列表中(新增路徑)
print(sys.path) #印出模組路徑列表
print("----------------")
import geometry.line
print(geometry.line.len(1,1,5,5))
