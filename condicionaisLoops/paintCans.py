painted_area = float(input("enter the size of area to be painted in square meters: "))

cans_paint = painted_area / 108
gallon_paint = painted_area / 21.6

if cans_paint == float(cans_paint):
    cans_paint = cans_paint + 1
if gallon_paint == float(gallon_paint):
    gallon_paint = gallon_paint + 1

total_value_cans = int(cans_paint) * 80
total_value_gallons = int(gallon_paint) * 25

print(f"the number of 18 liter cans you need is {cans_paint} and the total value is {total_value_cans}")
print(f"the number of 3.6 liter gallons you need is {gallon_paint} and the total value is {total_value_gallons}")

#incompleto