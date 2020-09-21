import PySimpleGUI as sg

max_loan_ = 50000000
val = 50000000

dt: dict = {"size":(20,1), "font":("Helvetica", 12)}
ds: dict = {"size":(20,10), "range":(0,200000000), "default_value": val, "orientation": "horizontal",
"tick_interval": "200000000", "resolution": "100000", "disable_number_display": True}
dss: dict = {"range":(0,300), "default_value": 100, "orientation": "horizontal", "tick_interval": "40",
"size":(35, 10)}

property_layout = [
    [sg.Text("Property Calculator")],
    [sg.Text("Property Market Value", **dt)],
    [sg.InputText(val, **dt, enable_events= True, key="_property_market_value_text_")],
    [sg.Slider(**ds, key= "_property_market_value_slider_", enable_events= True)],

    [sg.Text("Property Evaluation", **dt)],
    [sg.InputText(val, **dt, enable_events= True, key="_property_evaluation_text_")],
    [sg.Slider(**ds, key= "_property_evaluation_slider_", enable_events= True)],

    [sg.Text("Size", **dt)],
    [sg.Slider(**dss, key= "_property_size_")],

    [sg.Checkbox("First property", **dt, key= "_is_first_property_")],

    [sg.Button("Calculate Rent Profit")],
    [sg.Text("Rent profit is: ", **dt), sg.Text(0, key= "_property_rent_profit_", **dt)]
]