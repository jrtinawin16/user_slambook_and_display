user_info = {}
try:
    search_name = input("Please enter full name to search: ").strip()
    with open ("personal_data.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        user_data = {}

        for line in lines:
            if line.strip() == "-------------------------------------":
                if user_data:
                    user_data[user_info['full_name']] = user_data
                user_data = {}
                continue
            if line.lower().startswith(search_name.lower() + " : "):
                data = line.strip().split(" : ")
                user_data['full_name'] = data[0]
                user_data['nickname'] = data[1]
                user_data['user_age'] = data[2]
                user_data['user_address'] = data[3]
                user_data['user_birthday'] = data[4]
                user_data['user_number'] = data[5] 
                user_data['user_color'] = data[6] 
                user_data['user_hobby'] = data[7] 
                user_data['user_ambition'] = data[8]  
                user_data['user_favorite_food'] = data[9] 
                user_data["user_ice_cream "] = data[10] 
                user_data['user_choice'] = data[11]    
                user_data['user_preference'] = data[12]   
                user_data['user_description '] = data[13]
                user_data['user_motto'] = data[14]
                break
            else:
                print("Person not found.")  
except:
    print("An error occured.")

if user_info:
    print("\nInformation Found")
    for name, info in user_info.items():
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

