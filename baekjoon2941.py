string = input()
def rem(str):
    ss = ["c-", "c=", "dz=", "d-", "lj", "nj", "s=", "z="]
    count = 0
    for i in ss:
        if str.find(i) != -1:
            count += str.count(i)
            str = str.replace(i, " ")
    str = str.replace(" ", "")
    count = len(str) + count
    print(count)

rem(string)