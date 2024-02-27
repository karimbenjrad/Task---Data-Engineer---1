from re import sub

def camelcase_to_snakecase(s):
    """
    Convert CamelCase to snake_case
    """
    s = sub('([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower()
