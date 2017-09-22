import datetime


def print_header():
    print('-------------------------------------------')
    print('           When is your Birthday')
    print('-------------------------------------------')
    print()


def get_user_birthday():
    print('When were you born?')
    year = int(input('Enter the year [YYYY]? '))
    month = int(input('Enter the month [MM]? '))
    day = int(input('Enter the day [DD]? '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print('Your birthday was {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days'.format(days))
    else:
        print("Hey it's your Birthday! Happy Birthday!!!")


def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


main()
