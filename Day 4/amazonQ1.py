s = "ycce"
t = "ycsscece"

s = "h5c"
t = "h4c"

i = 0
j= 0



count=0

if(len(s)<len(t)):
    count = len(t)-len(s)
elif(len(s)>len(t)):
    count = len(s)-len(t)

else:
    while(i<len(s) and j<len(t)):
        if(s[i]==t[j]):
            pass
        else:
            count=count+1

        i=i+1
        j=j+1






print(count)