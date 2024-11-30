try:
    search_name = input("Please enter full name to search: ")
    with open ("personal_data.txt", "r") as file:
        lines = file.readlines()
        user_info = {}
        for line in lines

except:
    print("An error occured.")