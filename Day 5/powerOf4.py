n = int(input("Enter value of x: "))
ans="Yes"
temp = n
while(n>=1):
    if(n%4!=0 and n!=1):
        ans="No"
    n=n//4



print(ans)

    