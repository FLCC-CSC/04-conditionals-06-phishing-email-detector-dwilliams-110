# FILE NAME - phishing_email_detector.py

# NAME: Daniel Williams
# DATE: 3/38/3036
# BRIEF DESCRIPTION: Using \'in\' and \'or\' operators 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

subject_line = input('Enter the email subject line: ')

if 'urgent' in subject_line.lower():
    print()
    print('SECURITY ASSESSMENT:')
    print('HIGH RISK: Possible phishing attempt.')
    print('------------------------')
    print(f'Analyzed subject: \"{subject_line}\"')
elif 'win' in subject_line.lower() or 'free' in subject_line.lower():
    print()
    print('SECURITY ASSESSMENT:')
    print('MEDIUM RISK: Suspicious offer detected.')
    print('------------------------')
    print(f'Analyzed subject: \"{subject_line}\"')
elif 'password reset' in subject_line.lower():
    print()
    print('SECURITY ASSESSMENT:')
    print('LOW RISK: Verify legitimacy with sender.')
    print('------------------------')
    print(f'Analyzed subject: \"{subject_line}\"')
else:
    print()
    print('SECURITY ASSESSMENT:')
    print('No phishing indicators detected.')
    print('------------------------')
    print(f'Analyzed subject: \"{subject_line}\"')



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural? Using 'in' was very nice and natural. Using the or was a bit tricky, I didn't think you'd have to put the string variable twice. I had to google this.







'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[X] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[X] I'm solid. Totally got it.

'''
