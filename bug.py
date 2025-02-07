def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 0 as designed

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 3.0 as designed

my_list = [1,2,'a',4,5]
result = calculate_average(my_list) #This will throw an error
print(f"The average is: {result}")