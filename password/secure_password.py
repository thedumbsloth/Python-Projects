secure = (("jinny","stfu"),('a','@'),('h','#'),('v','^'),('and','&'),('123','()'),('o','O'),('i','!'),)

def secure_password(password):
    for a,b in secure:      
        password = password.replace(a,b)
    return password

if __name__ == "__main__":
    password = input("Enter your password\n")
    password = secure_password(password)
    print(f"Your secure password is {password}")

