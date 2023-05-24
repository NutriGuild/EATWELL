def calculate_bmr(age, weight, height, sex):
    if sex.upper() == "M":
        bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    elif sex.upper() == "F":
        bmr = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
    else:
        bmr = 0
    return bmr

def view_info(username):
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6 and user_data[0] == username:
                print("\n")
                print("+", "=" * 56, "+")
                print(f"{'View Info':^60}")
                print("+", "=" * 56, "+")
                print("  Username:", user_data[0])
                print("  Password:", user_data[1])
                print("  Age:", user_data[2])
                print("  Weight:", user_data[3])
                print("  Height:", user_data[4])
                print("  Sex:", user_data[5])
                bmr = calculate_bmr(int(user_data[2]), int(user_data[3]), int(user_data[4]), user_data[5])
                return True
        else:
            print("  User not found.")
            return False


def update_info(username):
    updated_data = []
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6 and user_data[0] == username:
                print("\n  Enter updated information:")
                new_username = input("  Username: ")
                password = input("  Password: ")
                while True:
                    try:
                        age = int(input("  Age: "))
                        break
                    except:
                        print("  Invalid input. Please enter a valid age.")
                while True:
                    try:
                        weight = int(input("  Weight(kg): "))
                        break
                    except:
                        print("  Invalid input. Please enter a valid weight.")

                while True:
                    try:
                        height = int(input("  Height(cm): "))
                        break
                    except:
                        print("  Invalid input. Please enter a valid height.")
                while True:
                    sex = input("  Sex(M/F): ")
                    if sex.upper() == "M" or sex.upper() == "F":
                        break
                    else:
                        print("  Invalid input. M/F only.")
                bmr = calculate_bmr(age, weight, height, sex)
                updated_data.append(':'.join(
                    [new_username, password, str(age), str(weight), str(height), str(sex), str(bmr), '0']) + '\n')
            else:
                updated_data.append(line)

    with open('users.txt', 'w') as file:
        file.writelines(updated_data)
        print("  Information updated successfully.")

    update_calorie_file()


def update_calorie_file():
    with open('users.txt', 'r') as file:
        users = []
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6:
                username = user_data[0]
                bmr = user_data[6]
                users.append(username + ':' + bmr + '\n')

    with open('calorie.txt', 'w') as file:
        file.writelines(users)


def users_info():
    while True:
        print("\n")
        print("+", "=" * 56, "+")
        print(f"{'User Info':^60}")
        print("+", "=" * 56, "+")
        username = input("  Enter your username: ")

        print("  [1] View Info")
        print("  [2] Exit")

        choice = input("  Enter your choice: ")

        if choice == '1':
            if view_info(username):
                print("\n  [1] Update Info")
                print("  [2] Exit")
                option = input("  Enter your choice: ")
                if option == "1":
                    update_info(username)
                    while True:
                        print("\n  [1] Back")
                        print("  [2] Exit")
                        option = input("  Enter your choice: ")
                        if option == "1":
                            break
                        elif option == "2":
                            return
                        else:
                            print("  Invalid choice. Please try again.")
                elif option == "2":
                    break
                else:
                    print("  Invalid choice. Please try again.")
            else:
                print("\n  [1] Back")
                print("  [2] Exit")
                option = input("  Enter your choice: ")
                if option == "1":
                    continue
                elif option == "2":
                    break
                else:
                    print("  Invalid choice. Please try again.")
        elif choice == '2':
            break
        else:
            print("  Invalid choice. Please try again.")

if __name__ == "__main__":
    users_info()