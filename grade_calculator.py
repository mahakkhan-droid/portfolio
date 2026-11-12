print("====STUDENT GRADE CALCULATOR====")


name=input("Enter student name : ")


S1=float(input("Enter marks in subject 1: "))
S2=float(input("Enter marks in subject 2: "))
S3=float(input("Enter marks in subject 3: "))
S4=float(input("Enter marks in subject 4: "))
S5=float(input("Enter marks in subject 5: "))


total=S1+S2+S3+S4+S5


percentage=total/5


print("\n====RESULT====")


print("Student Name : ",name)
print("Total Marks : ",total,"/ 500")
print("Percentage : ",percentage,"%")


if percentage>=90:
    print("Grade : A+")
elif percentage>=80:
    print("Grade : A")
elif percentage>=70:
    print("Grade : B")
elif percentage>=60:
    print("Grade : C")
elif percentage>=40:
    print("Grade : D")
else:
    print("Grade : Fail")

