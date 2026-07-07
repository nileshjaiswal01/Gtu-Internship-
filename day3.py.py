numbers = []

for i in range(5):
    num = int(input(f"enter the number { i+1 } : "))
    numbers.append(num)


for i in range(5):
    for j in range (i+1,5):
        if numbers[i] > numbers [j]:
            numbers[i],numbers[j] = numbers[j],numbers[i]

print("number is in ascending order :")

for num in numbers:
  print(num)

