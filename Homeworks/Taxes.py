try:    
    grossSalary = float(input("Enter the gross salary: "))
    if grossSalary < 1000:
        tax = 0.10
        child = 0.01
    elif grossSalary < 2000:
        tax = 0.12
        child = 0.01
    elif grossSalary < 4000:
        tax = 0.14
        child = 0.005
    elif grossSalary >= 4000:
        tax = 0.18
        child = 0.005
    childNum = int(input("Enter the number of children you have: "))
    finalTax = tax - (child * childNum)
    netSalary = grossSalary * (1 - finalTax)
    if netSalary > grossSalary:
        netSalary = grossSalary
    print(f"Your net salary is {netSalary}, due to your tax rate of {tax} and {childNum} children.")
except:
    print("Invalid input. Please enter a integer for children and a float for salary.")
    