def check_pwd(password):
    password_length = len(password)
    password_lowercase_list = [c for c in password if c.islower()]
    password_uppercase_list = [c for c in password if c.isupper()]
    password_integer_list = [c for c in password if c.isdigit()]
    approved_symbols = "~`!@#$%^&*()_+-=]"
    password_approved_symbols = [c for c in password if c in approved_symbols]
    if password == "" or password_length < 8 or password_length > 20\
            or not password_lowercase_list or not password_uppercase_list\
            or not password_integer_list or not password_approved_symbols:
        return False
    else:
        return True

