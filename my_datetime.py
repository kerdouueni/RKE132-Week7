import datetime

now = datetime.datetime.now()

print(now.year) #Kuvab praegust aastat (2026)
print(now.month) #Kuvab praegust kuud (1-12)
print(now.day) #Kuvab kuupäeva (1-31)
print(now.hour) #Kuvab tunni (0-23)

weekday = now.strftime("%A")
print(weekday)