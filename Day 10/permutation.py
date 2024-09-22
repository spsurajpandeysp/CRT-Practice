from itertools import permutations
a = 459
b = 500
s = str(a)
ans = permutations(s)
l = [''.join(p) for p in ans]
print(l)

ans = l




mini  = 43232342232

for x in ans:
    if b<int(x) and mini>int(x):
        mini = int(x)


print(mini)