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

# Loop 1 - ask user for next information
while True:
    print("\n---Hello! Please enter your information---")
    # Loop 2 - retry if there is error
    while True:
        try:
    # collect all datas
            full_name = input("Full name: ")
            if full_name == " ":
                break
            
        # store datas in dictionary
            person_info = {}

            person_info["Nickname"] = input("Nickname: ")
            if person_info["Nickname"] == " ":
                break
            person_info["Age"] = (int(input("Age: ")))
            if person_info["Age"] == " ":
                break
            person_info["Address"] = input("Address: ")
            person_info["Birthday"] = input("Birthday: ")
            person_info["Cellphone Number"] = (int(input("Cellphone Number: ")))
            if len(str(person_info["Cellphone Number"])) != 11 or person_info["Cellphone Number"] == " ":
                break
            person_info["Favorite Color"] = input("Favorite Color: ")
            person_info["Hobby"] = input("Hobby: ")
            person_info["Ambition"] = input("What would you like to be in the future?: ")
            person_info["Favorite Food"] = input("Favorite food: ")
            person_info["Favorite Ice Cream Flavor"] = input("Favorite Ice cream flavor: ")
            person_info["Choice"] = input("Books or songs?: ")
            if person_info["Choice"] != "Books":
                break
            elif person_info["Choice"] != "Songs":
                break
            person_info["Pineapple Preference"] = input("Do you like pineapples on pizza? (y/n): ")
            if person_info["Pineapple Preference"] != "y" or person_info["Pineapple Preference"] != "n":
                break
            person_info["Description"] = input("One word to describe yourself: ")
            person_info["Motto"] = input("Motto in life: ")

            print("\nInformation successfully saved!")
            
            retry = input("Do you want to add another person? (y/n): ")
            if retry != "y":    
                continue
            else:
                print("Thank you!")

        except: 
            print("Invalid input, please try again.")    

    
        