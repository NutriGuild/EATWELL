class CalorieTracker:
    def __init__(self, goal):
        self.goal = goal
        self.total_calories = 0

    def track_calories(self, calories):
        self.total_calories += calories

    def check_progress(self):
        remaining_calories = self.goal - self.total_calories
        if remaining_calories > 0:
            print(f"  You are {remaining_calories} calories away from your goal.")
        elif remaining_calories == 0:
            print("  Congratulations! You have reached your calorie goal.")
        else:
            excess_calories = abs(remaining_calories)
            print(f"  You have exceeded your calorie goal by {excess_calories} calories.")

    def reset_tracker(self):
        self.total_calories = 0
        print("  Tracker has been reset.")

    def set_goal(self, goal):
        self.goal = goal
        print("  Goal has been set.")


def get_bmr_from_file(username):
    with open('users.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if parts[0] == username:
                return float(parts[6])
    return None


def get_progress_from_file(username):
    with open('calorie.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if parts[0] == username:
                return float(parts[1])
    return None


def save_progress(username, progress):
    with open('calorie.txt', 'a') as file:
        file.write(f"{username}:{progress}\n")


def main():
    print("\n")
    print("+", "=" * 56, "+")
    print(f"{'Calorie Tracking and Goal Setting':^60}")
    print("+", "=" * 56, "+")

    while True:
        username = input("  Enter your username: ")
        bmr = get_bmr_from_file(username)

        if bmr is None:
            print("  Username not found. Please try again.")
            continue

        tracker = CalorieTracker(bmr)
        update_bmr = False

        while True:
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Calorie Tracking and Goal Setting':^60}")
            print("+", "=" * 56, "+")
            print("  [1] Goal Setting")
            print("  [2] Track calories")
            print("  [3] Check progress")
            print("  [4] Reset tracker")
            print("  [5] Exit")

            choice = input("  Enter your choice: ")

            if choice == '1':
                print(f"  Your goal: {tracker.goal} calories")
            elif choice == '2':
                calories = float(input("  Enter the number of calories consumed: "))
                tracker.track_calories(calories)
                update_bmr = True
                print("  Calories tracked successfully.")
            elif choice == '3':
                tracker.check_progress()
                progress = get_progress_from_file(username)
            elif choice == '4':
                tracker.reset_tracker()
                update_bmr = True
            elif choice == '5':
                if update_bmr:
                    save_progress(username, bmr - tracker.total_calories)
                break
            else:
                print("  Invalid choice. Please try again.")

        break


if __name__ == '__main__':
    main()
