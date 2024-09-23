def calculate_salary(years_in_service, office):
    salary = 0  # Initialize salary

      if office == 'it':
        if years_in_service >= 10:
            salary = 10000
        else:
            salary = 5000
    elif office == 'acct':
        if years_in_service >= 10:
            salary = 9000
        else:
            salary = 4500
    elif office == 'hr':
        if years_in_service >= 10:
            salary = 8000
        else:
            salary = 4000
    else:
        print("Invalid office entered.")
        return

    print(f"The employee in {office.upper()} with {years_in_service} years of service has a salary of ${salary}.")
