import math 

n = int(input("Enter number of list item: "))

l=[]

for i in range(n):
    l.append(int(input()))

sum=0

for i in range(n-1):
    sum+=math.abs(l[i]-l[i+1])

print(sum)
