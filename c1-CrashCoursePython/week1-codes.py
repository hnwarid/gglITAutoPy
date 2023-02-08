# These are codes from the practice quizzes and graded assessment.
# Adding answers of multiple choice questions seems unnecessary

# Fill in the correct Python command to put “My first Python program” onto the screen.
print("My first Python program")
# Convert this Bash command into Python:
print("Have a nice day")
# Fill in the correct Python commands to put “This is fun!” onto the screen 5 times.
for i in range(5):
    print("This is fun!")
# Select the Python code snippet that corresponds to the following Javascript snippet:
# for (let i = 0; i < 10; i++) {
#         console.log(i);
#     }
for i in range(10):
    print(i)

# Output a message that says "Programming in Python is fun!" to the screen.
print("Programming in Python is fun!")
# Replace the ___ placeholder and calculate the Golden ratio:  \frac{1+\sqrt{5}}{2} 2 1+ 5 ​ ​ .
# Tip: to calculate the square root of a number xx, you can use x**(1/2).
ratio = (1 + 5 ** 0.5) / 2
print(ratio)

# Write a Python script that outputs "Automating with Python is fun!" to the screen.
print("Automating with Python is fun!")
# Fill in the blanks so that the code prints "Yellow is the color of sunshine".
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)
# Use Python to calculate how many different passwords can be formed with 6 lower case English letters.
# For a 1 letter password, there would be 26 possibilities.
# For a 2 letter password, each letter is independent of the other,
# so there would be 26 times 26 possibilities.  Using this information,
# print the amount of possible passwords that can be formed with 6 letters.
print(26 ** 6)
# Most hard drives are divided into sectors of 512 bytes each.
# Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.
# Note: Your result should be in the format of just a number, not a sentence.
disk_size = 16 * 1024 * 1024 * 1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)
