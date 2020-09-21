from math import log
year_work = int(input("Enter in the year you start working: "))
living_costs = int(input("Enter in your living costs: "))
years_children_are_born = []
children = int(input("Enter how many children you're going to have: "))
for child in range(1, children + 1):
    year_child = int(input(f"Enter the year of birth of child {child}: "))
    years_children_are_born.append(year_child)

f = open("mortgageplan.txt", "w+")

def car_cost():
    price
    age
    if age > 7:

def write_to_txt():
    f.write(f"{year}: Eiki's salary: {eiki_salary}.\n")
    f.write(f"{year}: Hildur's salary: {hildur_salary}.\n")
    f.write(f"{year}: Total money after tax: {money_after_tax}.\n")
    f.write(f"{year}: Child expenses: {child_expense}.\n")
    f.write(f"{year}: Total money after tax and child expenses: {salary_minus_child_costs}.\n")
    f.write(f"{year}: Living costs: {living_costs}.\n")
    f.write(f"{year}: {round(percentage * 100)}%.\n")
    f.write(f"{year}: Total available for mortgage: {mortgage_payment}.\n")
    f.write("\n")

def e_salary(experience):
    salary = round(-832.47 * experience**2 + 37335 * experience + 736033)
    return salary

def h_salary(experience):
    salary = round(-237.24 * experience**2 + 10194 * experience + 460986)
    return salary

def remove_tax(sal):
    discount = 54628
    savings = sal * 0.08
    salary_for_tax = sal - savings

    tax1 = 336916 * 0.3504
    tax2 = (945873 - 335916) * 0.3719
    tax_step_2 = salary_for_tax - 336916
    tax_step_3 = salary_for_tax - 945873

    if sal <= 336916:
        salary_after_tax = salary_for_tax * 0.3504
    elif sal <= 945873:
        salary_after_tax = salary_for_tax - tax1 - tax_step_2 * 0.3719
    elif sal > 945873:
        salary_after_tax = salary_for_tax - tax1 - tax2 - tax_step_3 * 0.4624

    return round(salary_after_tax) + discount


def property_expenses(apartment_cost):
    expenses = 0.001 * apartment_cost
    return expenses


def child_expenses(age):
    if age > 21:
        return 0
    elif age > 18:
        return 100000
    elif age >= 0:
        return 150000


def child_ages(year, years_of_birth):
    ages = []
    for year_of_birth in years_of_birth:
        year_of_birth = int(year_of_birth)
        age = year - year_of_birth
        if age < 0:
            pass
        else:
            ages.append(age)
    return ages


def total_child_expenses(year, years_of_birth):
    ages = child_ages(year, years_of_birth)
    expenses = 0
    for age in ages:
        expenses += child_expenses(age)
    return expenses


def total_salary_after_tax(sal1, sal2):
    eiki_salary_after_tax = round(remove_tax(eiki_salary))
    hildur_salary_after_tax = round(remove_tax(hildur_salary))
    return eiki_salary_after_tax + hildur_salary_after_tax


for year in range(year_work, 2070, 2):
    experience = year - year_work
    eiki_salary = e_salary(experience)
    hildur_salary = h_salary(experience)

    money_after_tax = total_salary_after_tax(eiki_salary, hildur_salary)

    child_expense = total_child_expenses(year, years_children_are_born)

    salary_minus_child_costs = money_after_tax - child_expense

    mortgage_payment = salary_minus_child_costs - living_costs

    percentage = 1 - (child_expense + living_costs)/money_after_tax

    write_to_txt()

f.close()