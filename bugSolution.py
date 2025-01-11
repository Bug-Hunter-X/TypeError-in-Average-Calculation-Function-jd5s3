def calculate_average(numbers):
    if not numbers:
        return 0
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List contains non-numeric values.")
        return None

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10, 20, 'a']
result = calculate_average(my_list) #This will print error message and return None