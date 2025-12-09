numbers = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = min(numbers)
numbers.remove(smallest)

second_smallest = min(numbers)
print("Second smallest number is:", second_smallest)

# Also done by sort()