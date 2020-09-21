c = 0.0354/12
n = 60
L = 20000000
monthly_payment = L*(c*((1+c)**n))/(((1+c)**n)-1)
print(monthly_payment)