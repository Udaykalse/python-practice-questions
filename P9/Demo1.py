def login (userName,password):
    if userName=='admin' and password=='12345':
        return "Login Successful"
    return "Invalid Credentials"

print(login('admin','12345'))