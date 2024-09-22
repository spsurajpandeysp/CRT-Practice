subStr = []
s = set()
def checkPalen(str):
    i=0
    j=len(str)-1
    while(i<j):
        if str[i]!=str[j]:
            return False
        i=i+1
        j=j-1
    return True
        

def subStr(str):
 
    for i in range(0,len(str)):
        temp=""
        for j in range(i,len(str)):
            temp+=str[j]
            # print(temp)
            # # print(checkPalen(temp))
            if(checkPalen(temp)):
                s.add(temp)


# subStr("abaaa")
subStr("geek")


print(len(s))