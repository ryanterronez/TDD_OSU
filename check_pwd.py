def check_pwd(password):
    password_length = len(password)
    password_lowercase_list = [c for c in password if c.islower()]
    password_uppercase_list = [c for c in password if c.isupper()]
    password_integer_list = [c for c in password if c.isdigit()]
    if password == "" or password_length < 8 or password_length > 20\
            or not password_lowercase_list or not password_uppercase_list\
            or not password_integer_list:
        return False
    else:
        return True

