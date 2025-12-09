n = int(input("Enter number of items: "))
my_dict = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value

ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Ascending Order:", ascending)
print("Descending Order:", descending)
