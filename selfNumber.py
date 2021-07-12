numBer = []

def selfNumber(num):
    res = 0
    for i in str(num):
        res += int(i)
    num = num + res
    return num

def listNumber():
    for i in range(1, 10001):
        numBer.append(str(i))

def checkNumber():
    for i in range(1, 10001):
        r = selfNumber(int(i))
        if r < 10001:
            if str(r) in numBer:
                numBer.remove(str(r))
        r = 0
    for i in numBer:
        print(i)

listNumber()
checkNumber()