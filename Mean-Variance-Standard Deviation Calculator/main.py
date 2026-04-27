from mean_var_std import calculate

# ask user for input
user_input = input("Enter 9 numbers separated by spaces: ")

# convert string → list of integers
numbers = list(map(int, user_input.split()))

# call function and print result
print(calculate(numbers))