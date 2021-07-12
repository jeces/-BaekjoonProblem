lis = list(map(chr, range(65, 91)))
count = 0
for i in input():
    if i != 'S' and i != 'V' and i != 'Y' and i != 'Z':
        count += lis.index(i)//3 + 3
    elif i == 'S':
        count += 8
    elif i == 'V':
        count += 9
    else:           # YZ
        count += 10
print(count)