file = open('./day2/lab3/data.txt')

records = []
companies = []
company_sales = []
for record in file:
    if(record[0].isdigit()):
        formatted_record = record.replace('\n', '').split(',')
        int_record = list(map(int, formatted_record))
        company_sales.append(int_record)
        company_yearly_sales = sum(int_record)
        records.append(company_yearly_sales)
    else:
        formatted_record = record.replace('\t\n', '')
        companies.append(formatted_record)


print(company_sales)

for x in range(8):
    total = 0
    for y in range(5):
        total = total + company_sales[y][x]
    print(total)



grand_total = sum(records)
string = ''

for i, company in enumerate(companies):
    message = f'{company} made £{records[i]} this year\n'
    string = string + message


print(string)
print(f'combined all companies made £{grand_total} this year')