# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 6 Assignment #1
# Collaborators: None

# program6_1.py
# Program Description: Based on user input, write each day the user worked and each day's respective hours that the user worked to a separate plain text (.txt) file.
    # Use a 'for' loop to control (a) when the file opens, (b) when data is actively written to it, (c) and when it closes for data storage and subsequent retrieval in the next program ('program6_2.py'). 

# Start program.
    # Open the plain text (.txt) file 'workweek.txt' for writing data into the file's contents. Assign to variable 'work_file' ➞ This variable will be used to reference the file object.
    # Prompt the user to enter the number of days they worked in a given week for which they would like to view their total pay. Assign to variable 'days.'
    # For any number in the range beginning at one (1) and ending at 'days' plus one (1):
        # Prompt the user to enter the day of week that they worked. Assign to variable 'day_week.' ➞ This input will repeat for each recurrence of the 'for' loop, so the user will be able to input a corresponding day of the week for the number of days they worked.
        # Prompt the user to enter the number of hours they worked for the day of the week they previously entered. Assign to variable 'hours.' ➞ This input will repeat for each recurrence of the 'for' loop, so the user will be able to enter their hours for each day they worked.
        # Call the 'write' method function for 'work_file' to write each day the user worked as a string, allowing for the concatenation of a '/n' escape sequence to ensure that each piece of data is written to a separate line in the file.
        # Call the 'write' method function for 'work_file' to write the number of hours the user worked (per day) age a string, allowing for the concatenation of a '/n' escape sequence to ensure that each piece of data is written to a separate line in the file.
    # Close the plain text (.txt) file 'workweek.txt' by calling the 'close' method function for 'work_file.'
    # Print a statement telling the user that their .txt file was created and is now stored within their designated folder on their device's memory.
# End program.

def main():
    
# Open the file for which the user's inputs will be stored and subsequently retrieved ➞ Open as 'write' ONLY file, and not in Python's 'appending' data writing mode ('a').
    work_file = open('workweek.txt', 'w')
    
# Get user's input for the number of days they worked in the week for which they would like to view their total pay. 
    days = int(input('Enter the number of days you worked this week: '))
    
# Use a 'for' loop to execute the processes within the loop for the predetermined range given by the user in the previous input. 
    for num in range (1, days + 1):
        
# Get user's input for the day of week for which the user would like to enter the number of hours they worked. 
        day_week = input('Enter the day of week: ')
        
# Get user's input for the number of hours they worked on the day that they entered in the previous input. 
        hours = int(input('How many hours did you work on ' + str(day_week) + '? '))
        
# Call the 'write' function for 'work_file' to write each day the user worked to the 'workweek.txt' file as a strng. Concatenate the '/n' escape sequence ➞ This will allow for each piece of data to be written on a separate line in the file.
        work_file.write(str(day_week) + '\n')
        
#  Call the 'write' function for 'work_file' to write the number of hours the user worked on the inputted day to the 'workweek.txt' file as a strng. Concatenate the '/n' escape sequence ➞ This will allow for each piece of data to be written on a separate line in the file.
        work_file.write(str(hours) + '\n')

# Call the 'close' function for 'work_file' to close the file for which the user's inputs will be stored and subsequently retrieved.
    work_file.close()
    
# Display a statement that tells the user that their file (which stores (a) each day of the week that they worked and (b) the number of hours they worked per day of the week) was created. 
    print('File was created.')
    
# Call the 'main' function to end the program. 
main()
