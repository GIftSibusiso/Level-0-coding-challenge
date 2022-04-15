def hours_and_minutes(number):
    hours = number // 60
    minutes = number % 60

    if hours > 1:
        if minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif minutes == 0:
            return f"{hours} hours"
        else:
            return f"{hours} hours, {minutes} minute"
    else:
        if hours == 0:
            return f"{minutes} minutes"
        elif minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif minutes == 0:
            return f"{hours} hours"
        else:
            return f"{hours} hour, {minutes} minute"
