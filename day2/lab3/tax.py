def getIncomeTax(income):
    taxable_income = income - 13500
    tax = 0
    if(taxable_income < 0):
        tax = 0
    elif(taxable_income > 0 and taxable_income <= 34500):
        tax = taxable_income * 0.2
    elif(taxable_income > 34500 and taxable_income <= 150000):
        tax = taxable_income * 0.4
    elif(taxable_income > 150000):
        tax = taxable_income * 0.45

    return tax
    
total_income_tax = getIncomeTax(200000)

print(total_income_tax)
