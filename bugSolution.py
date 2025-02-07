def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 0 as designed

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 3.0 as designed

my_list = [1,2,'a',4,5]
result = calculate_average(my_list) #This will return 3.0 as designed
print(f"The average is: {result}") 