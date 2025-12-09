n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)


unique_values = []
for num in numbers:
    if num not in unique_values:
        unique_values.append(num)

print("Original list:", numbers)
print("Unique values:", unique_values)

"""
2nd way : using set 
- create list - convert to set so duplicate remove - convert list
"""