n = int(input("Enter value of n"))
l1 = eval(input("Enter array one"))
l2 = eval(input("Enter array Two"))



l1 = sorted(l1)
l2 = sorted(l2)

ans = 1 




for i in range(0,n):
    if l1[i]!=l2[i]:
        ans=0
print(ans)