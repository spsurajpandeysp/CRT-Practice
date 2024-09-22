
l = [5,2,8,3,1,9,4]

k=3

freq = []

maxi = max(l)

for i in range(0,maxi+1):
    freq.append(0)


for i in l:
    freq[i]=1

ans = []

for i in range(len(freq)):
    if freq[i]==1:
        ans.append(i)


print(ans)

print(ans[k-1])