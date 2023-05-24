class WaterTracker:
    def __init__(self, limit):
        self.limit = limit
        self.total_water = 0

    def track_water(self, amount):
        self.total_water += int(amount)

    def check_progress(self):
        print(f"  Total water intake: {self.total_water} / 1896 ml")

    def check_goal_achievement(self):
        if self.total_water >= self.limit:
            print("  Congratulations! You have reached your water intake goal.")
        else:
            remaining_water = self.limit - self.total_water
            print(f"  You are {remaining_water} ml away from your goal.")

    def reset_tracker(self):
        self.total_water = 0
        print("  Tracker has been reset.")


def get_progress_from_file(username):
    with open('water.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if parts[0] == username:
                return float(parts[1])
    return None


def save_progress(username, progress):
    with open('water.txt', 'a') as file:
        file.write(f"{username}:{progress}\n")


def main():
    print("\n")
    print("+", "=" * 56, "+")
    print(f"{'Water Intake Tracking':^60}")
    print("+", "=" * 56, "+")

    while True:
        username = input("  Enter your username: ")
        tracker = WaterTracker(1896)  # Set the water intake goal to 1896 ml
        update_progress = False

        while True:
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Water Intake Tracking':^60}")
            print("+", "=" * 56, "+")
            print("  [1] Track water intake")
            print("  [2] Check progress")
            print("  [3] Check goal achievement")
            print("  [4] Reset tracker")
            print("  [5] Exit")

            choice = input("  Enter your choice: ")

            if choice == '1':
                amount = input("  Enter the amount of water consumed (ml): ")
                tracker.track_water(amount)
                update_progress = True
                print("  Water intake tracked successfully.")
            elif choice == '2':
                tracker.check_progress()
                progress = get_progress_from_file(username)
            elif choice == '3':
                tracker.check_goal_achievement()
            elif choice == '4':
                tracker.reset_tracker()
                update_progress = True
            elif choice == '5':
                if update_progress:
                    save_progress(username, tracker.total_water)
                break
            else:
                print("  Invalid choice. Please try again.")

        break


if __name__ == '__main__':
    main()
