user_info = {}
try:
    with open ("personal_data.txt", "r") as file:
        lines = file.readlines()
        user_data = {}
        for line in lines:
            line = line.strip()
            if line == "-------------------------------------":
                if user_data:
                        user_info[user_data["full_name"]] = user_data
                user_data = {}
                continue

            if line.startswith("Full name: "):
                user_data['full_name'] = line.split(":", 1)[1].strip()
            elif line.startswith("Nickname: "):
                user_data["nickname"] = line.split(":")[1].strip()
            elif line.startswith("Age: "):
                user_data["user_age"] = line.split(":")[1].strip()
            elif line.startswith("Address: "):
                user_data["user_address"] = line.split(":")[1].strip()
            elif line.startswith("Birthday: "):
                user_data["user_birthday"] = line.split(":")[1].strip()
            elif line.startswith("Cellphone number: "):
                user_data["user_number"] = line.split(":")[1].strip()
            elif line.startswith("Favorite Color: "):
                user_data["user_color"] = line.split(":")[1].strip()
            elif line.startswith("Hobby: "):
                user_data["user_hobby"] = line.split(":")[1].strip() 
            elif line.startswith("Ambition: "):
                user_data["user_ambition"] = line.split(":")[1].strip()   
            elif line.startswith("Favorite food: "):
                user_data["user_favorite_food"] = line.split(":")[1].strip()
            elif line.startswith("Favorite ice cream flavor: "):
                user_data["user_ice_cream"] = line.split(":")[1].strip()
            elif line.startswith("Books or songs: "):
                user_data["user_choice"] = line.split(":")[1].strip()
            elif line.startswith("Like pineapples on pizza: "):
                user_data["user_preference"] = line.split(":")[1].strip()
            elif line.startswith("One word to describe yourself: "):
                user_data["user_description"] = line.split(":")[1].strip()
            elif line.startswith("Motto: "):
                user_data["user_motto"] = line.split(":")[1].strip()
        if user_data:
            user_info[user_data['full_name']] = user_data
        else:   
            print("Person not found.")  
except:
    print("An error occured.")
if len(user_info) > 0:
    while True:
        try:
            search_name = input("Please enter full name to search: ").strip()
            if search_name in user_info:
                print("\nInformation Found")
                data = user_info[search_name]
                print(f"Full Name: {data['full_name']}")
                print(f"Nickname: {data['nickname']}")
                print(f"Age: {data['user_age']}")
                print(f"Address: {data['user_address']}")
                print(f"Birthday: {data['user_birthday']}")
                print(f"Cellphone Number: {data['user_number']}")
                print(f"Favorite color: {data['user_color']}")
                print(f"Hobby: {data['user_hobby']}")
                print(f"Ambition: {data['user_ambition']}")
                print(f"Favorite food: {data['user_favorite_food']}")
                print(f"Favorite ice cream flavor: {data['user_ice_cream']}")
                print(f"Books or songs: {data['user_choice']}")
                print(f"Like pineapples on pizza: {data['user_preference']}")
                print(f"One word to describe yourself: {data['user_description']}")
                print(f"Motto: {data['user_motto']}")
            else: 
                print ("Invalid, try again.")
        except:
            print ("Person cannot be found, try again.")

