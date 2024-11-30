try:
    search_name = input("Please enter full name to search: ")
    with open ("personal_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.lower().startswith(search_name.lower() + " | "):
                line = line.strip().split(" | ")
                user_info = {}
                
                user_info['full_name'] = line[0]
                user_info['nickname'] = line[1]
                user_info['user_age'] = line[2]
                user_info['user_address'] = line[3]
                user_info['user_birthday'] = line[4]
                user_info['user_number'] = line[5] 
                user_info['user_color'] = line[6] 
                user_info['user_hobby'] = line[7] 
                user_info['user_ambition'] = line[8]  
                user_info['user_favorite_food'] = line[9] 
                user_info["user_ice_cream "] = line[10] 
                user_info['user_choice'] = line[11]    
                user_info['user_preference'] = line[12]   
                user_info['user_description '] = line[13]
                user_info['user_motto'] = line[14]
                break
            else:
                print("Person not found.")  
except:
    print("An error occured.")
tr
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

except:
    print("An error occured.")