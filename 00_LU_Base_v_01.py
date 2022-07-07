# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # Print the error
            else:
                print(error)

        except ValueError:
            print(error)


# main Routine goes here...
played_before = yes_no("Have you play this game before?   ")

if played_before == "no":
    instructions()

print("Programs Continues")

how_much = num_check("How much would you"
                     " like to play with?   ", 0, 10)
print("You will be spending ${}".format(how_much))
