lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

dic = {}

for item in lst:
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

for key, value in dic.items():
    print(f"{key} : {value}", end=", ")
