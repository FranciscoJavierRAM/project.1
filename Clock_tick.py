# Clock Tick Program
# SDM: This program will take in user input in the
# format of HH:MM where the digits can represent any
# valid 12 hour clock time, so for example, 01:59
# would be 01:59 AM or PM. After taking in a time,
# 1 more user input will be a positive integer which
# ticks the clock forward that many minutes & display
# the new time. Program will politely & clearly ask
# the user to put in the required info
# Bonus Points: (1) handle seconds also, so instead
# of taking in minutes to tick forward, it will take
# in seconds to tick forward. (2) Handle AM/PM inputs
# and outputs
#import the math library to use Math equations later on
import math
#The program will begin by introducing the premise and asking for the input
#of the users current time in a whole positive numbers for current hour, minute, seconds and for am or pm.
print("Hello wonderful human being, I am a time machine!\nI can travel into the future," \
" but first I'm going to need some information from you.")
hour = int(input("What is the current hour?\n"
"(please type a positive whole number)\n"))
#Im padding the amount so it show a zero in from of it if its less than 10 by using f"{hour:02}"
#Im also saving the number of hours as a variable for later use
padded_hour = f"{hour:02}"
#here Im turning the hours into seconds
hour_sec = hour * 60 * 60

minute = int(input("Now the minutes:\n(please type a positive whole number)\n"))
#Im saving the number of minutes as a variable
padded_minute = f"{minute:02}"
#turning the minutes into seconds
minute_sec = minute * 60

second = int(input("Now the seconds:\n(please type a positive whole number)\n"))
#Im savinf the number of seconds as a variable a padding it
padded_second = f"{second:02}"

am_pm = input("Is it currently am or pm:\n(Please type ""am"" or ""pm"")\n")
#Print out the users current time with the padded values
print(f"Your time is currently {padded_hour}:{padded_minute}:{padded_second}{am_pm}\n")
#Ask the user for an input of how many seconds they'd like 
#to travel into the future(tick the clock forward).
future_time = int(input(" How many seconds will you want to travel into the future?\n" \
"(Please type a positive whole number\n"))
# Calculate the total number of seconds by adding them all together 
# including the seconds we'll tick forward.
total_second = ((hour_sec + minute_sec + second) + future_time)

#I came up with this code to determine if am or pm will switch
if total_second >= 43200:
    if am_pm == "am":
        am_pm = "pm"
    elif am_pm == "pm":
        am_pm = "am"
# Here it check if the clock goes into 13:00 hours it goes down to 01:00
if total_second >= 46800:
   total_second = total_second - 43200
# Now we calculate the total hours by getting the quotinet of 
# the total number of seconds divided by 3600(60*60).
hours = total_second // 3600
#save the # of hours as a padded variable
hours_padded = f"{hours:02}"
# Now the total number of minutes by taking the quotient of sixty(minutes in seconds)
# from the remainder of the last operation
remaining = (total_second % 3600) // 60
#save the # of minutes as a padded variable
minutes_padded = f"{remaining:02}"
# Get the number of seconds left by getting the remainder of the last operation
remaining = total_second % 60
#save the # of seconds as a padded variable
seconds_padded = f"{remaining:02}"
#Finally print out the new time with the padded values
print(f"Your new time is {hours_padded}:{minutes_padded}:{seconds_padded}{am_pm}")