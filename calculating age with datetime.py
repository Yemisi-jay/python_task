from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

print(calculate_age(date(1960, 10, 1)), "years")

def age_calculating(birth_date):
    days_in_years = 365.2425
    age = int((date.today() - birth_date).days / days_in_years)
    return age

print(age_calculating(date(1960, 10, 1)), "years")
