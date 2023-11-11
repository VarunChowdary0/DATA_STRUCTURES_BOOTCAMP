# Basic-> Pass-Fail
# 3 - subject marks PASS or FAIL
Marks =[]
Pass = True
for i in range(3):
    Marks_ = int(input(f"Enter MARKS{i+1}: "))
    Marks.append(Marks_)
PassMarks = int(input("Enter Pass Marks: "))
for i in range(3):
    if(Marks[i]>PassMarks):
        continue
    else:
        Pass = False
        break
if(Pass):
    print("Pass")
else:
    print("Nice Try")


