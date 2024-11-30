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
                    

                #person_info["Birthday"] = input("Birthday: ")
                #person_info["Cellphone Number"] = (int(input("Cellphone Number: ")))
                #if (len(str(person_info["Cellphone Number"]))) != 11:
                    #break
                person_info["Favorite Color"] = input("Favorite Color: ")
                person_info["Hobby"] = input("Hobby: ")
                person_info["Ambition"] = input("What would you like to be in the future?: ")
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
    

    
        