subL = []
sem = int(input("Enter number of semesters: "))

for i in range(sem):
    sub = int(input(f"Enter number of subjects in semester {i + 1} :"))
    subL.append(sub)

marksL = []

for x in subL:
    dummy = []
    print("Enter the marks in semester", subL.index(x) + 1 ,":")
    for i in range(x):
        marks = int(input(f"Enter marks obtained in subject {i + 1}: "))
        dummy.append(marks)
    marksL.append(dummy)

for i in range(sem):
    print(f"Maximum mark in semester {i + 1}: {max(marksL[i])}")
