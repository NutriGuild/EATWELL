def view_info(username):
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6 and user_data[0] == username:
                print("+", "=" * 56, "+")
                print(f"{'View Info':^60}")
                print("+", "=" * 56, "+")
                print("  Username:", user_data[0])
                print("  Password:", user_data[1])
                print("  Age:", user_data[2])
                print("  Weight:", user_data[3])
                print("  Height:", user_data[4])
                print("  Sex:", user_data[5])
                break
        else:
            print("  User not found.")


def update_info(username):
    updated_data = []
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6 and user_data[0] == username:
                print("+", "=" * 56, "+")
                print(f"{'Update Info':^60}")
                print("+", "=" * 56, "+")
                print("  Username:", user_data[0])
                print("  Password:", user_data[1])
                print("  Age:", user_data[2])
                print("  Weight:", user_data[3])
                print("  Height:", user_data[4])
                print("  Sex:", user_data[5])
                print("\n  Enter updated information:")
                new_username = input("  Username: ")
                password = input("  Password: ")
                age = input("  Age: ")
                weight = input("  Weight: ")
                height = input("  Height: ")
                sex = input("  Sex: ")
                updated_data.append(':'.join([new_username, password, age, weight, height, sex]) + '\n')
            else:
                updated_data.append(line)

    with open('users.txt', 'w') as file:
        file.writelines(updated_data)
        print("  Information updated successfully.")


def users_info():
    while True:
        print("+", "=" * 56, "+")
        print(f"{'User Info':^60}")
        print("+", "=" * 56, "+")
        username = input("  Enter your username: ")

        print("  [1] View Info")
        print("  [2] Update Info")

        choice = input("  Enter your choice: ")
        print("\n")

        if choice == '1':
            view_info(username)
            option = input("\n  [3] Back: ")
            if option != "3":
                print("  Invalid input. Please try again.")
            else:
                break
        elif choice == '2':
            update_info(username)
            option = input("\n  [3] Back: ")
            if option != "3":
                print("  Invalid input. Please try again.")
            else:
                break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    users_info()