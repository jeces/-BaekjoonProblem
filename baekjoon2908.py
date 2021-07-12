string = list(map(str, input().split()))
if ''.join(reversed(string[0])) > ''.join(reversed(string[1])):
    print(''.join(reversed(string[0])))
else:
    print(''.join(reversed(string[1])))