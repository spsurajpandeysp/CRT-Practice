arr = eval(input("Enter array"))


ans = []

i = len(arr)-2

prevMax = int(arr[len(arr)-1])
ans.append(prevMax)
while(i>=0):
    if(prevMax<int(arr[i])):
        ans.append(int(arr[i]))
        prevMax=int(arr[i])

    i=i-1

print(ans[::-1])