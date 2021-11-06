def check_pwd(password):
    password_length = len(password)
    password_lowercase_list = [c for c in password if c.islower()]
    password_uppercase_list = [c for c in password if c.isupper()]
    password_integer_list = [c for c in password if c.isdigit()]
    approved_symbols = "~`!@#^&*()_+-=]"
    password_approved_symbols = [c for c in password if c in approved_symbols]
    password_non_approved_characters = [c for c in password if c in password_lowercase_list and
                                        c in password_uppercase_list and c in password_integer_list
                                        and c in password_approved_symbols]
    password_non_approved_length = len(password_non_approved_characters)
    if password == "" or password_length < 8 or password_length > 20\
            or not password_lowercase_list or not password_uppercase_list\
            or not password_integer_list or password_length != password_non_approved_length:
        return False
    else:
        return True

