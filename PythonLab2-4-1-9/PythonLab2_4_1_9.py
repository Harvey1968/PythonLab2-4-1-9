#Scenario
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles", end ="\n\n")

#Double checker (no rounding)
print(7.38 * 1.61)
print(12.25 / 1.61, end ="\n\n")

