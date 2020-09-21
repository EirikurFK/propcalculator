from layouts.property_layout import *
from layouts.loan_layout import *
import PySimpleGUI as sg
from functions.class_property import Property
from math import log

def update_values(new_value, *keys):
    ''' Update values an event '''
    for key in keys:
        window[f'{key}'].update(value= "{:,}".format(new_value))

def update_slider_or_text(key):
    text = key.replace("slider", "text")
    slider = key.replace("text", "slider")

    if "slider" in key:
        update_values("{:,}".format(values[key]), text)
    elif "text" in key:
        update_values(values[key], slider)
        

layout = [
    [sg.TabGroup([[sg.Tab("Property", property_layout), sg.Tab("Loan", loan_layout)]])]
]

window = sg.Window("Property Calculator", layout, size= (640, 480))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    prop = Property(values["_property_size_"], values["_property_market_value_slider_"], values["_property_evaluation_slider_"])
    if event == "Calculate Rent Profit":
        prop_rent_profit = prop.calc_rent_profit()
        update_values(prop_rent_profit, "_property_rent_profit_")

    if event == "Calculate Monthly Payment":
        total_loan = prop.calc_total_loan(int(values["_loan_amount_text_"]))
        base_monthly_payment = prop.calc_monthly_payment(total_loan["b_loan"], values["_base_loan_interest_"], values["_loan_years_"])
        sup_monthly_payment = prop.calc_monthly_payment(total_loan["s_loan"], values["_sup_loan_interest_"], values["_loan_years_"])
        monthly_payment = base_monthly_payment + sup_monthly_payment
        update_values(monthly_payment, "_property_monthly_payment_")

    if event == "_property_market_value_slider_":
        update_slider_or_text(event)
        prop_max_loan = prop.calc_available_max_loan(values["_is_first_property_"])

        update_values(prop_max_loan, "_property_max_loan_", "_loan_amount_text_", "_loan_amount_slider_")

    if event == "_property_market_value_text_":
        update_slider_or_text(event)
        prop_max_loan = prop.calc_available_max_loan(values["_is_first_property_"])

        update_values(prop_max_loan, "_property_max_loan_", "_loan_amount_text_", "_loan_amount_slider_")

    if event == "_property_evaluation_slider_":
        update_slider_or_text(event)

    if event == "_property_evaluation_text_":
        update_slider_or_text(event)

    if event == "_loan_amount_text_" or "_loan_amount_slider_":
        update_values("{:,}".format(values["_loan_amount_text_"]), "_loan_amount_slider_")
        update_values(values["_property_market_value_text_"] - values["_loan_amount_text_"], "_down_payment_text_", "_down_payment_slider_")

    if event == "_down_payment_text_" or event == "_down_payment_slider_":
        update_slider_or_text(event)
        update_values(values["_property_market_value_text_"] - values["_down_payment_text_"], "_loan_amount_text_", "_loan_amount_slider_")

window.close()