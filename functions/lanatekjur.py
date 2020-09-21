# This program should calculate how much profit renting out an apartment will give you
# The tax is 22%
# An apartment valued at 29 million costs 195k per month
# An apartment valued at 36 million costs 220k per month
# An apartment valued at 37 million costs 220k per month
# An apartment valued at 39 million costs 240k per month
# An apartment valued at 44 million costs 280k per month
# Square Meters to rent is 128906ln(x) - 333435
# Apartment value is the monthly payment * 165

import math
square_meters = int(input("Enter the size of the apartment (sqm): "))
rent = 144403 * math.log(square_meters) - 415264
rent_after_tax = rent * 0.78
apartment_value = square_meters * 400000
apartment_monthly_maintenance = apartment_value * 0.001
income = int(rent_after_tax - apartment_monthly_maintenance)
print(f"An apartment that is {square_meters} square meters large, your monthly income will be {income} kr.")