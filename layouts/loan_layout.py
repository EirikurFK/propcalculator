import PySimpleGUI as sg

max_loan_ = 50000000
val = 50000000

ib: dict = {"size":(10,1), "font":("Helvetica", 18)}
dt: dict = {"size":(20,1), "font":("Helvetica", 12)}
dst: dict = {"font":("Helvetica", 12)}
ds: dict = {"size":(20,10), "range":(0,200000000), "default_value": val, "orientation": "horizontal",
"tick_interval": "200000000", "resolution": "100000", "disable_number_display": True}

loan_layout = [
    [sg.Text("Max loan: ", **dt), sg.Text(0, key= "_property_max_loan_", **dt)],
    [sg.Text("Loan Amount", **dt), sg.Text("Down Payment", **dt)],
    [sg.InputText(val, **dt, enable_events= True, key="_loan_amount_text_"),
    sg.InputText(val, **dt, enable_events= True, key="_down_payment_text_")],
    [sg.Slider(**ds, key= "_loan_amount_slider_", enable_events= True),
    sg.Slider(**ds, key= "_down_payment_slider_", enable_events= True)],
    [sg.Text("Loan Years", **dst, size= (10,1)), sg.Text("Base Loan Interest", **dst), sg.Text("Supplementary Loan Interest", **dst)],
    [sg.Combo([num for num in range(1, 41)], default_value=40, size=(3,1), font=("Helvetica", 14), key="_loan_years_"),
    sg.InputText(**ib, key= "_base_loan_interest_", default_text=3.54), sg.InputText(**ib, key= "_sup_loan_interest_", default_text=4.84)],
    [sg.Button("Calculate Monthly Payment")],
    [sg.Text("Monthly Payment is: ", **dt), sg.Text(0, key= "_property_monthly_payment_", **dt)]
]