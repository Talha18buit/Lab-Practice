#code for PC invalid password and try again limit
correct_password = "qwerty"
enter_password = ""
password_limit = 5
password_enter = 0
out_of_limits = False
while enter_password != correct_password and not(out_of_limits):
    if password_enter < password_limit:
        enter_password = input("ENTER YOUR PASSWORD: ")
        password_enter += 1
    else:
        out_of_limits = True
if out_of_limits:
    print("Want To Recover Login I,D : ")
    yes_no = None
    while yes_no not in ("yes","no"):
        yes_no = input("Please Enter yes OR no : ")
    if yes_no == "yes":
        recover_password = input("Enter Your Recovery Email : ")
        print("Check Your Email ")
    elif yes_no == "no":
        print("out of limit sorry ! ")
    else:
        print("Please Enter yes or no")

else:
    print("Login Verified")




