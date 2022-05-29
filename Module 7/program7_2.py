# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 7 Assignment #2
# Collaborators: None

# program7_2.py
# Program Description: Given a list of twelve randomly generated integers: (a) sort the list in descending order, (b) slice the last four numbers in the sorted list, (c) determine the list's total, (d) determine which number is largest,
    # and, (e) determine which number is smallest. Display all outputs to the user. 

# Before defining the 'main' function, import the 'random' module as 'ra' ➞ Importing as a different name will increase efficiency when writing this program's code and will make it easier to read when debugging, for example.
# Start program.
    # OPTIONAL CODE: Print a statement telling the user that a list of random numbers from one (1) to one hundred (100) - inclusive - will appear on screen from which the program's executable statements will run.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Create an empty list for which the twelve random integers will be stored by placing two brackets next to each other. Assign to variable 'nums.'
    # For any number 'n' in the range of twelve numbers:
        # Call the 'append' method for empty list 'nums' and create random integers between one and one hundred using the 'randint' function for the 'ra' module.
    # Sort list 'nums' in ascending order by calling the 'sort()' method.
    # Sort list 'nums' in descending order by calling the 'reverse()' method.
    # For any number 'n' in list 'nums':
        # Print 'n' on one single line, using the 'end' operator to separate each integer by a single space ➞ This process avoids the so-called 'crude dump,' which is usually not good practice when creating programs, especially ones with numbers.
    # Print a single space in between the previous and following statements ➞ This ensures that the two lines of code are separated and will not appear on the same line.
    # Slice the final four numbers of list 'nums' by using the range from index eight to the end of the list (index eleven). Assign to variable 'final_four.'
    # Print a statement telling the user that the final four numbers follow in the next statement.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # For any number 'n' in new list 'final_four':
        # Print 'n' on one single line, using the 'end' operator to separate each integer by a single space ➞ This process avoids the so-called 'crude dump.'
    # Print a statement telling the user what the calculated total of all twelve integers is by using the 'sum' function for list 'nums.'
    # Print a statement telling the user what the largest number in the list is by using the 'max' function for list 'nums.'
    # Print a statement telling the user what the smallest number in the list is by using the 'min' function for list 'nums.'
# End program.

# Import the 'random' module as 'ra' ➞ This function is responsible for generating the random integers necessary for this program to run.
import random as ra

def main():
# OPTIONAL: [Display a message to the user telling them that a list of random integers will follow.]
    print('Here is a list of random integers from 1-100 in descending order...')
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('-------------------------------------------------------------------')
# Create an empty list that will later store the random integers. 
    nums = []
# Use a 'for' loop with the range function to write 12 random integers into the empty list.
    for n in range(12):
# Call the 'append' function for the list and write random integers all between 1 and 100, inclusive. 
        nums.append(ra.randint(1, 101))
# Sort this list in ascending order by calling the 'sort()' method for list 'nums.'
    nums.sort()
# Sort this list in descending order by calling the 'reverse()' method for list 'nums.'
    nums.reverse()
# Use a 'for' loop to display the random integers within the list's contents ➞ This flow control statement will avoid 'crude dumping.'
    for n in nums:
# Display each integer on a single line, separated by a single space.
        print(n, end = ' ')
# Display a space between the previous and following statements so that each get separated and do not appear on the same line together.
    print()
# Slice the final 4 integers from list 'nums' ➞ This will use the range from index 8 to index 11.
    final_four = nums[8:]
# Display a statement telling the user that the final four numbers list will appear following this statement. 
    print('The final four numbers include:')
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('-------------------------------')
# Use a 'for' loop to display the random integers within this new list's contents ➞ Again, to avoid a 'crude dump.'
    for n in final_four:
# Display each integer on a single line, separated by a single space.
        print(n, end = ' ')
# Display a space between the previous and following statements so that each get separated and do not appear on the same line together.
    print()
# Display a statement telling the user what the total for all 12 random integers is. 
    print('The list total is', sum(nums))
# Display a statement telling the user which integer in the list is the largest. 
    print('The largest integer is', max(nums))
# Display a statement telling the user which integer in the list is the smallest. 
    print('The smallest integer is', min(nums))

# Call the 'main' function to end the program. 
main()
    
        
