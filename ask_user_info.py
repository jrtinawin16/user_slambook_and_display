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
                    print("Please enter an ambition.")
                    
                person_info["Favorite Food"] = input("Favorite food: ")
                person_info["Favorite Ice Cream Flavor"] = input("Favorite Ice cream flavor: ")
                person_info["Choice"] = input("Books or songs?: ")
                #if person_info["Choice"] != "books":
                    #break
                #elif person_info["Choice"] != "songs":
                    #break
                person_info["Pineapple Preference"] = input("Do you like pineapples on pizza? (y/n): ")
                #if person_info["Pineapple Preference"] != "y" or person_info["Pineapple Preference"] != "n":
                    #break
                person_info["Description"] = input("One word to describe yourself: ")
                person_info["Motto"] = input("Motto in life: ")

                print("\nInformation successfully saved!")
                #continue_input = input("Do you want to add another person? (y/n): ")
                #break
            
        except: 
            print("Invalid input, please try again.")
    
        #if continue_input == "y":    
            #continue
        #elif continue_input == "n":
            print("Thank you!")
            break
        #else:
            print("Invalid input, please try again.")
    

    
        