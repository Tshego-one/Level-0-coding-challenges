
def convert(number):

    hour = (number // 60)
    minutes = (number % 60)
    
    if hour == 1 and minutes ==1:
        print(f"{hour} hour, {minutes} minute")
    elif (hour >= 2 or hour == 0) and (minutes >= 2 or minutes == 0):
        print(f"{hour} hours, {minutes} minutes")
    elif hour <= 1 and minutes >=2:
        print(f"{hour} hour, {minutes} minutes")
    else:
        print(f"{hour} hours, {minutes} minute")
  
convert(188)