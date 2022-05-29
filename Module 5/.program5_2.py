# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 5 Assignment #2
# Collaborators: None

# program5_2.py
# Program Description: Based on user inputs, determine (a) how many courses the user has taken throughout the term, (b), the name of each course,
    # (c) how many tests occurred in each course, (d) the scores of each test, (e) the score average for each course, and (f) the user's term average. Be sure to include a custom imported module to do the majority of the program's calculations. 

# Before defining the 'main' function, import the custom 'grades' module to utilize the 'grade_pct' function, which will allow this program to prompt the user to enter number of tests in each course and the corresponding test scores in each course, as well as calculate the average of each courses' test scores.
# Start program.
    # Begin a counter that starts at zero (0) for the number of courses the user is currently taking, which will increase by one (1) for each recurrence of the program's 'for' loop. Assign to variable 'course.'
    # Begin a counter that starts at zero (0) for the total of the user's course test scores, which will increase by each inputted score for each recurrence of the program's 'for' loop. Assign to variable 'term_total.'
    # Prompt the user to enter the number of courses they are taking in the term. 
    # For a number in a range starting at one (1) and stopping at the user's input for their number of current courses plus one (1):
        # Add one (1) to the 'course' counter.
        # Prompt the user to enter the name of the course for which they will input their test scores.
        # Print a statement telling the user that their course data is being retrieved.
        # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output. 
        # "Catch" the output of the 'grades_pct' function for the argument 'course' within the 'grades' custom imported module. Assign to variable 'scores.'
        # Print a statement that tells the user what their average is for that course, given that they have inputted their test scores. Format the output to one (1) decimal place, making sure that the percent (%) symbol accompanies said output. 
        # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output. 
    # Calculate the user's term average (which determines the average grade based on all inputted test scores from all desired courses) by using the division math operator to divide 'term_total' by 'course.' Assign to variable 'term_avg.'
    # OPTIONAL CODE: "Catch" the output of the 'determine_grade' function for the argument 'term_avg' within the 'grades' custom imported module. Assign to variable 'letter_grade.'
    # Print a statement that tells the user what their final average is for the term, formatting the output to one (1) decimal place and making sure that the percent (%) symbol accompanies said output.
# End program.

# Import the custom 'grades' module. 
import grades

def main():
    
# Set the 'course' counter to 0, which will ensure that, when increased by 1 for each recurrence of the 'for' loop, the resulting output is not compromised. 
    course = 0
    
# Set the 'term_total' counter to 0, which will ensure that, when added to the 'score' variable, the resulting output is not compromised. 
    term_total = 0
    
# Get user's input for the number of courses they have taken during the term. 
    num_courses = int(input('Please enter the number of courses taken in this term: '))
    
# Use a 'for' loop to determine the range of numbers for which this loop will execute the following processes. 
    for num in range (1, num_courses + 1):
        
# Continue to add 1 to the 'course' counter for each iteration of the loop. 
        course += 1
        
# Get user's input for the name of the course that has test grades. 
        course_name = input('Please enter the course name: ')
        
# Display to the user that the program is currently getting data for their course. 
        print('Retrieving data for your', course_name, 'course.')
        
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
        print('---------------------------------------')
        
# Using the so-called 'dot-notation,' "catch" the imported module's output by calling the 'grade_pct' function for the argument 'course' within the imported 'grades' module. Assign to variable 'scores.'
        scores = grades.grade_pct(course)
        
# Continue to add the output for 'scores' to 'term_total.' Effectively, this variable holds the total for all the user's test scores across all of their courses, and will be used as one variable for calculating their overall term average).
        term_total += scores
        
# Display the user's test score average for the current course being handled by the program. Format output to three decimal places and specifying that the grade is a percentage.
        print('The average for this course is ', format(scores, ',.1f'), '%.', sep = '')
        
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
        print('------------------------------------')
        
# Calculate the user's term average by dividing 'term_total' by 'course.' 
    term_avg = (term_total / course)
    
# Using the 'dot-notation,' "catch" the imported module's output by calling the 'determine_grade' function for the argument 'term_avg' within the imported 'grades' module. Assign to variable 'letter_grade.'
    letter_grade = grades.determine_grade(term_avg)
    
# Display the calculation's output to the user. Format output to three decimal places and specifying that the grade is a percentage. 
    print('Your average for the term is ', format(term_avg, ',.1f'), '%.', sep = '')
    
# OPTIONAL: [Display a statement telling the user their letter grade ➞ based on the number calculations from 'term_avg.']
    print('You ended this term with a(n)', letter_grade)
    
# Call the 'main' function to end the program. 
main()
                    
