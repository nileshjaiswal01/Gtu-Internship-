#1. Calculate area of a rectangle. .(Formula :- L*B)

l = float(input("Enter the value of l : "))
b = float(input("enter the value of b : "))
print(l*b) 

#2. Calculate area of a square.(Formula :- L*L)

l = float(input("Enter the value of l : "))
print(l**2) 

#3. Calculate area of a circle.(Formula :- pi*r*r)

pi = 3.14 
r = float(input("Enter the value of r : "))
print(pi*r*r)

#4. Calculate average of 5 numbers. (Formula :- (n1+n2+n3+n4+n5)/5)

n1 = 10
n2 = 20
n3 = 30
n4 = 40
n5 = 50
print(n1+n2+n3+n4+n5/5)

#5. Calculate Simple interest.(Formula :- (p*r*t)/100).

p = float(input("Enter the value of principle amount : "))
r = float(input("enter the value of rate of interest  : "))
t = float(input("Enter the value of time in months : "))
sp = (p*r*t/100)
print(sp)

# 6. Take any three numbers and find their squares and cubes.

a = 10 
b = 5
c = 4
print(a**2,b**2,c**2)
print(a**3,b**3,c**3)

# 7. Write a program to enter the temperature in Fahrenheit and convert it to Celsius.[C = ((F-32)*5)/9]

C = float(input("Enter the temperature in Celsius : "))
F = C + 273 
print( F-32 *5/9)

# 8. Check whether number is even or odd.

a = float(input("Enter the Number : "))
if a%2==0:
    print("it is even number")
else:
    print("it is odd number")

# 9. Take a year and check whether it is leap year or not.

a  = int(input("Enter the Year : "))
if a%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")


# 10. Write a program to enter two numbers and find the smallest out of them. Use conditional operator.

a = float(input("Enter the value of a : "))
b = float(input("enter the value of b : "))
if a < b :
    print("a is the smallest ")
else:
    print("b is the smallest")

# 11. Take a number and check whether it is zero, positive or negative.

a = float(input("Enter the number"))
if a==0 :
    print("it is zero ")
elif a > 0 :
    print("it is positive")
else:
    print("it is negative")

# 12. Take 2 numbers and display greatest number. (Number can be equal).

a = float(input("Enter the number :"))
b = float(input("Enter the number :"))

if a==b:
    print("number is same enter different number")
elif a > b:
    print("a is greatest")
else:
    print("b is greatest")

# 13. Take age and whether it is less than 18 or not. If it is less than 18 then print not eligible for vote.

a = float(input("Enter the age : "))
if   a < 18:
    print("you are not eligible for vote")
else:
    print("you are  eligible for vote ")

# 14. Write a program to check whether the blood donor is eligible or not for donating blood. The conditions laid down are as under. Use if statement.
# • Age should be above 18 year but not more than 55 year.

a = float(input("Enter the number : "))
if a > 18 and a <55:
    print("you are eligible for  blood donation ")
else: 
    print("you are not eligible for blood donation")

# 15. Take 2 numbers and find smallest number.

a = float(input("Enter the number :"))
b = float(input("Enter the number :"))
if a < b :
    print("a is the smallest")
else:
    print("b is the smallest")


# 16. Write a program to find the maximum from given three numbers (Without using Nested if, or Logical Operator, Or Conditional operators).

a = float(input("Enter the number 1 :"))
b = float(input("Enter the number 2 :"))
c = float(input("Enter the number 3 :"))

max = 0 
if a > max:
    max = a
if b > max :
    max = b
if c > max :
    max = c
print(max)


# 17. Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

a = float(input("Enter the number :"))
if a < 100 :
    print("the number is less than 100")
elif a > 100:
    print("the number is not less than 100 ")
if a%2==0:
    print("it is even")
else:
    print("it is odd")

# 18. Take a number to print the square of a number if it is less than 10.

a = float(input("Enter the number : "))
if a < 10 :
    print(f"square of number is {a} = {a**2}")

# 19. Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

a = float(input("Enter the number : "))
if a >= 0 :
    
    if a==0 :
        print(" it is zero ")
    else :
     print("it is positive ")
