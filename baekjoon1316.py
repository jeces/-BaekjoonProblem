def check(string):
    li = []
    global count
    for i in range(len(string)):
        if i == 0:
            li.append(string[i])
        elif li[-1] != string[i]:
            li.append(string[i])
    if len(li) == len(set(li)):
        count += 1

cou = input()
count = 0
for i in range(int(cou)):
    strings = list(map(str, input()))
    check(strings)

print(count)




