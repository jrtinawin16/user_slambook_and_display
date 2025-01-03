# ask user about their:
    # full name
    # nickname
    # age
    # address
    # birthday
    # cellphone number
    # favorite color
    # hobby
    # what would they like to be in the future
    # favorite food
    # favorite ice cream flavor
    # books or songs?
    # preference on pineapples on pizza? (yes or no)
    # one word to describe yourself
    # motto in life
# ask user again if they want to enter another set of data

user_info = {}
# Loop 1 - asks user for next input
while True:
    print("\n---Hello! Please enter your information---")
    # Loop 2 - retry if there is error
    while True:
        try:
            while True: # Loop 3 - asks user for full name
                full_name = input("Full name: ")
                if len(full_name.split()) >= 3:
                    break
                else:
                    print("Full name must be at least 3 words.")

            while True: # Loop 4 - asks user for nickname
                nickname = input("Nickname: ")
                if len(nickname.split()) >= 1:
                    break
                else:
                    print("Please enter a nickname.")

            while True: # Loop 5 - asks user for age    
                user_age = int(input("Age: "))
                if user_age >= 0 and user_age <= 100:
                    break
                elif user_age > 100: 
                    print ("Age cannot exceed 100 years old.")
                else:
                    print("Age cannot be lower than zero.")

            while True: # Loop 6 - asks user for address
                user_address = input("Address: ")
                if len(user_address.split()) >= 5:
                    break
                else:
                    print("Address is too short.")

            while True: # Loop 7 - asks user for birthday
                print("Birthday (MM/DD/YYYY): ")
                while True: # Loop 7a - asks user for month in number format
                    month = int(input("Month: "))
                    if month > 0 and month <= 12:
                        break
                    else:
                        print("Invalid month, try again.")
                while True: # Loop 7b - asks user for date
                    date = int(input("Birthdate: "))
                    if date >= 1 and date <= 31:
                        break
                    else:
                        print("Invalid date, try again.")
                while True: # Loop 7c - asks user for year
                    year = int(input("Year: "))
                    if year >= 1924 and year <= 2024:
                        break
                    else:
                        print("Invalid year, try again.")
                user_birthday = f"{month}/{date}/{year}"
                print (f"Birthday: {user_birthday}")
                break

            while True: # Loop 8 - asks user for cellphone number
                user_number = (int(input("Cellphone Number (0 + ..): ")))
                if (len(str(user_number))) == 10:
                    break
                else: 
                    print("Cellphone number must be 11 digits.")
            
            while True: # Loop 9 - asks user for favorite color
                user_color = input("Favorite Color: ")
                common_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray"]
                if user_color in common_colors:
                    break
                else:
                    print("Color is uncommon or invalid.")

            while True: # Loop 10 - asks user for hobby
                user_hobby = input("Hobby: ")
                if len(user_hobby.split()) >= 1: 
                    break
                else:
                    print("Invalid, please enter a hobby.")
            
            while True: # Loop 11 - asks user for ambition
                user_ambition = input("What would you like to be in the future?: ")
                if len(user_ambition.split()) >= 1:
                    break
                else:
                    print("Ambition cannot be blank.")

            while True: # Loop 12 - asks user for favorite food    
                user_favorite_food = input("Favorite food: ")
                if len(user_favorite_food.split()) >= 1:
                    break
                else:
                    print("Favorite food cannot be blank.")

            while True: # Loop 13 - asks user for favorite ice cream flavor        
                user_ice_cream = input("Favorite ice cream flavor: ")
                common_flavors = ["vanilla", "chocolate", "strawberry", "cookies and cream",
                    "rocky road", "double dutch", "coffee", "ube", "cheese", "mango"]
                if user_ice_cream in common_flavors:
                    break
                else: 
                    print("Ice cream flavor is uncommon or invalid.")

            while True: # Loop 14 - asks user if they prefer books or songs        
                user_choice = input("Books or songs?: ")
                if user_choice == "books":
                    break
                elif user_choice == "songs":
                    break
                else:
                    print("Pick only one from the choices.")

            while True: # Loop 15 - asks user if they like pineapples on pizza   
                user_preference = input("Do you like pineapples on pizza? (y/n): ")
                if user_preference == "y": 
                    break
                elif user_preference == "n":
                    break
                else: 
                    print("Invalid answer.")

            while True: # Loop 16 - asks user for a word    
                user_description = input("One word to describe yourself: ")
                if len(user_description.split()) == 1:
                    break
                else: 
                    print("Cannot be blank.")

            while True: # Loop 17 - asks user for their motto
                user_motto = input("Motto in life: ")
                if len(user_motto.split()) >= 3:
                    break
                else:
                    print("Motto is too short.")

            user_info[full_name] = {
                'full_name': full_name,
                'nickname': nickname,
                'user_age': user_age,
                'user_address': user_address,
                'user_birthday': user_birthday,
                'user_number': user_number,
                'user_color': user_color,
                'user_hobby': user_hobby,
                'user_ambition': user_ambition,
                'user_favorite_food': user_favorite_food,
                'user_ice_cream': user_ice_cream,
                'user_choice': user_choice,
                'user_preference': user_preference,
                'user_description': user_description,
                'user_motto': user_motto 
            }        

            print("-------------------------------------")
            print(f"Your information")
            print(f"Full Name: {user_info[full_name]['full_name']}")
            print(f"Nickname: {user_info[full_name]['nickname']}")
            print(f"Age: {user_info[full_name]['user_age']}")
            print(f"Address: {user_info[full_name]['user_address']}")
            print(f"Birthday: {user_info[full_name]['user_birthday']}")
            print(f"Cellphone Number: {user_info[full_name]['user_number']}")
            print(f"Favorite color: {user_info[full_name]['user_color']}")
            print(f"Hobby: {user_info[full_name]['user_hobby']}")
            print(f"Ambition: {user_info[full_name]['user_ambition']}")
            print(f"Favorite food: {user_info[full_name]['user_favorite_food']}")
            print(f"Favorite ice cream flavor: {user_info[full_name]['user_ice_cream']}")
            print(f"Books or songs: {user_info[full_name]['user_choice']}")
            print(f"Like pineapples on pizza: {user_info[full_name]['user_preference']}")
            print(f"One word to describe yourself: {user_info[full_name]['user_description']}")
            print(f"Motto: {user_info[full_name]['user_motto']}")
            print("Information successfully saved!")
            print("-------------------------------------")

            continue_input = input("Do you want to add another person? (y/n): ")
            break
        except: 
            print("Invalid input, please try again.")
            
    if continue_input == "y":
        continue
    elif continue_input == "n":
        with open("personal_data.txt", "a") as file:
            file.write("Collected informations: \n")
            file.write("-------------------------------------\n")
            for name, info in user_info.items():
                file.write(f"Full Name: {info['full_name']}\n")
                file.write(f"Nickname: {info['nickname']}\n")
                file.write(f"Age: {info['user_age']}\n")
                file.write(f"Address: {info['user_address']}\n")
                file.write(f"Birthday: {info['user_birthday']}\n") 
                file.write(f"Cellphone Number: {info['user_number']}\n")
                file.write(f"Favorite color: {info['user_color']}\n")
                file.write(f"Hobby: {info['user_hobby']}\n")
                file.write(f"Ambition: {info['user_ambition']}\n")
                file.write(f"Favorite food: {info['user_favorite_food']}\n")
                file.write(f"Favorite ice cream flavor: {info['user_ice_cream']}\n")
                file.write(f"Books or songs: {info['user_choice']}\n")
                file.write(f"Like pineapples on pizza: {info['user_preference']}\n")
                file.write(f"One word to describe yourself: {info['user_description']}\n")
                file.write(f"Motto: {info['user_motto']}\n")
                file.write("-------------------------------------\n")
                break
        print("Thank you!")
        break
    else:
        print("Invalid, please try again.")
            
        
    
  
    

    
        