else:
   print("it is negative")

# 20. Take 3 numbers and find greatest number using nested IF….ELSE statement.

a = float(input("Enter the number 1 : "))
b = float(input("Enter the number 2 : "))
c = float(input("Enter the number 3 : "))

if a >= b :
  
    if a >= c :
     greatest = a
    else:
       greatest = c

else:

    if b >= c :
       greatest = b
    else:
       greatest = c
print(f"the number is greatest {greatest} : ")


# 21. Take 3 numbers and find smallest number using logical operator

a = float(input("Enter the number 1 : "))
b = float(input("Enter the number 2 : "))
c = float(input("Enter the number 3 : "))

if a<b and a < c :
    print("number 1  is the smallest")
elif b<c:
    print("number 2 is the smallest")
else:
    print("number 3 is the smallest")

# 22. Take a number and find factorial of that number.

a = int(input(" Enter the number  : ",))
factorial = 1
for i in reversed(range( 1 , a + 1 ,1)):
 factorial = factorial*i
print(f"the factorial of {a} : {factorial} ",)
 


# 23. Write a program to swap 2 numbers using third variable.

a = int(input(" Enter the number  : ",))
b = int(input(" Enter the number  : ",))
print(f"number {a},{b} before swap")
temp = a
a = b
b= temp
print(f"number {a},{b} after swap")

# 24. Take a number. Generate multiplication table of that number

a = int(input(" Enter the number for multiplication table  : ",))
for i in range(1,11):
 print(f" {a} * {i } = ", a * i)
 i = i +1 

# 25. Take a number and calculate sum of natural numbers.


a = int(input(" Enter the number  : ",))
num = 0
for i in range(1,1+a,1):
    num = num + i
print(f"the natural number  of  {a} is  : {num} ")

# 26. Take a number. If number is 1 then print Monday, 2 then print Tuesday and so on….

day = int(input(" Enter the number  : ",))

match day:
    case 1:
        print("monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednesday")
    case 4 :
        print("thursday")
    case 5 :
        print("friday")
    case 6 :
        print("saturday")
    case 7 :
        print("sunday")
      
    

# 27. Take a number between 1 to 12.If number is 1 then print January, 2 then print February and so on… (Use switch case)

month = int(input("enter the month number : "))

match month:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("octomber")
    case 11:
        print("november")
    case 12:
        print("December")

# 28. The ABC Insurance Company Ltd. Offers the following three categories of car insurance policy to car owners:
# • Category A, here the basic premium is calculated as 2% of the car’s value.
# • Category B, here the basic premium is calculated as 3% of the car’s value.
# • Category C, here the basic premium is calculated as 5% of the car’s value.



# 29. Make a simple calculator using switch case.
# 1.Addition
# 2.Subtraction
# 3.Multiplication
# 4.Division


num1 = float(input("enter the number : "))
operator = input("enter operator(+,-,*,/): ")
num2 = float(input("enter the number : "))
match operator:
    case "+":
       result = num1 + num2
       print(result)
    case "-":
       print(num1-num2)
    case "*":
       print(num1*num2)
    case"/":
       print(num1/num2)
    

# 30. Take 5 numbers and calculate average. According to that percentage print grade.
# • If average <50 then Grade is F. 
# • if average >=50 <60 then Grade is D. 
# • if average >=60 <70 then Grade is C. 
# • if average >=70 <80 then Grade is B. 
# • if average >=80 <90 then Grade is A. 
# • if average >=90 then Grade is A+


subject = ["CNS","AI","ML","DAV","SE"]
mark =[]

for i in range(0,5):
   marks = float(input(f" enter the marks of {subject[i]} : "))
   mark.append(marks)
total = sum(mark)
f = total/ 5
print(f"The total avg is : ",total)
if f <= 100 and f >= 90:
   print("Get A+ grade")
elif f < 90 and f >= 80:
   print("Get A grade")
elif f < 80 and f >= 70:
   print("Get B grade")
elif f < 70 and f >= 60:
   print("Get C grade")
elif f < 60 and f >= 50:
   print("Get D grade")
else:
   print("Get F grade")