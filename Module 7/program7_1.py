# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 7 Assignment #1
# Collaborators: None

# program7_1.py
# Program Description: Based on user input: (a) store artist/group names in a list, (b) count how many names was inputted into the program, and (c) in a second function, alphabetically sort these names and display them to the user. 

# Start program.
    # Begin a counter that starts at zero (0) for the total number of artist/group names that the user inputs, which will increase by each input of 'name' for each recurrence of the program's 'while' loop. Assign to variable 'name_count.'
    # Create an empty list for which the artist/group names will be stored by placing two brackets next to each other. Assign to variable 'names.'
    # Prompt the user to enter a group/artist name or type the word 'done' to quit the program ➞ This is known as the 'priming read.'
    # While 'name' does NOT equal string 'done':
        # Call the 'append' method for empty list 'names' for argument 'name' (which is the user's input).
        # Add one (1) to 'name_count' for each reocurence of the 'while' loop. 
        # Continue the loop by re-prompting the user to enter a artist/group name or type the word 'done' to quit the program.
    # Print a statement telling the user how many artist/group names they entered throughout the program's execution.
    # Call the second function, 'my_music' for the argument 'names,' which is the list created in the beginning.
# Define second function 'my_music' for parameter 'names':
    # Sort the list 'names' in ascending (alphabetical) order by calling the 'sort()' method.
    # For any 'name' in list 'names':
        # Print each artist/group name ➞ Notice that we do not use the 'end' operator in this statement because it is not required to print all the names on a single line.
# End program. 
    
def main():
# Set the 'name_count' counter to 0, which will ensure that each artist/group name will be accounted for in the 'while' loop. 
    name_count = 0
# Create an empty list that will later store all of the user's inputted artist/group name. 
    names = []
# Get user's input for the name of an artist/group name, OR give them the option to type 'done' to quit the program. 
    name = input("Please enter the name of the artist/group or type 'done' to quit: ")
# Use a 'while' loop to determine when the program stops appending names to the 'names' list. 
    while name != 'done':
# Call the 'append' function for the 'names' list and write each artist/group name to the list. 
        names.append(name)
# Add 1 to the 'name_count' counter every time the user inputs a name. 
        name_count += 1
# Continue the loop by re-prompting the user to input another artist/group done, OR type 'done' to quit the program. 
        name = input("Please enter the name of the artist/group or type 'done' to quit: ")
# When the loop ceases, display a statement telling the user how many names they put into the program. 
    print('You entered', name_count, 'names.')
# Call the 'my_music' function for argument 'names.'
    my_music(names)
# Define a new function called 'my_music' for parameter 'names.'
def my_music(names):
# Sort list 'names' by calling the 'sort()' method for this list. 
    names.sort()
# Use a 'for' loop to display the random integers within the list's contents ➞ This flow control statement will avoid 'crude dumping.
    for name in names:
# Display each name on a single line, separated  by a single space. 
        print(name)
    
# Call the 'main' function to end the program. 
main()
        
        
    
    
