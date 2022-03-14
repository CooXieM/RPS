# Version 3 - checks that response is in a given list

def choice_checker(question, valid_list, error):


    valid = False
    while not valid:

        #ask user for choice (and put choice in lowercase)
        response = input(question).lower()
        # Iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        #output error if item not in list
        print(error)
        print()

#main routine goes here

# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

#loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    #ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list, "please choose from rock / paper / scissors (or type xxx to quit")

    #print out choice for comparison purposes
    print("You Chose {}".format(user_choice))