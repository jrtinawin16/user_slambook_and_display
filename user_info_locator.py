try:
    search_name = input("Please enter full name to search: ")
    with open ("personal_data.txt", "r") as file:
        lines = file.readlines()
        user_info = {}
        for line in lines:
            if line.strip() == "-------------------------------------":
                if user_info:
                    user_info[user_info["full_name"]] = user_info
                user_info = {}
                continue
            line = line.strip()
            if line.startswith("Full_name: "):
                user_info['full_name'] = line.split("|")[1].strip()
            elif line.startswith("Nickname: "):
                user_info['nickname'] = line.split("|")[1].strip()
            elif line.startswith("Age: "):
                user_info['user_age'] = line.split("|")[1].strip()
            elif line.startswith("Address: "):
                user_info['user_address'] = line.split("|")[1].strip()
            elif line.startswith("Birthday: "):
                user_info['user_birthday'] = line.split("|")[1].strip() 
            elif line.startswith("Cellphone Number: "):
                user_info['user_number'] = line.split("|")[1].strip()   
            elif line.startswith("Favorite color: "):
                user_info['user_color'] = line.split("|")[1].strip() 
            elif line.startswith("Hobby: "):
                user_info['user_hobby'] = line.split("|")[1].strip()  
            elif line.startswith("Ambition: "):
                user_info['user_ambition'] = line.split("|")[1].strip()   
            elif line.startswith("Favorite food: "):
                user_info['user_favorite_food'] = line.split("|")[1].strip() 
            elif line.startswith("Favorite ice cream flavor: "):
                user_info["user_ice_cream "] = line.split("|")[1].strip() 
            elif line.startswith("Books or songs: "):
                user_info['user_choice'] = line.split("|")[1].strip()    
            elif line.startswith("Like pineapples on pizza: "):
                user_info['user_preference'] = line.split("|")[1].strip()   
            elif line.startswith("One word to describe yourself: "):
                user_info['user_description '] = line.split("|")[1].strip()
            elif line.startswith("Motto: "):
                user_info['user_motto'] = line.split("|")[1].strip()                                

except:
    print("An error occured.")