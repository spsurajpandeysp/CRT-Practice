

l = [0,1,0,3,12]

for x in l:
    if x ==0:
        l.remove(x)
        l.append(x)
print(l)