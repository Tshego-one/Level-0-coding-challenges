
def Convert(number):

    hour = (number // 60)
    minutes = (number % 60)
    
    if hour <= 1 and minutes <=1:
        print(f"{hour} hour, {minutes} minute")
    elif hour >= 2 and minutes >= 2:
        print(f"{hour} hours, {minutes} minutes")
    elif hour <= 1 and minutes >=2:
        print(f"{hour} hour, {minutes} miutes")
    else:
        print(f"{hour} hours, {minutes} minute")
  
Convert(188)