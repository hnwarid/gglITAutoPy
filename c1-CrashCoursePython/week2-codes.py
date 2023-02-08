# These are codes from the practice quizzes
# Adding answers of multiple choice questions seems unnecessary

# In this scenario, two friends are eating dinner at a restaurant.
# The bill comes in the amount of 47.28 dollars.
# The friends decide to split the bill evenly between them,
# after adding 15% tip for the service.
# Calculate the tip, the total amount to pay, and each friend's share,
# then output a message saying
# "Each person needs to pay: " followed by the resulting number.
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
print(f"Each person needs to pay: {share}")

# This code is supposed to take two numbers,
# divide one by another so that the result is equal to 1,
# and display the result on the screen. Unfortunately,
# there is an error in the code.
# Find the error and fix it, so that the output is correct.
numerator = 10
denominator = 10
result = numerator / denominator
print(result)

# Combine the variables to display the sentence "How do you like Python so far?"
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1, word2, word3, word4, word5, word6, word7)

# This code is supposed to display "2 + 2 = 4" on the screen, but there is an error.
# Find the error in the code and fix it, so that the output is correct.
print("2 + 2 =", (2 + 2))


# This function converts miles to kilometers (km).
# 1. Complete the function to return the result of the conversion
# 2. Call the function to convert the trip distance from miles to kilometers
# 3. Fill in the blank to print the result of the conversion
# 4. Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is ", my_trip_km)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is", my_trip_km * 2)


# note: the above code works but the answer told me I was supposed to use str() function:
# Not quite. Remember to use the str() function to convert
# numbers into strings when printing them with text, and to
# call the function with just one parameter, then accept the
# return value into a new variable.

# This function compares two numbers and returns them in increasing order.
# 1. Fill in the blanks, so the print statement displays the result of the function call in order.
# Hint: if a function returns multiple values, don't forget to store these values in multiple variables
# This function compares two numbers and returns them in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


# Let's revisit our lucky_number function.
# We want to change it, so that instead of printing the message, it returns the message.
# This way, the calling line can print the message, or do something else with it if needed.
# Fill in the blanks to complete the code to make it work.
def lucky_number(name):
    number = len(name) * 9
    string = "Hello " + name + ". Your lucky number is " + str(number)
    return string


print(lucky_number("Kay"))
print(lucky_number("Cameron"))


# Complete the script by filling in the missing parts. The function receives a name,
# then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

# What’s the output of this code if number equals 10?
# if number > 11:
#   print(0)
# elif number != 10:
#   print(1)
# elif number >= 20 or number < 12:
#   print(2)
# else:
#   print(3)
# the answer is 2...

# Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100?
# Replace the plus sign in the following code to let Python check it for you and then answer.
print("A dog" > "A mouse")
print(9999 + 8888 > 100 * 100)


# If a filesystem has a block size of 4096 bytes,
# this means that a file comprised of only one byte will still use 4096 bytes of storage.
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return block_size * full_blocks


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
