import math
# The formula for compounded interest is A = Pe^rt
# Money needs to be added to the total money amount every month while constantlycalculating the inflation
proceed = True
while proceed == True:
    current_balance = int(input("Type in your current balance: "))
    monthly_payment = int(input("Type in how much you want to save per month: "))
    years = float(input("Type in how many years you want to save: "))
    interest = float(input("Type in the interest in float: ")) - 1
    months = years * 12
    days = years * 360

# This calculates the monthly payments and their interest

    total_months = 0
    count_months = 1
    while count_months <= months:
        total_months += monthly_payment
        total_months += (total_months * math.e ** interest - total_months) / 12
        count_months += 1

    total_interest_months = total_months - months * monthly_payment
# This calculates the original balance and it's interest
    total_current = current_balance * math.e ** (interest * years)
    total_interest_current = total_current - current_balance
    total = total_current + total_months
    print("----------------------------------------------")
    print(f"Total interest aquired on monthly payments: {int(total_interest_months)}")
    print(f"Total monthly payment value: {int(total_months) - int(total_interest_months)}")
    print(f"Total saved with monthly payments: {int(total_months)}")
    print(f"Total interest aquired on original balance: {int(total_interest_current)}")
    print(f"Original balance with interest: {int(total_current)}")
    print(f"Total money saved over {years} years: {int(total)}")

    proceed = bool(input("Would you like to continue? "))