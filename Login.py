from User import UserClass


class Login:
    __db = []

    def __init__(self):
        self.print_menu()

    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def email_validation(self, email):
        if email[0] in "qwertyuiopasdfghjklzxcvbnm":
            return True
        else:
            return False

    def check_credentials(self, email):
        if self.email_validation(email):
            if "@" in email:
                domain = ["gmail.com", "outlook.com", "yahoo.com"]
                temp, do = email.split("@")
                if do in domain:
                    return True
                else:
                    return False
            else:
                return False

    def password_validation(self, password):
        l, u, p, d = 0, 0, 0, 0
        capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets = "abcdefghijklmnopqrstuvwxyz"
        specialchar = "$@_"
        digits = "0123456789"
        if len(password) >= 8:
            for i in password:
                if i in smallalphabets:
                    l += 1
                if i in capitalalphabets:
                    u += 1
                if i in digits:
                    d += 1
                if i in specialchar:
                    p += 1
        if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(password):
            return "Valid password"
        else:
            return "Invalid Password"

    def create_user(self, name, email, password):
        if self.check_credentials(email):
            new_user = UserClass(name, email, password)
            self.__db.append(new_user)
            print(self.__db)
            return True

    def validate_user(self, email, password):
        temp = self.__db.copy()
        for user_obj in temp:
            if email in user_obj.email:
                if password in user_obj.get_user_password():
                    return f"Welcome Back"
                else:
                    return f"Wrong Credentials"
        return f"Wrong Credentials"


def main():
    obj = Login()
    while True:
        option = input("Enter your choice: ")
        if option == '1':
            name = input("Enter your full name: ")
            email = input("Enter Email: ")
            check = obj.check_credentials(email)
            if not check:
                print("You have entered wrong credentials")
            if obj.check_credentials(email):
                password = input("Create Password: ")
                print(obj.password_validation(password))
                res = obj.create_user(name, email, password)
                if res is True:
                    print("User created successfully")
                else:
                    print("User Registration Failed")
        elif option == '2':
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            print(obj.validate_user(email, password))
        elif option == '3':
            break
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
