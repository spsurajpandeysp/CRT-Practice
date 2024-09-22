s = "suraj pandey 4944 456 864"

l = s.split(" ")       

maxi = 0


for i in l:
    if i.isdigit() and i.count("9")==0:
        if int(i)>maxi:
            maxi = int(i)


print(maxi)