# Create a list squaring the numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


# Filter out even numbers from an input of numbered list
list_of_strings = input("enter a list of numbers: ").split(',')
# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_ints = [int(n) for n in list_of_strings]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in list_of_ints if num % 2 == 0]
print(result)


# Take numbers from the two text files and return the numbers common in both files
with open("file1.txt") as file1:
    list1 = file1.read().split()

with open("file2.txt") as file2:
    list2 = file2.read().split()

result = [int(num) for num in list1 if num in list2]
print(result)


# Create a dictionary of words and letter length from a sentence input
sentence = input("Enter some sentence(s): ")
result = {word:len(word) for word in sentence.split()}
print(result)


# Convert the dictionary of Celsius input temperatures into a dictionary of Fahrenheit temperatures
weather_c = eval(input())
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)


# For iterating through pandas dataframes:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)