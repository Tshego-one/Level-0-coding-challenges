
def time_convert(number):

    hour = number // 60

    if hour >= 2 or hour == 0:
        string_1 = "hours"
    else:
        string_1 = "hour"

    minute = number % 60

    if minute >=2 or minute == 0:
        string_2 = "minutes"
    else:
        string_2 = "minute"

    print(f"{hour} {string_1}, {minute} {string_2}")
  
time_convert(188)