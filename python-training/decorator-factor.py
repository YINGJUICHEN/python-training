#計算1+2+3+...+max的裝飾器工廠
def calculatefactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            callback(total)
        return run
    return calculate

@calculatefactory(100)
def show(result):
    print("結果", result)

@calculatefactory(10)
def showenglish(result):
    print("result is", result)

show()
showenglish()



'''
def myFactory(base):
    def my_decorator(callback):
        def run():
            print("裝飾器內的程式", base)
            result=base*1.5
            callback(result)
        return run
    return my_decorator

@myFactory(3)
def test(result):
    print("普通函式的程式", result)

test()
'''