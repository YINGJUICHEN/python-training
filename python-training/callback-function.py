def add(n1, n2, cb):
    cb(n1+n2)

def handle(result):
    print("結果", result)

def handle2(result):
    print("result of add is", result)

add(3, 4, handle)
add(5, 6, handle2)



'''
def test(arg):
    arg("hi") #呼叫回呼函式，帶入參數

#定義一個回呼函式
def handle(da):
    print(da)

test(handle)
'''
