# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 6 Assignment #2
# Collaborators: None

# program6_2.py
# Program Description: Based on user inputs from the previous program ('program6_1.py'), retrieve and read the data from the file, display the user's hours worked per day of the given week, and calculate user's total pay for that week.
    # Using a custom imported module, tell the user (a) the total number of hours they worked that week, (b) how many of which were considered overtime, (c) their calculated regular pay, (d) their calculated overtime pay, and (e) their calculated total pay. 

# Before defining the 'main' function, import the custom module 'calc_pay.py' as 'calc' ➞ Importing as a different name will increase efficiency when writing this program's code, and will also reduce confusion between the custom module and the function that it stores.
# Start program.  
    # Begin an accumulator that starts at zero (0) for the total hours that the user worked during the week, which will increase by each input of 'hours' value for each recurrence of the program's 'while' loop. Assign to variable 'total_hours.'
    # OPTIONAL CODE: Print a statement summarizing the program's purpose/function to the user, which will make this program more understandable for people who do not know what this program will do for them.
    # Prompt the user to enter their hourly pay rate ➞ Allow for the input to accept floating-point numbers, as this occurs in the real world. Assign to variable 'pay_rate.'
    # OPTIONAL CODE: Print a message telling the user that the program is retrieving their data from the previous program. 
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Open the plain text (.txt) file 'workweek.txt' for reading data from the file's contents. Assign to variable 'work_file' ➞ This variable will be used to reference the file object.
    # Read the string contents within 'workweek.txt' by calling the 'readline' method function for 'work_file.' Assign to variable 'day.'
    # While 'day' does NOT equal an empty string (i.e., there is no 'day' data for the program to read):
        # Read the integer contents within 'workweek.txt' by calling the 'readline' method function for 'work_file.' Assign to variable 'hours.'
        # Add 'hours' to the 'total_hours' accumulator (i.e., for every loop iteration, the number of hours the user worked per day will be added to the accumulator, and will occur for every day the user chooses to input) ➞ This will be used as one variable for calculating the user's total pay for the week.
        # "Strip" the '\n' escape sequence from within 'day' by using the 'rstrip' method function ➞ This allows for the program to interpret the file's data by removing specific characters from the end of a string.
        # Print a statement telling the user (a) the day of the week they worked and (b) how many hours they worked each day, with the ourput formatted to one (1) decimal place ➞ This statement will re-print for each iteration of the 'while' loop.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Close the plain text (.txt) file 'workweek.txt' by calling the 'close' method function for 'work_file.'\
    # If 'total_hours' is greater than forty (40):
        # Calculate the user's hours of overtime by using the subtraction math operator to subtract forty (40) from 'total_hours.' Assign to variable 'ot_time.'
    # Else:
        # 'ot_time' is equivalent to zero (0) ➞ This means that the user did not work overtime for the week they wish to see their total pay.
    # Print a statement telling the user how many total hours they worked during that week.
    # Print a statement telling the user how many overtime hours they worked during that week.
    # Print a statement telling the user what their hourly pay rate is, formatting the output in currency format.
    # OPTIONAL CODE: Print a statement telling the user that the program is about to output the results it calculated. 
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Using 'dot-notation,' call the 'calc_pay' function from within the custom imported module 'calc' for the two arguments 'total_hours' and 'pay_rate.'
# End program.

# Import the custom module 'calc_pay.py' as 'calc' to make this program's code easier to understand ➞ The function within this custom module is responsible for the majority of the program's calculations that will tell the user (a) their regular pay, (b) overtime pay, and (c) total pay.
import calc_pay as calc

def main():
    
# Set the 'total_hours' accumulator to 0, which will ensure that, when added to the 'hours' variable, the resulting output is not compromised.
    total_hours = 0
    
# OPTIONAL: Display a statement to the user that accurately captures this program's purpose/function.
    print('This program calculates the total pay of your work week, overtime included.')
    
# Get user's input for their hourly pay rate. 
    pay_rate = float(input('Please enter your hourly pay rate: '))
    
# OPTIONAL: [Display a message telling the user that the program is retrieving their data.]
    print('Retrieving your data...')
    
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('-----------------------')
    
# Open the file for which the user's inputs will be retrieved and subsequently read.
    work_file = open('workweek.txt', 'r')
    
# Read the string contents within 'work_file' by calling the 'readline' function. 
    day = work_file.readline()
    
# Use a while loop to determine whether or not the loop's processes should occur for the file's contents.
    while day != '':
        
# Read the integer contents within 'friend_file' by calling the 'readline' function. 
        hours = int(work_file.readline())
        
# Continue to add the hours the user worked per day ('hours') to 'total_hours.' Effectively, this variable holds the total hours that the user worked for the entire week, and will be used as one variable for calculating their total pay for the week. 
        total_hours += hours
        
# "Strip" the extraneous '\n' escape sequence from within 'day' by using the 'rstrip' function.
        day = day.rstrip('\n')
        
# Display a statement to the user that lists the outputs from their 'program6_1.py' inputs. 
        print('You worked', format(hours, '.1f'), 'hours on', day)
        
# Continue the loop by using the 'readline' function to read the next lines of data within 'workweek.txt.'
        day = work_file.readline()
        
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('-----------------------')
    
# Call the 'close' function for 'work_file' to close the file ➞ This program no longer needs this file to complete the subsequent processes.
    work_file.close()
    
# Use an 'if-else' block to determine whether the user worked overtime for the week they worked.
    if total_hours > 40:
        
# Calculate the user's overtime by subtracting 40 from 'total_hours.'
        ot_time = total_hours - 40
        
# The above 'if' statement was proven to be false.
    else:
        
# The user's worked overtime automatically becomes 0, for they did not work for more than 40 hours during the week. 
        ot_time = 0
        
# Display a statement telling the user the total number of hours they worked during the week. 
    print('You worked', total_hours, 'hours this week.')
    
# Display a statement telling the user how many of those hours were considered overtime (if any). 
    print('Of those', total_hours, 'hours,', ot_time, 'hours were overtime.')
    
# Display a statement telling the user what their hourly pay rate is, formatting the output in currency format. 
    print('Your hourly pay rate is $', format(pay_rate, ',.2f'), sep = '')
    
# OPTIONAL: [Display a message telling the user that the program has calculated their total pay.]
    print('Here is what this program calculated:')
    
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('-----------------------')
    
# Using the so-called 'dot-notation,' call the 'calc_pay' function from within the custom imported module 'calc' for two arguments: 'total_hours' and 'pay_rate.' 
    calc.calc_pay(total_hours, pay_rate)
    
# Call the 'main' function to end the program. 
main()
