# The create_python_script function creates a new python script in the current working directory,
# adds the line of comments to it declared  by the 'comments' variable,
# and returns the size of the new file. Fill in the gaps to create a script called "program.py".
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        filesize = file.write(comments)
    return filesize


print(create_python_script("program.py"))

# The new_directory function creates a new directory inside the current working directory,
# then creates a new empty file inside the new directory, and returns the list of files in that directory.
# Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
import os


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # Create the new file inside the new directory
    os.chdir(directory)  # change working dir to directory
    with open(filename, 'w') as file:
        file.write("")

    os.chdir("..")  # change working dir back to original dir
    # Return the list of files in the new directory
    return os.listdir(directory)


print(new_directory("PythonPrograms", "script.py"))

# The file_date function creates a new file in the current working directory,
# checks the date that the file was modified, and returns just the date portion
# of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create
# a file called "newfile.txt" and check the date that it was modified.
import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        file.write("")
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    timestamp = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return (
        "{}".format(timestamp.strftime("%Y=%m-%d")))  # https://www.programiz.com/python-programming/datetime/strftime


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


# The parent_directory function returns the name of the directory that's located
# just above the current working directory. Remember that '..' is a relative path
# alias that means "go up to the parent directory". Fill in the gaps to complete this function.
import os


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    # relative_parent = os.path.join(os.getcwd(), "..") # /home/..
    relative_parent = os.path.abspath('..')  # /

    # Return the absolute path of the parent directory
    return relative_parent


print(parent_directory())

# We're working with a list of flowers and some information about each one.
# The create_file function writes this information to a CSV file.
# The contents_of_file function reads this file into records and returns the information
# in a nicely formatted block. Fill in the gaps of the contents_of_file function
# to turn the data in the CSV file into a dictionary using DictReader.
import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)
        # Process each item of the dictionary
        # return_string = reader # this returns <csv.DictReader object at 0x......>
        for row in reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))


# Using the CSV file of flowers again, fill in the gaps of the contents_of_file
# function to process the data without turning it into a dictionary.
# How do you skip over the header record with the field names?
import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Read the rows of the file
        reader = csv.reader(file)
        # Process each row
        for row in list(reader)[1:]:
            name, color, types = row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(name, color, types)
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
