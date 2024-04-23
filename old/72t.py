time1 = int(input("Time 1:"))
time2 = int(input("Time 2:"))

hour1 = time1 // 100
hour2 = time2 // 100
min1 = time1 % 100
min2 = time2 %100

hour_diff = hour2 - hour1
min_diff = min2 - min1

print("Hours: ", hour_diff, "\nMinutes: ", min_diff)