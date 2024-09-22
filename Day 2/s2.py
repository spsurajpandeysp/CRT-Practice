n = int(input("Enter Number: "))
occ = int(input("Enter digit: "))

count=0

while n>0:
    last = n%10
    if(last==occ):
        count+=1
    n=n//10

print(count)
