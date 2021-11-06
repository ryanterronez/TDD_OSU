def check_pwd(password):
    password_length = len(password)
    if password == "" or password_length < 8 or password_length > 20:
        return False
    else:
        return True

