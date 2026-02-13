# User Login Check

def login_check(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login Successful"
    else:
        return "Invalid Credentials"


if __name__ == "__main__":
    print(login_check("admin", "1234"))
