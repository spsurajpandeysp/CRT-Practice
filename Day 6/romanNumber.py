dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}



def solve(n):
    temp = 1
    ans = ""
    while(n>0):
        last = n%10
        n=n//10

        num = last*temp
        temp=temp*10

        if dict[temp]:
            ans+=dict[temp]
        else:
            if num>1000:
                ans=ans+'M'+temp[]

    return ans



solve(1994)