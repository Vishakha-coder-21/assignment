#  Write a Python program to get a single string from two given strings, separated by
# a space and swap the first two characters of each string.

f_name = input("Enter 1st name : ")
l_name = input("Enter last name : ")

full_name = f_name +" " + l_name

print(full_name)

print("---After swapping 2 charecter ---")

new_str1 = l_name[:2] + f_name[2:]
new_str2 = f_name[:2] + l_name[2:]

# Combine into single string
result = new_str1 + " " + new_str2
print(result)