import calendar

def get_day_of_week(year, month, day):
    # Get the day of the week as an integer (0=Monday, 6=Sunday)
    day_of_week = calendar.weekday(year, month, day)
    
    # Convert the integer to the corresponding day name
    day_name = calendar.day_name[day_of_week]
    
    return day_name

if __name__ == '__main__':
    # Read input values for year, month, and day
    year, month, day = map(int, input().split())
    
    # Get the day of the week
    result = get_day_of_week(year, month, day)
    
    # Print the result
    print(result)
