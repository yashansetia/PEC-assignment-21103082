#QUESTION1:Recursive Python Function to solve the Tower Of Hanoi

def towerofhanoi(n,source,destination,auxiliary):
#For Base Case
     if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
#For f(n-1)
     towerofhanoi(n-1,source,auxiliary,destination)
     print("Move disk",n,"from source",source,"to destination",destination)
#For Showing f(n) works using f(n-1)
     towerofhanoi(n-1,auxiliary,destination,source)

n=3
towerofhanoi(n,'A','C','B')

#Question2: Pascal Triangle

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("USING LOOPS")
print("USING FOR LOOP")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")                                                  #for spacing
	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	                                                                # for new line
print("\n\n")

print("USING WHILE LOOP")

i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')
    #first number is always 1
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")

#Question3:

a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))
Quotient=a//b
Remainder=a%b
print("Quotient:",Quotient)
print("Remainder:",Remainder)

#part <a>
print("<a> Checking if the quotient and remainder is a callable value or not:")
print(callable(Quotient))
print(callable(Remainder))
#part <b>
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")
#part <c>
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")
#part <d>
setresult = set(result)
print("<d> Set:",setresult)
#part <e>
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutableSet)
#part <f>
print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))

#Question4:
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("The Object is destroyed")
#creating object
student1 = Student("Yashan", 21103082)
print("Object is created")
#printing the assigned values
print("Name of the student is",student1.name,"and SID is",student1.roll_no,)
#deleting object
del student1
       
#Question5:

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):                                                     
        print("Name is",self.name,"and salary is",str(self.salary),)
    def __del__(self):
         print("The record of",self.name,"is deleted")

employee1=employee('Mehak',40000)
employee1.display()

employee2=employee('Ashok',50000)
employee2.display()

employee3=employee('Viren',60000)
employee3.display()
#Update salary of employee1(Mehak)
print("<A>Updated:",end='')
employee1.salary=70000
employee1.display()
#Delete the info for employee3(Viren)
print("<B>",end='')
del employee3

#Question6:

#inputing a word from the first friend
word =input("Enter the word: ")
word=word.lower()
#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")
    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
