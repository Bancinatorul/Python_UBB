"""
Determine a calendar date (as year, month, day) starting from two integer numbers representing the year
and the day number inside that year (e.g. day number 32 is February 1st).
Take into account leap years. Do not use Python's inbuilt date/time functions.
"""

def leap_year(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)

def determine_the_date(num, months):
    for i in months:
        if months[i] < num:
            num -= months[i]
        else:
            return num, i

if __name__ == "__main__":
    all_months = {'January': 31, 'February': 0, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    while True:
        number = int(input("Give the number you want to determine as a date: "))
        year = int(input("Give the year: "))
        if number <= 0 or year <= 0:
            print("Invalid date!")
        else:
            break
    while True:
        if leap_year(year):
            all_months['February'] = 29
            days_in_year = 366
        else:
            days_in_year = 365
            all_months['February'] = 28
        if number > days_in_year:
            year += 1
            number -= days_in_year
        else:
            number, month = determine_the_date(number, all_months)
            break
    print(number, month, year)
