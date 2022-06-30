
show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user of they have played before
    show_instructions = input("Have you play this game before? ").lower()

    # If they say yes, output program continues
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program continues")

    # If they say no, output 'display instructions
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    # If other, print error
    else:
        print("Please answer yes / no")

    print("You chose {}" .format(show_instructions))
