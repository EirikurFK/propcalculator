from math import log

MILLION = 10**6
LOAN_PERCENTAGE_1 = 0.7
LOAN_PERCENTAGE_2 = 0.80
LOAN_PERCENTAGE_3 = 0.85
MAX_LOAN_1 = 60 * MILLION


class Property:
    def __init__(self, size, market_value, evaluation):
        self.size = float(size)
        self.market_value = int(market_value)
        self.evaluation = int(evaluation)
        self.maintenance = int(evaluation) * 0.001
    
    def calc_available_max_loan(self, is_first_loan):
        if is_first_loan:
            if self.market_value >= 40 * MILLION:
                
                if self.market_value >= 85.7 * MILLION:
                    max_loan = self.market_value * LOAN_PERCENTAGE_1
                elif self.market_value >= 72.5 * MILLION:
                    max_loan = MAX_LOAN_1
                else:
                    loan_part_1 = 40 * MILLION * LOAN_PERCENTAGE_3
                    rest_of_market_value = self.market_value - 40 * MILLION
                    loan_part_2 = rest_of_market_value * LOAN_PERCENTAGE_2
                    max_loan = loan_part_1 + loan_part_2
            else:
                max_loan = self.market_value * LOAN_PERCENTAGE_3

        else:
            if self.market_value >= 85.7 * MILLION:
                max_loan = self.market_value * LOAN_PERCENTAGE_1
            elif self.market_value >= 75 * MILLION:
                max_loan = MAX_LOAN_1
            else:
                max_loan = self.market_value * LOAN_PERCENTAGE_2
    
        return round(max_loan)

    def calc_base_loan(self, loan_amount):
        loan_amount = loan_amount
        max_base_loan = LOAN_PERCENTAGE_1 * self.evaluation
        if loan_amount < LOAN_PERCENTAGE_1 * self.evaluation:
            base_loan = loan_amount
        else:
            base_loan = max_base_loan

        return round(base_loan)

    def calc_sup_loan(self, loan_amount):
        loan_amount = loan_amount
        sup_loan = loan_amount - self.calc_base_loan(loan_amount)
        if sup_loan > 0:
            return round(sup_loan)

        return 0

    def calc_total_loan(self, loan_amount):
        base_loan = self.calc_base_loan(loan_amount)
        sup_loan = self.calc_sup_loan(loan_amount)
        return {"b_loan": base_loan,
                "s_loan": sup_loan
        }

    def calc_rent(self):
        rent = 144403 * log(self.size) - 415264
        return round(rent)
    
    def calc_rent_profit(self):
        rent_after_tax = self.calc_rent() * 0.78
        rent_after_maintenance = rent_after_tax - self.maintenance
        return round(rent_after_maintenance)

    def calc_monthly_payment(self, loan_amount, loan_interest, loan_years):
        months = int(loan_years) * 12
        loan_interest = float(loan_interest) / 100
        loan_amount = int(loan_amount)

        monthly_interest = loan_interest / 12
        
        monthly_payment = (loan_amount * (monthly_interest * (1 + monthly_interest) ** months))/((1 + monthly_interest) ** months - 1)
        return round(monthly_payment)

