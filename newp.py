import random

# Take the input from the user
ui = input("Enter your first version of password: ")

# Strip any leading and trailing spaces
u1 = ui.replace(" ", "")

# Convert the string into a list of characters
char_list = list(u1)

# Shuffle the list randomly
random.shuffle(char_list)

# Join the shuffled characters back into a string
shuffled_string = ''.join(char_list)

# Print the shuffled string
print("Here is your strong password:", shuffled_string)


