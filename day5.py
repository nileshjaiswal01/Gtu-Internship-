# 1) functions 

def dosum(a,b,c):
    d = (a+b+c)
    return d

def doavg(total):
    d = total/300
    return d

no1 = float(input("enter the number : "))
no2 = float(input("enter the number : "))
no3 = float(input("enter the number : "))

sumans = dosum(no1,no2,no3)
print(sumans)

avgans = doavg(sumans)
print(avgans)

# 2) print the number 10 to 1

def callmeback(no):
    if no > 0:
        print(no)
        no = no-1
        callmeback(no)

callmeback(10)

# 3) to create file

myfile = open("nilesh.txt","a")
myfile.write("hello ")
myfile.close

myfile2 = open("nilesh.txt","r")
data = myfile.read()
print(data)
myfile.close