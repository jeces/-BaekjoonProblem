count = input()
li = []
for i in range(0, int(count)):
    string = input().split()
    a = list(map(str, string[1]))
    st = ""
    for j in a:
        st += j*int(string[0])
    li.append(st)

for i in li:
    print(i)