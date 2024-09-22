# reverse string
s = input("enter string")
ans=""
for i in s:
  ans=i+ans
print(ans)


# check palendrome
s = input("enter string")
ans=""

i=0
j=len(s)-1

while( i<j):
  if(s[i]==s[j]):
    pass
  else:
    print("No")
    i=i+1
    j=j-1

print("yes")


# remove duplicate



s = input("Enter string")

ans = ""

for i in s:

  if(ans.find(i)>0):
    pass
  else:
    ans=ans+i

print(ans)


# substring in a string
s = input("Enter string")
subStr = s = input("Enter string")

print(s.count(subStr))



# pangram

s = input("Enter string")

ans = "pangram"

for i in s:
  if(i>='a' and i<='z' or i==" " or i>='A' and i<='Z'):
    pass
  else:
    ans = "Not pangram"
    break

print(ans)