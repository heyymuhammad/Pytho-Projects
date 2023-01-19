##LIST COMPREHENSION

## For loop
# numbers  = [1, 2, 3, 4]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

## String in list 
# name = "Angela"
# letter_list = [letter for letter in name]
# print(letter_list)

## Using Range
# double_integers = [n *2 for n in range(1,5)]
# print(double_integers)

## Using IF Statement
# even_numbers = [n for n in range (1, 11) if n%2 == 0]
# print(even_numbers)

## Using .upper() function
# names = ["Jhon", "Steve", "Shawn", "Rick", "Flora"]
# names_range_5 = [name.upper() for name in names if len(name) == 5]
# print(names_range_5)


## DICTIONARY COMPREHENSION

## Example #1
# dict = {
#      "Name": "Muhammad",
#      "Age": 17,
#      "Proffession": "DevOps Engineer"
# }

# new_dict = {key:value for (key,value) in dict.items() if key == "Age"}
# print(new_dict)

## Example #2
# import random

# names = ["Maggie", "Carl", "Rick", "Shawn", "Millie"]

# student_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student:score for (student,score) in student_score.items() if score >= 60}

# print(passed_students)

## Dict into dataframes

# import pandas

# student_dict = {
#     "student": ["Rick", "Maggie", "Carl"],
#     "score": [56, 77, 89]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


## Loop through rows of a dataframes
# for (index, row ) in student_data_frame.iterrows():
#     print(row.score)


## PHONETIC WORDS

import pandas
data = pandas.read_csv("./day-26-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
