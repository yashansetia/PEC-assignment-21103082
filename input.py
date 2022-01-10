#Ques1:calculate average of three numbers
print("Give three numbers to calculate average")
num1 =float(input("a="))
num2 =float(input("b="))
num3 =float(input("c="))
avr =(num1 +num2 +num3)/3
print("average of given numbers is",avr)

#Question2: Compute a person's income tax
#All values are in $
Gross_income = float(input("Enter your gross income($)="))

Standard_deduction =10000

Dependent_deduction =3000 #deduction on each dependent
dependents =int(input("Enter number of dependents="))

Taxable_income=Gross_income-Standard_deduction-(Dependent_deduction*dependents)

print("Your Taxable income is",Taxable_income)

#Tax Rate=20%
Tax=Taxable_income*0.2
print("Your Tax is",Tax)

#Ques3: Store different type of data in list
sid=input("Enter SID: ")
name=input("Enter Name: ")

gender=input("Enter Gender(M(male),F(female),U for unknown)")

course=input("Enter course name: ")
cgpa=float(input("Enter CGPA"))

student=[sid,name,gender,course,cgpa]

print(student)

# Ques4: enter marks of 5 students into a list and display them in sorted manner

Marks = []
for i in range(5):
    print("Enter Marks", i + 1, ": ", end="")
    x = int(input())
    Marks.append(x)
Marks.sort()  # Sorting the marks list
print("Sorted Order Of Marks : ", Marks)

#Ques5(a):Print a specified list
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color.remove('Black')
print("color:", Color)

#Ques5(b): Print a specified list
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Color[3:5] = ['Purple']  # Replacing Black and Pink with Purple
print("color :", Color)


