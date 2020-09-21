from layouts.property_layout import *
from layouts.loan_layout import *
import PySimpleGUI as sg
from functions.class_property import Property
from math import log

def update_value(key, new_value):
    ''' Update max loan value after an event '''
    window[f'{key}'].update(value= new_value)

def update_parameter(parameter, new_value):
    ''' Update max loan value after an event '''
    window[f'{key}'].update(value= new_value)

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
        update_value("_property_rent_profit_", prop_rent_profit)
    if event == "Calculate Monthly Payment":
        total_loan = prop.calc_total_loan(int(values["_loan_amount_text_"]))
        base_monthly_payment = prop.calc_monthly_payment(total_loan["b_loan"],
        values["_base_loan_interest_"], values["_loan_years_"])
        sup_monthly_payment = prop.calc_monthly_payment(total_loan["s_loan"],
        values["_sup_loan_interest_"], values["_loan_years_"])
        monthly_payment = base_monthly_payment + sup_monthly_payment
        update_value("_property_monthly_payment_", monthly_payment)
    if event == "_property_market_value_slider_":
        update_value("_property_market_value_text_", "{:,}".format(values["_property_market_value_slider_"]))
        prop_max_loan = prop.calc_available_max_loan(values["_is_first_property_"])
        update_value("_property_max_loan_", prop_max_loan)
        update_value("_loan_amount_text_", "{:,}".format(prop_max_loan))
        update_value("_loan_amount_slider_", "{:,}".format(prop_max_loan))
    if event == "_property_market_value_text_":
        update_value("_property_market_value_slider_", "{:,}".format(values["_property_market_value_text_"]))
        prop_max_loan = prop.calc_available_max_loan(values["_is_first_property_"])
        update_value("_property_max_loan_", prop_max_loan)
        update_value("_loan_amount_text_", "{:,}".format(prop_max_loan))
        update_value("_loan_amount_slider_", "{:,}".format(prop_max_loan))
    if event == "_property_evaluation_slider_":
        update_value("_property_evaluation_text_", "{:,}".format(values["_property_evaluation_slider_"]))
    if event == "_property_evaluation_text_":
        update_value("_property_evaluation_slider_", "{:,}".format(values["_property_evaluation_text_"]))
    if event == "_loan_amount_text_":
        update_value("_loan_amount_slider_", "{:,}".format(values["_loan_amount_text_"]))

        update_value("_down_payment_text_", "{:,}".format(values["_property_market_value_text_"] - values["_loan_amount_text_"]))
        update_value("_down_payment_slider_", "{:,}".format(values["_property_market_value_text_"] - values["_loan_amount_text_"]))

    if event == "_loan_amount_slider_":
        update_value("_loan_amount_text_", "{:,}".format(values["_loan_amount_slider_"]))

        update_value("_down_payment_text_", "{:,}".format(values["_property_market_value_text_"] - values["_loan_amount_slider_"]))
        update_value("_down_payment_slider_", "{:,}".format(values["_property_market_value_text_"] - values["_loan_amount_slider_"]))

    if event == "_down_payment_text_":
        update_value("_down_payment_slider_", "{:,}".format(values["_down_payment_text_"]))

        update_value("_loan_amount_text_", "{:,}".format(values["_property_market_value_text_"] - values["_down_payment_text_"]))
        update_value("_loan_amount_slider_", "{:,}".format(values["_property_market_value_text_"] - values["_down_payment_text_"]))

    if event == "_down_payment_slider_":
        update_value("_down_payment_text_", "{:,}".format(values["_down_payment_slider_"]))

        update_value("_loan_amount_text_", "{:,}".format(values["_property_market_value_text_"] - values["_down_payment_slider_"]))
        update_value("_loan_amount_slider_", "{:,}".format(values["_property_market_value_text_"] - values["_down_payment_slider_"]))
       
window.close()