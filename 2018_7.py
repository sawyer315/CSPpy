unix = int(input('UNIX time: '))

unix = int(unix/60)
day_half = 'AM'
hours = 0
days = 0
month = 'Jan'
year = 1970
lmonth = ['Jan',  'Mar', 'May',
          'Jul', 'Aug', 'Oct', 'Dec']
smonth = ['Apr', 'Jun', 'Sep', 'Nov']
allmonths = ['Jan', 'Feb', 'Mar',
             'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year_done = False
while year_done is False:
  if year % 4 == 0:
    if unix >= 527040:
      unix -= 527040
      year += 1
    else:
      year_done = True
  else:
    if unix >= 525600:
      unix -= 525600
      year += 1
    else:
      year_done = True

while unix >= 1440:
  days += 1
  unix -= 1440

month_done = False

if year % 4 == 0:
  while month_done is False:
    if month in lmonth:
      if days >= 31:
        days -= 31
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True
    elif month in smonth:
      if days >= 30:
        days -= 30
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True
    else:
      if days >= 29:
        days -= 29
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True

  
else:
  while month_done is False:
    if month in lmonth:
      if days >= 31:
        days -= 31
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True
    elif month in smonth:
      if days >= 30:
        days -= 30
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True
    else:
      if days >= 28:
        days -= 28
        allmonths.pop(0)
        month = allmonths[0]
      else: month_done = True

while unix >= 60:
  unix -= 60
  hours += 1

if hours >= 12:
  hours -= 12
  day_half = 'PM'
if hours == 0:
  hours = 12
days +=1

print(year)
print(days+1)
print(month)
print(hours)
print(unix)

print(f'{hours:02d}:{unix:02d} {day_half}  {month}/{days:02d}/{year}')