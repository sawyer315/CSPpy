Initial = float(input("Amount: "))
Rate = float(input("Rate: "))
Time = float(input("Time (Days): "))


Final = Initial * ((1 + ((0.01 * Rate) / 365)) ** (Time))
Final = round(Final, 2)
Gain = Final - Initial

print("")
print("New total: $", Final)
print("Amount gained: $", Gain)