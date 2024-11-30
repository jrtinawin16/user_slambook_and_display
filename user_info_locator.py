user_info = {}
try:
    with open ("personal_data.txt", "r") as file:
        lines = file.readlines()
        user_data = {}
        for line in lines:
            if line in lines:
                if line.strip() == "-------------------------------------":
                    if user_info:
                        user_info[user_data["full_name"]] = user_info
                    user_data = {}
                    continue
                line = line.strip()
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
                user_info[user_data['full_name']]
        else:   
            print("Person not found.")  
except:
    print("An error occured.")
if len(user_info) > 0:
    while True:
        try:
            search_name = input("Please enter full name to search: ").strip()
            if search_name in user_info == 'full_name':
                user_data = user_info["full_name"]
                print("\nInformation Found")
                print(f"Full Name: {user_info['full_name']}")
                print(f"Nickname: {user_info['nickname']}")
                print(f"Age: {user_info['user_age']}")
                print(f"Address: {user_info['user_address']}")
                print(f"Birthday: {user_info['user_birthday']}")
                print(f"Cellphone Number: {user_info['user_number']}")
                print(f"Favorite color: {user_info['user_color']}")
                print(f"Hobby: {user_info['user_hobby']}")
                print(f"Ambition: {user_info['user_ambition']}")
                print(f"Favorite food: {user_info['user_favorite_food']}")
                print(f"Favorite ice cream flavor: {user_info['user_ice_cream']}")
                print(f"Books or songs: {user_info['user_choice']}")
                print(f"Like pineapples on pizza: {user_info['user_preference']}")
                print(f"One word to describe yourself: {user_info['user_description']}")
                print(f"Motto: {user_info['user_motto']}")
            else: 
                print ("Invalid, try again.")
        except:
            print ("Person cannot be found, try again.")

