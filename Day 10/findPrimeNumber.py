n = 4
m = 30


def checkPrime(n):
   
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    


    return True

count=0
for i in range(n,m+1):
    if checkPrime(i) and checkPrime(i+6):
        count+=1



print(count)