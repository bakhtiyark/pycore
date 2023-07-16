pencil_number = int(input("How many pencils would you like to use:"))
name_x = "John"
name_y = "Jack"
first_person = input(f"Who will be the first ({name_x}, {name_y}):")
print("|" * pencil_number)
while(pencil_number>0):
    if(first_person !=  name_x):
        print(name_y + "'s turn:")
        removal = int(input())
        pencil_number -= removal
        print("|" * pencil_number)
        first_person = name_x
    else:
        print(name_x + "'s turn:")
        removal = int(input())
        pencil_number -= removal
        print("|" * pencil_number)
        first_person = name_y