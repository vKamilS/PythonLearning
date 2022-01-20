def days_to_year_end():
    from datetime import date
    from datetime import timedelta

    date_today = date.today()
    days_difference = timedelta(days=25)
    
    current_year = date.today().year

    date_end_year = date(current_year, 12, 31)
    day = date_today + days_difference
    delta = date_end_year - day

    print("There are", delta.days, "to the end of the year", current_year)

days_to_year_end()
