import calendar

def display_month_names():
    """
    Displays all month names.
    """
    for month_number in range(1, 13):
        month_name = calendar.month_name[month_number]
        print(month_name)

# Example usage:
display_month_names()