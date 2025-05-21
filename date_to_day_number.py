import datetime

def get_day_of_year(date_string):
    """
    Calculates the day number of the year for a given date string.

    Args:
        date_string: A string representing the date in "dd-mm-yyyy" format.

    Returns:
        An integer representing the day number of the year (1-366) if the
        input is valid, or an error message string otherwise.
    """
    error_message = "Invalid date format or value. Please use dd-mm-yyyy."
    try:
        # Preliminary format check for "dd-mm-yyyy" structure
        parts = date_string.split('-')
        if len(parts) != 3:
            return error_message
        
        day_str, month_str, year_str = parts
        
        if len(day_str) != 2 or len(month_str) != 2 or len(year_str) != 4:
            return error_message
        
        # Attempt to parse after basic format validation
        dt_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        return dt_object.timetuple().tm_yday
    except ValueError:
        # This will catch errors from strptime like invalid dates (e.g., "32-01-2023", "29-02-2023")
        # or if date_string passed basic checks but is still not a valid date recognized by strptime.
        return error_message

if __name__ == '__main__':
    user_input = input("Enter date (dd-mm-yyyy): ")
    result = get_day_of_year(user_input)
    if isinstance(result, int):
        print(f"The day number is: {result}")
    else:
        print(result)
