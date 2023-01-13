# These are codes from all the practice quizzes.
# Adding answers of multiple choice questions seems unnecessary

# The is_palindrome function checks if a string is a palindrome.
# A palindrome is a string that can be equally read from left to right or right to left,
# omitting blank spaces, and ignoring capitalization.
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for _ in input_string.lower():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if _.isalpha():
            new_string += _
            reverse_string = _ + reverse_string
    print(new_string)
    print(reverse_string)

    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


# Using the format method, fill in the gaps in the convert_distance function
# so that it returns the phrase "X miles equals Y km",
# with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


# Fill in the gaps in the nametag function so that it uses the format method
# to return first_name and the first initial of last_name followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))


# Should display "Jean-Luc G."


# The replace_ending function replaces the old string in a sentence with the new string,
# but only if the sentence ends with the old string.
# If there is more than one occurrence of the old string in the sentence,
# only the one at the end is replaced, not all of them. For example,
# replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
# The string comparison is case-sensitive,
# so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


# Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames,
# consisting of the new filenames. Fill in the blanks in the code using
# any of the methods you’ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for file in filenames:
    old_name = file.split(".")
    if old_name[1] == "hpp":
        old_name[1] = 'h'
    newfilenames.append(".".join(old_name))

print(newfilenames)


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Let's create a function that turns text into pig latin: a simple text transformation
# that modifies each word moving the first character to the end
# and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:] + word[0] + "ay" + " "
        # Turn the list back into a phrase
    return say.strip()


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# The permissions of a file in a Linux system are split into three sets of three permissions:
# read, write, and execute for the owner, group, and others. Each of the three values can be
# expressed as an octal number summing each permission, with 4 corresponding to read,
# 2 to write, and 1 to execute. Or it can be written with a string using the letters
# r, w, and x or - when the permission is not granted. For example: 640 is read/write
# for the owner, read for the group, and no permissions for the others; converted to a string,
# it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute
# for group and others; converted to a string, it would be: "rwxr-xr-x"
# Fill in the blanks to make the code convert a permission in octal format into a string format.
def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for _ in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if _ >= value:
                result += letter
                _ -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


# The group_list function accepts a group name and a list of members,
# and returns a string with the format: group_name: member1, member2, …
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
# Fill in the gaps in this function to do that.
def group_list(group, users):
    members = ",".join(users)
    return "{}: {}".format(group, members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


# The guest_list function reads in a list of tuples with the name, age,
# and profession of each party guest, and prints the sentence
# "Guest is X years old and works as __." for each one. For example,
# guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out:
# Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer.
# Fill in the gaps in this function to do that.
def guest_list(guests):
    for guest in guests:
        name, age, job = guest
        print("{} is {} years old and works as {}".format(name, age, job))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


# The email_list function receives a dictionary, which contains domain names as keys,
# and a list of users as values. Fill in the blanks to generate a list
# that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(f"{user}@{domain}")
    return emails


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]
     }))


# The groups_per_user function receives a dictionary, which contains group names with the list
# of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary
# with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group_name, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            user_groups[user] = user_groups.get(user, []) + [group_name]
    # groups for this user, creating the entry
    # in the dictionary if necessary

    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))

# The dict.update method updates one dictionary with the items coming from the other dictionary,
# so that existing entries are replaced and new entries are added.
# What is the content of the dictionary “wardrobe“ at the end of the following code?
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)


# The add_prices function returns the total price of all of the groceries in the  dictionary.
# Fill in the blanks to complete this function.
def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for price in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
