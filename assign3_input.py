#QUESTION1: Count occurence in a string

a=str(input("ENTER ANY STRING: "))

list=a.split()                #To split all the elements of string in a list
dict={}                       #initializing an empty dictionary
if list.__len__()==1:         #if a single word is entered by user
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                         #else when more than a word is entered by user
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict) 


#QUESTION2: Print Next Date Entered By User

from subprocess import list2cmdline

def Next_Date():
    list1=[1,3,5,7,8]
    list2=[2]
    list3=[4,6,9,11]
    list4=[12]
    while(True):                 #while loop is used so that if any wrong value is entered ,then values will be entered again
        date=int(input("Enter The Date: "))
        if(1<=date<=31):
            break
        else:
            print("Please Enter a valid Date")
    while(True):                  #while loop is used so that if any wrong value is entered  then values will be entered again
        month=int(input("Enter The Month: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):                #while loop is used so that if any wrong value is entered  then values will be entered again
        year=int(input("Enter The Year(1800-2500): "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(date==31):
            date=1
            month=month+1
            print(date,"/",month,"/",year)
        elif(date<31):
            date+=1
            print(date,"/",month,"/",year)
        else:
            print("Wrong Information, Enter Again")
            Next_Date()
    
    elif month in list3 :
        if(date==30):
            date=1
            month=month+1  
            print(date,"/",month,"/",year)   
        elif(date<30):
            date+=1
            print(date,"/",month,"/",year)
        else:
            print("Wrong Information, Enter Again") 
            Next_Date()      
    elif month in list2:
        if(year % 4 == 0):  
            if(date==29):
                date=1
                month=month+1
                print(date,"/",month,"/",year)
            elif(date<29):
                date+=1
                print(date,"/",month,"/",year)
            else:
                print("Wrong Information, Enter Again")
                Next_Date()
        else:
            if(date==28):
                date=1
                month+=1
                print(date,"/",month,"/",year)
            elif(date<28):
                date+=1
                print(date,"/",month,"/",year)
            else:
                print("Wrong Information, Enter Again")
                Next_Date()
    elif month in list4:
        if(date==31):
            date=1
            month=1
            year+=1  
            print(date,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print(date,"/",month,"/",year)
        else:
            print("Wrong Information, Enter Again") 
            Next_Date()
        
    else:
        print("Wrong Information, Enter Again")
        Next_Date()
Next_Date()


#QUESTION3:Create a List of tuples

input_list = input("Enter elements for a list(space between them):") #Take input from user for first element in list
user_list = input_list.split()

print('list: ', input_list             # Print list

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])   # Convert each item to int type
square_list =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(square_list)


#QUESTION4:Print Grade and Performance

def input_grade():
    grade = int(input("Enter Grade Point(int): "))
  
    if grade>10 or grade<4:  #Checking Conditions
        print("Error!! Grade out of Range")
        grade = input_grade()
    return grade
grade=input_grade()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")


#QUESTION5:Print in Certain sequence

alpha = 6
for i in range(alpha):              # printing Empty spaces
    for j in range(i):
        print(' ', end='')          # printing Required alphabets
    for j in range(2*(alpha-i)-1):
        print(chr(65 + j), end='')
#ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()



#QUESTION6:Perform Operations on Dictionary

sid = int(input("Enter SID: "))
name = input("Enter corresponding Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
        
print("<a>",students)

#part b. sort acc to the names

print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs

print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID

sid = int(input("Search Name with SID: "))
print("<d>",students[sid])


#QUESTION7

def recur_fibo(n):         #  Function to display the Fibonacci sequence
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter The Number of terms in the Series: "))
if no_of_terms <= 0:       # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("Average of Series is",avg)

#QUESTION8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)

