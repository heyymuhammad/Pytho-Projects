# with open("day-24-start/letter-naming/Input/Names/invited_names.txt") as names:
#     names_content = names.read()
# lines = names_content.splitlines()
# each_name = {}

 
# for line in lines:
#     with open(f"day-24-start/letter-naming/Output/ReadyToSend/letter_to_{line}.txt", mode="w") as final_letter:
#         letter_to_send = final_letter.write(f"""Dear {line},\nYou are invited to my birthday this Saturday.\nHope you can make it!\nAngela""")
       
    
#Second Method
PLACEHOLDER = "[name]"


with open("day-24-start/letter-naming/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("day-24-start/letter-naming/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"day-24-start/letter-naming/Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
