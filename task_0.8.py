def hours_and_minutes(number):
    hours = number // 60
    minutes = number % 60

    if hours > 1 or hours == 0:
        if minutes > 1 or minutes == 0:
            return f"{hours} hours, {minutes} minutes"
        else:
            return f"{hours} hours, {minutes} minute"
    else:
        if minutes > 1 or minutes == 0:
            return f"{hours} hour, {minutes} minutes"
        else:
            return f"{hours} hour, {minutes} minute"
