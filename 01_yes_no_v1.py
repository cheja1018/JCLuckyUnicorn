# Ask the user of they have played before
show_instructions = input("Have you play this game before? ").lower()

# If they say yes, output program continues
if show_instructions == "yes":
    print("Program continues")

# If they say no, output 'display instructions
elif show_instructions == "no":
    print("display instructions")

# If other, print error
else:
    print("Please answer yes / no")
