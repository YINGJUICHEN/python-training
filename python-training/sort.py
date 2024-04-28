import random
import math
import sys

# 計算合併排序所需的記憶體空間
def mergeSortMemory(arr):
    if len(arr) < 2:
        return arr
    
    middle = math.floor(len(arr) / 2)
    left, right = arr[:middle], arr[middle:]
    
    # 遞迴排序左右兩半
    left_sorted = mergeSortMemory(left)
    right_sorted = mergeSortMemory(right)
    
    # 合併左右兩半並計算額外記憶體空間
    merged = merge(left_sorted, right_sorted)
    return merged

# 合併操作並計算額外記憶體空間
def merge(left, right):
    result = []
    
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    
    return result

# 產生隨機列表
random_list = random.sample(range(1, 10001), 10000)

# 計算排序前的記憶體使用量
memory_before = sys.getsizeof(random_list)

# 呼叫合併排序函式
sorted_list = mergeSortMemory(random_list)

# 計算排序後的記憶體使用量
memory_after = sys.getsizeof(sorted_list)

# 計算記憶體花費
memory_spent = memory_after - memory_before

print("Memory usage before sorting:", memory_before, "bytes")
print("Memory usage after sorting:", memory_after, "bytes")
print("Memory spent during sorting:", memory_spent, "bytes")


import random
import sys

def shellSort(arr):
    # 計算排序前的記憶體使用量
    memory_before = sys.getsizeof(arr)
    
    import math
    
    gap = 1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    
    # 計算排序後的記憶體使用量
    memory_after = sys.getsizeof(arr)
    
    # 計算記憶體花費
    memory_spent = memory_after - memory_before
    
    return memory_spent

# 產生隨機列表
random_list = random.sample(range(1, 10001), 10000)

# 執行希爾排序並獲取記憶體花費
memory_spent = shellSort(random_list)

print("Memory spent during shell sort:", memory_spent, "bytes")
