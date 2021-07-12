string = list(map(str, input().lower()))
count={}
lis = []
check = ''
for i in string:
    try: count[i] += 1
    except: count[i] = 1
max_key = max(count.values())

for key ,value in count.items():
    if value == max_key:
        lis.append(key)
        check = key

if len(lis) > 1:
    print('?')
else:
    print(check.upper())
