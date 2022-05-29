# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 6 Assignment #2 (CUSTOM MODULE)
# Collaborators: None

# calc_pay.py
# ** CUSTOM MODULE FOR MODULE 6 ASSIGNMENT #2**

'''
This is a custom module that is imported into 'program6_2.py.'
The following function is called in the program.
This function is used within the program to (a) define what is considered overtime, (b) determine whether or not the user worked overtime for the week they desire to see their total pay, (c) calculate their regular pay, overtime pay (if any), and total pay, and (d) tell the user their total pay for the week.
To pass the two arguments 'total_hours' and 'pay_rate' to the above program's 'main' function, we use 'total_hours' and 'pay_rate' as this function's parameters.
This function is considered a 'void' function, meaning that it will print the output, which, in turn, will be displayed in the main program's output when this function is called within the 'main' function.
'''

def calc_pay(total_hours, pay_rate):                                                        # Define the 'calc_pay' function for the 'total_hours' and 'pay_rate' arguments.
    
    ot_time = (total_hours - 40)                                                            # Define what is considered overtime by subtracting 40 from 'total_hours.'

    if total_hours > 40:                                                                    # Use an 'if' statement to determine whether or not the user worked overtime for they week they desire to see their total pay. 
        reg_pay = (total_hours - ot_time) * pay_rate                                        # Calculate the user's regular pay by subtracting the overtime hours from the total hours worked and multiplying that value by the user's hourly pay rate.
        ot_rate = (pay_rate * 1.5)                                                          # Calculate the hourly overtime pay rate by multiplying the user's hourly pay rate by 1.5. 
        ot_pay = (ot_time * ot_rate)                                                        # Calculatee the user's overtime pay multiplying the user's overtime hours by the previously calculated overtime hourly pay rate. 
    else:                                                                                   # Use an 'else' statement to determine the user's pay without overtime.
        reg_pay = total_hours * pay_rate                                                    # Calculate the user's regular pay by multiplying the total hours the user worked during the week by their hourly pay rate. 
        ot_pay = 0                                                                          # We know that the user worked 0 hours of overtime through the calculations, so we can re-assign 'ot_pay' to the value of 0. 
        
    total_pay = reg_pay + ot_pay                                                            # Calculate the user's total pay by adding the user's regular pay by their overtime pay.
    
    print('Regular pay: $', format(reg_pay, ',.2f'), sep = '')                              # Display a statement telling the user what their calculated regular pay for the week is. 
    print('Overtime pay: $', format(ot_pay, ',.2f'), sep = '')                              # Display a statement telling the user what their calcualted overtime pay for the week is. 
    print('Total pay: $', format(total_pay, ',.2f'), sep = '')                              # Display a statement telling the user what their calculated total pay for the week is. 

    
