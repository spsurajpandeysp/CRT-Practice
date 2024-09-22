def reverse(num):
    rev = 0

    while(num>0):
        last = num%10
        rev=rev*10+last
        num=num//10
    
    return rev


def plinNum(num):
    rev = 0
    temp = num
    while(num>0):
        last = num%10
        rev=rev*10+last
        num=num//10
    
    return rev

    if(temp==num):
        print("It is palinDrome:")
    else:
        print("Not palindrome")

def fact(num):
    ans=1;
    while num>0:
        ans=ans*num
        num=num-1
    
    return ans



def armstrong(n):
    l = len(str(n))
    sum=0
    while n>0:
        last = n%10
        sum=sum+last**l
        n=n//10


    return sum

