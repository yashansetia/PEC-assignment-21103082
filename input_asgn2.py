#Question1

string1 = "Python is a case sensitive language"

print("(a)Length of string is",len(string1))  #Find Length of string

print("(b)The reverse string is",string1[-1::-1]) #Reverse the order of string

string2=string1[10:26] # Store "a case sensitive" in another string

string2.replace("a case sensitive","object oriented") #Replace "a case sensitive" With "object oriented"

print("(e)The index of substring a is ",string1.find('a')) #Find index of substring “a”

print("(f)The Original String After Removing Whitespaces is",string1.replace(" ","")


#Question2

#Get Information From User
Name = str(input("Enter Your Name "))
SID  = int(input("Enter Your SID "))
Department=str(input("Enter Your Department "))
CGPA = float(input("Enter Your CGPA "))

print("Hey,%s"%Name,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%Department,"and my CGPA is %f"%CGPA)


#Question3

a=56
b=10

print("(a)Value of a&b=",a&b)
print("(b)value of a|b=",a|b)
print("(c)value of a^b=",a^b)
print("(d)value of a after left shifting 2 bits is",a<<2)
print("   value of b after left shifting 2 bits is",b<<2)
print("(e)value of a after right shifting 2 bits is",a>>2)
print("   value of b after right shifting 4 bits is",b>>2)


#Queation4:Print the Greatest of Three Numbers

#get three numbers from users
a=int(input("num1="))
b=int(input("num2="))
c=int(input("num3="))

if a>=b>=c or a>=c>=b:
  Greatest=a
elif b>=a>=c or b>=c>=a:
  Greatest=b
elif c>=a>=b or c>=b>=a:
  Greatest=c
  

#Print Greatest of Three Numbers
print("Greatest of three numbers is",Greatest)

#Question5

#Take input from user
string=input("Enter a string ")
if (string.find('name') !=-1):
    print ("Yes")
else:
    print ("No")


#Question6

#Take length of sides from user
a=int(input("Enter First side of Triangle "))
b=int(input("Enter Second side of Triangle "))
c=int(input("Enter Third side of Triangle "))
if(a>(b+c)):
    print("No")
elif(b>(a+c)):
    print("No")
elif(c>(a+b)):
    print("No")
else:
    print("Yes")