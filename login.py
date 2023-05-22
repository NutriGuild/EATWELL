class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        if entered_password == self.password:
            print("  Login successful!")
            return True
        else:
            print("  Incorrect password. Please try again.")
            return False

class RegisteredUser(User):
    def __init__(self, username, password, age, weight, height, sex):
        super().__init__(username, password)
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex

    def display_info(self):
        print("Username:", self.username)

def save_user_data(users):
    with open("users.txt", "w") as file:
        for user in users:
            file.write(
                f"{user.username}:{user.password}:{user.age}:{user.weight}:{user.height}:{user.sex}\n"
            )

def load_user_data():
    try:
        with open("users.txt", "r") as file:
            users = []
            for line in file:
                fields = line.strip().split(":")
                if len(fields) == 6:
                    username, password, age, weight, height, sex = fields
                    users.append(RegisteredUser(username, password, age, weight, height, sex))
                else:
                    print(f"Ignoring line: {line}")
            return users
    except FileNotFoundError:
        return []

def main():
    registered_users = load_user_data()

    while True:
        print("+", "=" * 56, "+")
        print(f"{'EATWELL':^60}")
        print("+", "=" * 56, "+")
        print("  [1] Log In")
        print("  [2] Sign Up")
        print("  [3] Exit")
        choice = input("  Enter your choice: ")

        if choice == "1":
            print("\n+", "=" * 56, "+")
            print(f"{'Log In':^60}")
            print("+", "=" * 56, "+")
            username = input("  Enter your username: ")
            password = input("  Enter your password: ")

            matching_users = [user for user in registered_users if user.username == username]

            if matching_users:
                user = matching_users[0]
                if User(user.username, user.password).authenticate(password):
                    exec(open("nutriguild.py").read())
            else:
                print("  User not found!")

        elif choice == "2":
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

            registered_users.append(RegisteredUser(username, password, age, weight, height, sex))

            save_user_data(registered_users)
            print("  Registration successful!")

        elif choice == "3":
            print("\+", "=" * 56, "+")
            print(f"{'THANK YOU! EATWELL.':^60}")
            print("+", "=" * 56, "+")
            break

        else:
            print("  Invalid choice. Please try again.")

if __name__ == "__main__":
    main()