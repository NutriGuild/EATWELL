import datetime
import choice_4

total_calorie = choice_4.Calorie_Tracker

#Food Diary
class Food_Diary:
    def __init__(self):
        self.date = []
        self.meal = []
        self.food = []
        self.calorie = []
    @property
    def record_food(self):
        self.date_save = input("  Enter the date (MM/DD/YYYY): ")
        try:
            self.date_obj = datetime.datetime.strptime(self.date_save, "%m/%d/%Y")
        except ValueError:
            print("  Incorrect format. Try again!")
            return self.record_food()
        while True:
            self.meal_type = input("  Which meal is it? [breakfast/lunch/dinner/snack]: "
                                   "\n  for ")
            if self.meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                break
            else:
                print("  Invalid. Please enter a valid input.")

        self.food_like = input("  What food: ")
        while True:
            try:
                self.calories_count = int(input("  Number of calories: "))
                break
            except:
                print("  Invalid. Please enter a number.")

        self.date.append(self.date_save)
        self.meal.append(self.meal_type)
        self.food.append(self.food_like)
        self.calorie.append(self.calories_count)

        with open ("food_diary.txt", "a") as file:
            file.write(f"  {self.date_save}: {self.meal_type} - {self.food_like} ({self.calories_count} calories) \n")

        print("\n  Recorded Successfully!")
        return diaryandprogress()

    def view_diary(self):
        while True:
            with open('food_diary.txt', 'r') as file:
                self.data_read = file.read()
                print(self.data_read)

            print("\n  [1] Delete")
            print("  [2] Back")
            self.option = input("  Enter choice: ")
            if self.option == "1":
                self.data_to_delete = input("  Enter data to delete: ")
                with open('food_diary.txt', 'r') as file:
                    self.lines = file.readlines()
                with open('food_diary.txt', 'w') as file:
                    keyword_found = False
                    for line in self.lines:
                        if self.data_to_delete in line:
                            keyword_found = True
                            print("  Data deleted.")
                            continue
                        file.write(line)
                    if not keyword_found:
                        print(f"  '{self.data_to_delete}' not found in diary.")
            elif self.option == "2" :
                break
            else:
                print("  Invalid input. Please try again.")


"""def user():
    username = input("Enter your username: ")
    user_found = False

    with open('users.txt', 'r') as file:
        for line in file:
            user_data = line.strip().split(':')
            if len(user_data) >= 6 and user_data[0] == username:
                user_found = True
                break

    if user_found:
        progress = Progress()
        progress.view_progress()
    else:
        print("Invalid username. Please try again.")"""

class Progress:
    def read_water_intake(self):
        water_intake = 0
        with open('users.txt', 'r') as file:
            for line in file:
                water_data = line.strip().split(':')
                water_intake += int(water_data[5])
        return water_intake

    def view_progress(self):
        while True:
            #total_calorie_intake = total_calorie.total_calorie_consumed(self)
            total_water_intake = self.read_water_intake()
            print("\n  Progress Report")
            #print(f"  Total calorie consumed: {total_calorie_intake}")
            print(f"  Total water intake: {total_water_intake} mL")

            option = input("\n  [1] Back:  ")
            if option == "1":
                break
            else:
                print("  Invalid input. Please try again.")


def diaryandprogress():
    diary = Food_Diary()
    progress = Progress()

    while True:
        print("+", "=" * 56, "+")
        print(f"{'Food Diary and Progress Tracking':^60}")
        print("+", "=" * 56, "+")
        print("  [1] Record Food")
        print("  [2] Food Diary")
        print("  [3] View Progress")
        print("  [4] Back")
        user_choice = input("  Enter choice: ")

        if user_choice == "1":
            print("\n+", "=" * 56, "+")
            print(f"{'Record Food':^60}")
            print("+", "=" * 56, "+")
            diary.record_food()
        elif user_choice == "2":
            print("\n+", "=" * 56, "+")
            print(f"{'Food Diary':^60}")
            print("+", "=" * 56, "+")
            diary.view_diary()
        elif user_choice == "3":
            print("\n+", "=" * 56, "+")
            print(f"{'View Progress':^60}")
            print("+", "=" * 56, "+")
            progress.view_progress()
        elif user_choice == "4":
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    diaryandprogress()



