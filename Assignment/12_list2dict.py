n = int(input("Enter number of key-value pairs: "))

tuples_list = []

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    tuples_list.append((key, value))

result_dict = dict(tuples_list)

print("Dictionary:", result_dict)
