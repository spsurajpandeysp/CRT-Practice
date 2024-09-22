# anagram

s1 = input("Enter string 1")
s2 = input("Enter string 2")

ans="Yes"

s1.upper()
s2.lower()


for x in s1:
  if(s2.count(x)==s1.count(x)):
    pass
  else:
    ans = "No"
    


print(ans)