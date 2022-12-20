#**********************Change 1*********************************************************
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:00:30 2021

@author: Tony Jones-Organ

Enter Countdown Length (in seconds) and Officer rank.

Commanding :
           Officer Initiate Code:111A-Destruct
           Executive Officer Initiate Code:21A2B-Destruct
           Chief of Engineering Initiate Code:31B2B-Destruct
Self Destruct Confirmation Code           
           000-Destruct-0
           000-Destruct-1
"""

###################################################################################################
import time

# Custom Functions
# 2. DESCRIBE HOW THE INCLUDED countdown() FUNCTION WORKS
# A:Countdown function works like a stopwatch. Countdown receives integer n(seconds) and it subrated by by ubtill the n is zero
# A:It is used for Timer Purpose
def countdown(n):
    while n >= 0:
        print (n)
        time.sleep(1)
        n -= 1
    
##################################################################################################
# Self Destruct Sequencer
# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = "000-Destruct-0"
    authorized_final = "000-Destruct-1"

    # 3. CREATE VARIABLES (SIMILAR TO ABOVE) FOR THE COMMANDING OFFICER'S CODE (co_code)
    # EXECUTIVE OFFICER'S CODE (xo_code) & CHIEF ENGINEER'S CODE (ce_code)
    # Write your code here
    co_code="11AB-Destruct"
    xo_code="21AB-Destruct"
    ce_code="31AB-Destruct"
    
##################################################################################################
    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.
    #  Display Self Destruct Warning
    print ('--------------------- WARNING! -----------------------\nYou have initiated the USR ARES Self Destruct Program\n_____________________________________________________\nYou must provide Authorized Initiate Code to Proceed.')

##################################################################################################
    # Request Authorized Rank
    # 4. EXPLAIN THE SIGNIFICANCE OF THE int() FUNCTION IN THE FOLLOWING LINE:
    rank = int(input("Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n RANK: "))
    # A. whatever the user give the input value, that will be taken as a string by the input function. 
    #A.  so we have used integer for ranking the officer so here we are using int conversion from user string input.

##################################################################################################
    # Because we're expecting the user to enter a number above, the conditional statement
    # below is needed to convert those numbers into something more useful. Doing this helps
    # reduce the risk of the user introducing bad data into the script.
##################################################################################################
    # Retrieve Rank Initiate Code
##################################################################################################
    # Commanding Officer
    if rank == 1:
        code = "111A-Destruct"
        print ("Commanding Officer Confirmed.")
    # Executive Officer
    elif rank == 2:
        code = "21A2B-Destruct"
        print ("Executive Officer Confirmed.")
    # Chief Engineer
    elif rank == 3:
        code = "31B2B-Destruct"
        print ("Chief Engineer Confirmed.")
    else:
        print ("You are not authorized to initial Self Destruct.")


##################################################################################################
    # Enter Self Destruct Code: 000-Destruct-0 or 000-Destruct-1
##################################################################################################
    # Set Supplied Rank Code
    initiate = input("Enter Self Destruct Confirmation Code: ")

    # Compare Rank Codes
    if initiate == code:
        print ("Self Destruct Initiate Code: ACCEPTED")
        final_code = input("Enter Activation Code: ")
        if final_code == authorized_final:
            print ("Destruct Sequence Confirmed.")
            # 5. EXPLAIN THE SIGNIFICANCE OF X
            print (x, " seconds to Self Destruct.")
            # A. While going for Self Destruct we are enabling stop watch fot destruct.
            # here x will decides the time to go for destruct.
            print ("ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL")
            countdown(x)
            print ("Have a nice day!")
            print ("BOOM!")
        elif final_code == authorized_test:
            print ("Destruct Sequence Test Order Confirmed.")
            print ("THIS IS A DRILL - THIS IS A DRILL")
            print ("Timer Set to: " + str(x) + " seconds.")
        else:
            print ("Destruct Sequence Aborted.")


##################################################################################################
    # Program Ends
##################################################################################################
# Self Destruct
timer = int(input("Enter Countdown Length (in seconds): "))
self_destruct(timer)



# 6. LIST THE LOCAL VARIABLES AND GLOBAL VARIABLES USED THROUGHOUT THIS SCRIPT
# A. Instead of declaring a global variable we have used same value 
#as two local variable named as timer and 
#Local variables:timer,x,final_code,authorized_test,authorized_final,initiate,code,rank
#                xo_code,ce_code,co_code,n


# 7. LIST THE BUILT IN FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. int(),input(),print(),str()

# 8. LIST THE MODULE FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. time.sleep()

# 9. LIST THE CUSTOM FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A.self_destruct(),countdown()