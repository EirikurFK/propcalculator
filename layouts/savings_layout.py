import PySimpleGUI as sg

dt: dict = {"size":(20,1), "font":("Helvetica", 12)}

savings_layout = [
    [sg.Text("Savings Calculator")],
    [sg.Text("Your current amount", **dt)],
    [sg.InputText(**dt, key="_current_amount_")],

    [sg.Text("Savings per month", **dt)],
    [sg.InputText(**dt, key="_month_savings_")],

    [sg.Text("Saving interest", **dt)],
    [sg.InputText(**dt, key="_savings_interest_")],

    [sg.Text("Years", **dt)],
    [sg.InputText(**dt, key="_saving_years_")],

    [sg.Button("Calculate Savings")],
    [sg.Text("Total savings are: ", **dt), sg.Text(0, key= "_total_savings_", **dt)]
]