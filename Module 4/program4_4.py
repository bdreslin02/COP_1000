# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 4 Assignment
# Collaborators: None

# program4_4.py
# Program Description: Based on user inputs, determine the total cost of the customer's shopping trip and how many different items the customer bought. Display these results to the customer. 

# Start program.
    # Begin an item counter by setting the number of items equal to zero. Assign to variable 'items.'
    # Begin a total price accumulator by setting the total price equal to zero. Assign to variable 'total.'
    # Get user's input for the item quantity (if any) as an integer. Assign to variable 'item_qty.'
    # While 'item_qty' does NOT equal zero:
        # Add one to 'items' by using the += augmented assignment operator. 
        # Get user's input for the item(s) price as a floating point number. Assign to variable 'item_price.'
        # Calculate the subtotal by multiplying 'item_qty' and 'item_price' together. Assign to variable 'subtotal.'
        # Add 'subtotal' to 'total' by using the += augmented assignment operator.
        # Print 'subtotal' in currency format.
        # Repeat the 'item_qty' question to the user (this will continue to restart the program as well as its associated inputs and outputs).
    # If 'item_qty' DOES equal zero, print a statement using 'items' to state how many items the user purchased.
    # Using 'total,' print a statement prompting the user to pay the total amount for all items purchased, formatting the statement in currency format.
# End program. 

def main ():
# Begin the item counter by setting the number of items equal to 0.
    items = 0
    
# Begin the total price accumulator by setting the price equal to 0. 
    total = 0
    
# Prompt the user to enter the number of items or to press the number key '0' to quit the program.
    ### get user input
    item_qty = int(input('Enter item quantity or press zero to quit: '))
    
# Use a while statement to determine whether or not the user's input is equal to zero. Refer to pseudocode for this while loop explanation. 
    while item_qty != 0:
        
# Continue to add one to the items counter. 
        ### do the math
        items += 1
        ### generate output
        
# Prompt the user to enter the unit price of the item they are purchasing.
        ### get user input
        item_price = float(input('Enter the unit price of the item: '))
    
# Multiply the number of item(s) by the price of each item to arrive at the subtotal. 
        ### do the math
        subtotal = item_qty * item_price
        ### generate output
        
# Add the current subtotal to a running total, which will be displayed when the user decides to quit the program. 
        ### do the math
        total += subtotal
        ### generate output
        
# Display the individual's subtotal in currency format. 
        print('The subtotal is: $', format(subtotal, '.2f'), sep = '')
        
# Repeat this question (asked in the beginning of this program) to restart the process. 
        item_qty = int(input('Enter item quantity or press zero to quit: '))

# Display both (a) the number of different items purchased, and (b) the total the user will have to pay, formatting each in currency format. 
    print('You purchased', items, 'different items.')
    print('Please pay $', format(total, '.2f'), sep = '')
    print('Thank you for shopping with us today! We hope to see you again!')

main()
