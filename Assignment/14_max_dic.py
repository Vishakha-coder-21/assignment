n = int(input("Enter number of items: "))
my_dict = {}

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value


top_3 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 highest values:", top_3)
