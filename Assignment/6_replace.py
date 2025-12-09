def replace_not_poor(s):
    not_index = s.find("not")
    poor_index = s.find("poor")

    if not_index >= 0 and poor_index >= 0 and not_index < poor_index:
        return s[:not_index] + "good" + s[poor_index + 4:]
    else:
        return s

user_string = input("Enter a sentence: ")
result = replace_not_poor(user_string)
print("Output:", result)
