# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#write to file with or without changes
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

#create a new file using the same command 
with open("my_new_file.txt", mode="w") as file:
    file.write("\nNew text.")