#SDM: This program will take in user input in the format of HH:MM where the digits can be any valid 12 hour clock time, so for example, 01:59 in either late night/morning or afternoon
#After takin in a tiem, 1 more user input wil be a positive integer which ticks the clock forward that many minutes & display the new time
#bonus instead taking in minutes to tick forward, it will take in seconds to tick
#program will politely ask the user to put the required information clearly
#Due date: End of day Monday (11:59pm)
import math
print("Hello wonderful human being, I am a time machine! I can travel into the future, but first I'm going to need some information from you.")
hour = int(input("What is the current hour?\n" \
"(please type a whole number)\n"))
padded_hour = f"{hour:02}"
hour_min = hour * 60
minute = int(input("Now the minutes:\n"))
padded_minute = f"{minute:02}"
seconds = int(input("Now the seconds:\n"))
padded_seconds = f"{seconds:02}"
am_pm = input("Is it currently am or pm: ")

print(f"Your time is currently {padded_hour}:{padded_minute}:{padded_seconds}{am_pm}\n")

future_time = int(input(" How many minutes will you want to travel into the future?\n" \
"(Please type a positive whole number\n"))
total_minutes = ((hour_min + minute) + future_time)

if total_minutes >= 720:
    if am_pm == "am":
        am_pm = "pm"
    elif am_pm == "pm":
        am_pm = "am"
if total_minutes >= 780:
   total_minutes = total_minutes - 720
hours = total_minutes // 60
hours_padded = f"{hours:02}"
remaining = total_minutes % 60
minutes_padded = f"{remaining:02}"

print(f"Your new time is {hours_padded}:{minutes_padded}:{padded_seconds}{am_pm}!\n")
seconds_forward = int(input("Now lets travel in seconds, how many seconds will you travel into the future?:\n"))
total_seconds = (total_minutes * 60) + seconds_forward + seconds
print (total_seconds)
if total_seconds >= 46800:
   total_seconds = total_seconds - 43200
hours = total_seconds // 3600
hours_padded = f"{hours:02}"
total_seconds = total_seconds % 3600
minutes = total_seconds // 60
minutes_padded = f"{minutes:02}"
seconds = total_seconds % 60
seconds_padded = f"{seconds:02}"
print(f"Your new time is {hours_padded}:{minutes_padded}:{seconds_padded}{am_pm}!\n")





# 1 Hour = 60 minutes8
# 1 Minute = 60 seconds
# 1159pm > 1200am
# 1159am > 1200pm
# 1259 > 01000