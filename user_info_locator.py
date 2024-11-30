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

except:
    print("An error occured.")