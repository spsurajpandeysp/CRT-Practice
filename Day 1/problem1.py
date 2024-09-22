#Accept 9 digit and find  of 1st and last in 2step

a = input("Enter nUmber")
if len(a)==9:
    print(int(int(a[0])+int(a[-1])))
else:
    print("number is not 9 digit")