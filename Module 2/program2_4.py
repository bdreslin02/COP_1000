# Brandon Dreslin - SPC ID# 2414755; COP1000 #4228; Module 2 Assignment
# Collaborators: https://www.daniweb.com/programming/software-development/threads/328557/calculate-the-change
    # Note: I used this website as a source of help for when I needed help with the math operators. Original code is used in this program. 

# program2_4.py
# Program Description: Calculate the amount of change to be given when user inputs an item price (in cents) under one dollar.

# Start program.
    # Get user input for an item's price in cents.
    # Calculate the change due by subtracting 100 from the item's price. Assign to variable 'item_price.'
    # Calculate the number of quarters needed by using integer division to divide the change due by a quarter's monetary value.
    # Calculate the number of dimes needed by using the remainder operator to divide the change due by a quarter's monetary value. Using integer division, divide the remainder by a dime's monetary value. Assign to variable 'dime.'
    # Calculate the number of nickels needed by using the remainder operator to divide the change due by both a quarter's and a dime's monetary value. Using integer division, divide the remainder by a nickel's monetary value. Assign to variable 'nickel.'
    # Calculate the number of pennies needed by using the remainder operator to divide the change due by a nickel's monetary value. Assign to variable 'penny.'
    # Print the user's original input of an item's price. 
    # Print the number of quarters needed.
    # Print the number of dimes needed.
    # Print the number of nickels needed.
    # Print the number of pennies needed.
# End program. 

def main ():
# Prompt user to enter the item's price, in cents, under one dollar.
    item_price = int(input('Enter the item price in cents: '))
    
# Calculate the amount of change due by subtracting 100 from the item's price.\
    ### do the math
    change_due = 100 - item_price
    ### generate output
    
# Calculate the number of each coin needed to accurately achieve the amount of change needed. Refer to the above pseudocode.
    ### do the math
    quarter = change_due // 25
    dime = (change_due % 25) // 10
    nickel = (change_due % 25 % 10) // 5 
    penny = change_due % 5
    ### generate output
    
# Display the amount of change due, as well as the number of coins needed to make the change.
    print('The change due is:', change_due, 'cents')
    print('Quarters:', quarter)
    print('Dimes:', dime)
    print('Nickels:', nickel)
    print('Pennies:', penny)

main()
