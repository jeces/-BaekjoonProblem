def hanSu():
    lis = []
    count = 0
    n = input()
    if int(n) > 1000:
        return
    for i in range(1, int(n)+1):
        for j in str(i):
            lis.append(j)
        if int(len(lis)) == 3:
            if int(int(lis[0]) - int(lis[1])) == int(int(lis[1]) - int(lis[2])):
                count = count + 1
        elif int(len(lis)) == 4:
            pass
        else:
            count = count + 1
        lis.clear()
    print(count)

hanSu()