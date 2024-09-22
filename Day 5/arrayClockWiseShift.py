# l=[1,2,3,4,5,6]

# l=[10,20,30,40,50]
# k = 2
n = int(input("Enter value of n"))
l=eval(input("Enter List"))
k = int(input("Enter value of k"))


k = k%len(l)




for i in range(0,k):
    x = l.pop()
    l.insert(0,x)
print(l)

# or

# print(l[k:len(l)],l[0:k])