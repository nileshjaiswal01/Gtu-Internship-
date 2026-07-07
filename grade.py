subject = ["AI","CNS","DE","SE","ML"]
mark = []
for i in range(0,5):
    marks = float(input(f"Enter the {subject[i]} marks "))
    mark.append(marks)
failed = False 
for i in range(len(mark)):
   if mark[i] < 33:
    print(f"you fail in the {subject[i]}" )
    failed = True
    

total = sum(mark)
f = total / 5
if failed :
    print("you are fail")
else:
    total = sum(mark)
    f = total / 5
    print(f"The total avg is :",f)
    if f <= 100 and f >= 90:
        print("Get A grade")
    elif f < 90 and f >= 80:
        print("Get B grade")
    elif f < 80 and f >= 70:
        print("Get c grade")
    elif f < 70 and f >= 60:
        print("Get c grade")
    elif f < 50 and f >= 40:
        print("Get c grade")
    else:
        print("Fail")