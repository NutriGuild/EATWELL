# ❗❗❗ FIRST CHECK THE "api.txt" FILE. REMOVE THE WORD "EATWELL" TO ENABLE THE API KEY.
# ❗❗❗ FIRST CHECK THE "api.txt" FILE. REMOVE THE WORD "EATWELL" TO ENABLE THE API KEY.
# ❗❗❗ FIRST CHECK THE "api.txt" FILE. REMOVE THE WORD "EATWELL" TO ENABLE THE API KEY.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        if entered_password == self.password:
            print("  Log In successful!")
            return True
        else:
            print("  Incorrect password. Please try again.\n\n")
            return False


class RegisteredUser(User):
    def __init__(self, username, password, age, weight, height, sex, bmr):
        super().__init__(username, password)
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.bmr = bmr

    def display_info(self):
        print("Username:", self.username)


def calculate_bmr(age, weight, height, sex):
    if sex.upper() == "M":
        bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    elif sex.upper() == "F":
        bmr = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
    else:
        bmr = 0
    return bmr


def save_user_data(users):
    with open("users.txt", "w") as file:
        for user in users:
            file.write(
                f"{user.username}:{user.password}:{user.age}:{user.weight}:{user.height}:{user.sex}:{user.bmr}:0\n")


def save_bmr(username, bmr):
    with open("calorie.txt", "a") as file:
        file.write(f"{username}:{bmr}\n")


def save_water(username):
    with open("water.txt", "a") as file:
        file.write(f"{username}:0\n")


def load_user_data():
    with open("users.txt", "r") as file:
        users = []
        for line in file:
            fields = line.strip().split(":")
            if len(fields) == 8:
                username, password, age, weight, height, sex, bmr, water = fields
                users.append(
                    RegisteredUser(username, password, age, weight, height, sex, bmr)
                )
                save_bmr(username, bmr)
                save_water(username)
        return users


def login():
    registered_users = load_user_data()

    while True:
        print("+", "=" * 56, "+")
        print(f"{'Embrace A Tasty, Well-balanced Eating Lifestyle':^60}")
        print(f"{'(EATWELL)':^60}")
        print(f"{'A Nutritional Guide Software':^60}")
        print("+", "=" * 56, "+")
        print("  System Notice:")
        print("      This system requires internet connectivity.")
        print("      Response rate will depend on the internet's speed.")
        print("      Please be patient.\n")
        print("  [1] Log In")
        print("  [2] Sign Up")
        print("  [3] Exit")
        choice = input("  Enter your choice: ")

        if choice == "1":
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Log In':^60}")
            print("+", "=" * 56, "+")
            username = input("  Enter your username: ")
            password = input("  Enter your password: ")

            matching_users = [user for user in registered_users if user.username == username]

            if matching_users:
                user = matching_users[0]
                if User(user.username, user.password).authenticate(password):
                    exec(open("main_menu.py").read())
            else:
                print("  User not found. Please try again.\n\n")

        elif choice == "2":
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Sign Up':^60}")
            print("+", "=" * 56, "+")
            username = input("  Enter a username: ")
            password = input("  Enter a password: ")
            while True:
                try:
                    age = int(input("  Enter your age: "))
                    break
                except:
                    print("  Invalid input. Please enter a valid age.")
            while True:
                try:
                    weight = int(input("  Enter your weight(kg): "))
                    break
                except:
                    print("  Invalid input. Please enter a valid weight.")

            while True:
                try:
                    height = int(input("  Enter your height(cm): "))
                    break
                except:
                    print("  Invalid input. Please enter a valid height.")

            while True:
                sex = input("  Enter your sex(M/F): ")
                if sex.upper() == "M" or sex.upper() == "F":
                    break
                else:
                    print("  Invalid input. M/F only.")

            bmr = calculate_bmr(age, weight, height, sex)

            registered_users.append(
                RegisteredUser(username, password, age, weight, height, sex, bmr))

            save_user_data(registered_users)
            save_bmr(username, bmr)
            save_water(username)

            print("  Sign Up successful!")
            print("\n")
        elif choice == "3":
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'THANK YOU! EATWELL.':^60}")
            print(f"{'-NutriGuild-':^60}")
            print("+", "=" * 56, "+")
            break
        else:
            print("  Invalid choice. Please try again.\n\n")


if __name__ == "__main__":
    login()
