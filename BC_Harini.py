#Importing date and time
import datetime as dt
import time

#Asking user for inputs
print('WANNA KNOW HOW FAR YOUR NEXT BIRTHDAY IS??')
print('WELL, YOU ARE IN LUCK BECAUSE THAT IS EXACTLY WHAT I DO')

year =int(input("Which year were u born in?"))
month=int(input("Which month were you born in? 1 for Jan etc..")) 
day=int(input("Which date were you born on?"))
print()

date_birth = dt.datetime(year,month,day)

#Determining which Generation the user belongs to and their qualities
if year >= 1946 and year <= 1964:
    print('Known for their strong work ethic, resilience and no-nonsense attitude,Gen baby boomers show us how to navigate the complex modern work environment')
    print('YOU BELONG TO GEN BABY BOOMERS!!!!')
elif year >= 1965 and year <= 1980:
    print("Gen Xers grew up to be self reliant, self sufficient and skep- tical. They don't trust in the permanence of things. In the workplace, they are independent and don't respond well to micro-management.")
    print('YOU BELONG TO GEN X!!!')
elif year >= 1981 and year <= 1996:
    print("Generation Y can be confident and ambitious. They are not afraid to question authority, are constantly seeking out new challenges and want meaningful work.")
    print('YOU BELONG TO GEN Y!!!')
elif year >= 1997 and year <= 2009:
    print("Gen Z are typically self-driven, collaborative, and diverse-minded. They value flexibility, authenticity, and a pragmatic approach to addressing problems.")
    print('YOU BELONG TO GEN Z!!!')
elif year >= 2010 and year <= 2024:
    print('Generation Alpha has been shown to develop characteristics such as hyper-connectivity, independence, and visual learning. Alpha children are connected more than ever due to their technologically based way of living.')
    print('YOU BELONG TO GEN ALPHA!!!')
elif year >= 2025 and year <= 2036:
    print("Generation Beta will be more globally minded, community-focused, and collaborative than other generations.")
    print('YOU BELONG TO GEN BETA!!!')

print()

#Determining which Zodiac sign user is and their qualities
def zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn:","Goal-oriented but unforgiving"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return"Aquarius:","Philosophical but detached"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces","Whimsical but over-sensitive"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return  "Aries:","Competitive but insecure"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus:","Loyal but stubborn"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini:","Versatile but impatient"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer:","Passionate but uncommunicative"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo:","Confident but dominating"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo:","Perfectionist but self-critical"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra:","Empathetic but indecisive"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio:","Intense but secretive"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
       return "Sagittarius:","Spontaneous but flighty"
    else:
        print('Are you an alien or smthg??')

zodiac = zodiac_sign(day, month)
print("Your zodiac sign is:", zodiac)


weekday_num= date_birth.weekday()
weekday_names=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#Giving user their original day of birth
print("You were originally born on (drum roll pls :))")
print()
print(weekday_names[weekday_num].upper(),"!!!!!")
print()

current_time = dt.datetime.now()
this_year = current_time.year
this_year_bday = dt.datetime(this_year,month,day)

#Finding next birthday(no leap year)
if this_year_bday > current_time:
    next_bday = this_year_bday
    print('Your next birthday will be this year')
else:
    next_bday = dt.datetime(this_year +1, month, day)
    print('Your next birthday will be next year')

print('Your next bday is on')
print(next_bday)
print()

weekday_num = next_bday.weekday()

print('But I can tell you..It will be on a')
print(weekday_names[weekday_num])


#Countdown for next birthday
while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    seconds_left = total_seconds_left%60
    total_mins_left = total_seconds_left//60
    minutes_left = total_mins_left%60
    hrs_left = total_mins_left//60


    print('Your next birthday is', days_left, 'days', hrs_left, 'hrs', minutes_left, 'mins', seconds_left, 'seconds away', end = '\r' )
    time.sleep(1)
