# Version 2 - error message included when calling function

def choice_checker(question):

    error = "please choose from rock / paper / sissors (or press xxx to quit)"

    valid = False
    while not valid:

        #ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response
        
        #check for exit code...
        elif response == "xxx":
            return response
        else: print(error)

#main routine goes here

#loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    #ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

    #print out choice for comparison purposes
    print("You Chose {}".format(user_choice))