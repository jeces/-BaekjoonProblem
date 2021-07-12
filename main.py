bl = []
al = []

def Test():
    a = input()
    for i in range(0, int(a)):
        b = input().split()
        if (int(b[0]) < 1) or (int(b[0]) > 1000):
            return
        c = 0
        count = 0
        res = 0
        for j in range(0, int(b[0])):
            al.append(int(b[j + 1]))
            c += int(b[j+1])
            d = c/int(b[0])
        for k in al:
            if k > d:
                count = count + 1
        res = count / int(b[0]) * 100
        bl.append(round(res, 3))
        #print("{:.3f}%".format(bl[i]))

    for i in range(0, len(bl)):
        print("{:.3f}%".format(bl[i]))

Test()
