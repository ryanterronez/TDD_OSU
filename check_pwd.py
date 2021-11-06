def check_pwd(password):
    if password == "" or len(password) < 8:
        return False
    else:
        return True

