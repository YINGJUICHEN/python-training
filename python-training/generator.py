#定義建立生成器涵式
'''
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 10
#呼叫並回傳生成器
gen=test()

#搭配for迴圈使用

for d in gen:
    print(d)
'''

def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGenerator=generateEven(100)
for data in evenGenerator:
    print(data)
