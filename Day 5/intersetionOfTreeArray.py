
arr1 = [1,2,3]
arr2 = [2,3,4]
arr3 = [3,4,5]


ans=[]

for x in arr1:
    if arr2.count(x) and arr3.count(x):
        arr1.remove(x) 
        arr2.remove(x)
        arr3.remove(x)

        ans.append(x)


print(ans)