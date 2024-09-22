l = int(input("Enter left:"))
r = int(input("Enter Right"))

freq = [0,0,0,0,0,0,0,0,0,0]

def findPrime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

for i in range(l,r+1):
    if(findPrime(i)):
        n = i
        while n>0:
            last = n%10
            freq[last]+=1
            n=n//10

maxi = 0

i=len(freq)-1
while(i>=1):
    x = freq[i]
    if maxi<x:
        maxi = x
        ans = i
    i=i-1

print(ans)