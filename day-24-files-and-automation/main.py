# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# for open function, modes are read (default), write ("w"), append ("a")

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
