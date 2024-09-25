def calculate_salary(years_in_service, office):
    salary = 0  # Initialize salary

    if office == 'it':
        if years_in_service >= 10:
            salary = 10000
        else:
            salary = 5000
    elif office == 'acct':
        if years_in_service >= 10:
            salary = 12000
        else:
            salary = 6000
    elif office == 'hr':
        if years_in_service >= 10:
            salary = 15000
        else:
            salary = 7500
    else:
        print("Invalid office entered.")
        return

    print(f"The employee in {office.upper()} with {years_in_service} years of service has a salary of {salary}.")

try:
    years = int(input("Enter number of years in service: "))
    office = input("Enter office (it, acct, hr): ").lower()

 
    calculate_salary(years, office)

except ValueError:
    print("Invalid input! Please enter a valid number for years.")
