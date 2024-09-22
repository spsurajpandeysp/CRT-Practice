l = [4,78,3]

i = 0
j=len(l)-1

ans="It is plindrome"

while i<j:
    if(l[i]==l[j]):
        pass
    else:
        ans = "Not plindrome"

    i=i+1
    j=j-1
        
        
print(ans)