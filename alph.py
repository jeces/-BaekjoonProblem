sntnce = list(input())
print(sntnce)
alphabet = list(map(chr, range(97,122+1)))

#print(alphabet)b
for i in range(len(alphabet)) :
    if alphabet[i] in sntnce :
        alphabet[i] = sntnce.index(alphabet[i])
    else : alphabet[i] = -1
for i in range(len(alphabet)-1) :
    print(alphabet[i], end=" ")
print(alphabet[len(alphabet)-1])