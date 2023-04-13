import datetime

# tuple 
pay_rates = (
    ('C', 16.50),
    ('S', 15.75),
    ('J', 15.75),
    ('M', 19.50)
)
# tuple
deduction_rates = (
    ('Federal Income Tax', 0.12),
    ('State Income Tax', 0.03),
    ('Social Security Tax', 0.062),
    ('Medicare Tax', 0.0145)
)

def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data ():
    global job_code, hours_worked
    job_code = input("Enter job category code (C, S, J, or M): ").upper()
    hours_worked = float(input("Enter number of hours worked: "))

def perform_calculations():
    global gross_pay, total_deductions, net_pay
    pay_rate = None
    for p in pay_rates:
        if p[0] == job_code:
            pay_rate = p[1]
            break

    if pay_rate is None:
        print("Invalid job category code")
    else:

        gross_pay = hours_worked * pay_rate

    
    total_deductions = 0
    for d in deduction_rates:
        deduction_name = d[0]
        deduction_rate = d[1]
        deduction_amount = gross_pay * deduction_rate
        total_deductions += deduction_amount
        print('{} $ {:>10,.2f}'.format(deduction_name + ':', deduction_amount))

    # net pay
    net_pay = gross_pay - total_deductions

def display_results ():
    print('\n-----------------------------------------')
    print("ABC Company Payroll Summary")
    print('\n-----------------------------------------')
    print('Number of Hours Worked' + format(hours_worked,'10,.2f'))
    print('Gross Pay        $ ' + format(gross_pay,'10,.2f'))
    print('Total Deductions $ ' + format(total_deductions,'10,.2f'))
    print('Net Pay          $ ' + format(net_pay,'10,.2f'))
    print('\n----------------------------------------')
    print(datetime.datetime.now())
main ()
