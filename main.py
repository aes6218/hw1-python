# Author: August Sanderson aes6218@psu.edu

p1 = 0
p2 = 0
p3 = 0

class1 = input("Enter your course 1 letter grade: ")
if class1.lower()=="a" or class1.lower()=="a+":
    p1 = 4.0
elif class1.lower()=="a-":
    p1 = 3.67
elif class1.lower()=="b+":
    p1 = 3.33
elif class1.lower()=="b":
    p1 = 3.0
elif class1.lower()=="b-":
    p1 = 2.67
elif class1.lower()=="c+":
    p1 = 2.33
elif class1.lower()=="c":
    p1 = 2.0
elif class1.lower()=="d":
    p1 = 1.0
else:
    p1 = 0.0
credit1 = float(input("Enter your course 1 credit: "))
print(f"Grade point for course 1 is: {p1}")

class2 = input("Enter your course 2 letter grade: ")
if class2.lower()=="a" or class2.lower()=="a+":
    p2 = 4.0
elif class2.lower()=="a-":
    p2 = 3.67
elif class2.lower()=="b+":
    p2 = 3.33
elif class2.lower()=="b":
    p2 = 3.0
elif class2.lower()=="b-":
    p2 = 2.67
elif class2.lower()=="c+":
    p2 = 2.33
elif class2.lower()=="c":
    p2 = 2.0
elif class2.lower()=="d":
    p2 = 1.0
else:
    p2 = 0.0
credit2 = float(input("Enter your course 2 credit: "))
print(f"Grade point for course 2 is: {p2}")

class3 = input("Enter your course 3 letter grade: ")
if class3.lower()=="a" or class3.lower()=="a+":
    p3 = 4.0
elif class3.lower()=="a-":
    p3 = 3.67
elif class3.lower()=="b+":
    p3 = 3.33
elif class3.lower()=="b":
    p3 = 3.0
elif class3.lower()=="b-":
    p3 = 2.67
elif class3.lower()=="c+":
    p3 = 2.33
elif class3.lower()=="c":
    p3 = 2.0
elif class3.lower()=="d":
    p3 = 1.0
else:
    p3 = 0.0
credit3 = float(input("Enter your course 3 credit: "))
print(f"Grade point for course 3 is: {p3}")

print(f"Your GPA is: {(p1*credit1 + p2*credit2 + p3*credit3)/(credit1+credit2+credit3)}")