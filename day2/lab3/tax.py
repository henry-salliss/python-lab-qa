def getIncomeTax(income):
    tax = 0
    if(income > 0 and income <= 34500):
        tax = income * 0.2
    elif(income > 34500 and income <= 150000):
        tax = income * 0.4
    elif(income > 150000):
        tax = income * 0.45

    return tax
    
total_income_tax = getIncomeTax(200000)

print(total_income_tax)
