s = input("Enter String: ")
i=0
ans=""
while i<len(s):
  count = s.count(s[i])
  if(count>1):
    ans+=s[i]+str(count)
  else:
    ans+=s[i]
  i+=count

print(ans)