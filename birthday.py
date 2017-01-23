from datetime import date
from datetime import time
from datetime import datetime

#string date
today = date.today()
# print str(today.month) + " " + str(today.day) + ", " + str(today.year)

print "Todays date and time is:"
###current date and time
now = datetime.now()
print now.strftime("%B %d, %Y")
print now.strftime("%I:%M:%S %p")

###days until my birthday
#today = date.today() #gets todays date
bday = date(today.year, 11, 23) #get my bday for that year
#check if the date has gone by
#if it has then use the replace() function to get the date for next year
if bday < today:
    print "Your birthday has already passed %d days ago" % ((today-bday).days)
    bday = bday.replace(year=today.year + 1) 
print " "
print "How many days until your birthday?"
time_to_bday = abs(bday - today)
print time_to_bday.days, "days until my birthday."
