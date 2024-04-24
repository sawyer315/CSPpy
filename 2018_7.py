unix = int(input('UNIX time: '))

#days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years = 0
while unix >= 31536000:
  if years % 4 == 0:
    unix -= 31622400
  else:
    unix -= 31536000
  years +=1
print(years)

days = 0
while unix >= 86400:
  unix -= 86400
  days += 1
print('days',days)
hours = 0
while unix >= 3600:
  unix -= 3600
  hours += 1
print(hours)
minutes = 0
while unix >= 60:
  unix -= 60
  minutes += 1
print(minutes)
print(unix)
year = 1970 + years
print(year)
month = 0
if years % 4 == 0:
  days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
while days > 0:
  day = days
  days -= days_in_month[0]
  month += 1
  if days_in_month != []:
    days_in_month.pop(0)
print(month)
day_half = 'AM'
if hours >= 12:
  hours -= 12
  day_half = 'PM'
if hours == 0: hours = 12

print(f'{hours}:{minutes} {day_half}  {month}/{day}/{year}')