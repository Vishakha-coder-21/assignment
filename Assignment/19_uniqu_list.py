n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

uniq_list = list(set(numbers))

print(f"Orignal list : {numbers}")

print(f"Unique list : {uniq_list}")