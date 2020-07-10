def get_percentage(x, round_digits=-1):
    if round_digits == -1:
        return f'{round(x * 100)}%'
    return f'{round(x * 100, round_digits)}%'
