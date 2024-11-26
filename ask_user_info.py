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
while True:
    print("\n---Hello! Please enter your information---")

    # collect all datas
    full_name = input("Full name: ")
    if full_name == " ":
        print ("Invalid, please re-enter your name")
            
    # store datas in dictionary
    person_info = {}

    person_info["Nickname"] = input("Nickname: ")
    person_info["Age"] = int(input("Age: "))