unix = int(input('UNIX time: '))

years = 0
leap = 2
while unix >= 31536000:
  if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
    unix -= 31622400
  else:
    unix -= 31536000
  years +=1
  leap+=1
print('years',years)

days = 0
while unix >= 86400:
  unix -= 86400
  days += 1
print('days',days)
hours = 0
while unix >= 3600:
  unix -= 3600
  hours += 1
print('hours',hours)
minutes = 0
while unix >= 60:
  unix -= 60
  minutes += 1
print('mins', minutes)
print('seconds',unix)
year = 1970 + years
print('year',year)
month = 0
if leap % 4 == 0:
  days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  print('Leap Year')
else:
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
while days >= 0:
  day = days+1
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

print(f'{hours:02d}:{minutes:02d} {day_half}  {month:02d}/{day:02d}/{year}')