import datetime

# Food Diary
class Food_Diary:
    def __init__(self):
        self.date = []
        self.meal = []
        self.food = []

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

        self.date.append(self.date_save)
        self.meal.append(self.meal_type)
        self.food.append(self.food_like)

        with open("food_diary.txt", "a") as file:
            file.write(f"  {self.date_save}: {self.meal_type} - {self.food_like}\n")

        print("  Recorded Successfully!")

    def view_diary(self):
        while True:
            with open('food_diary.txt', 'r') as file:
                self.data_read = file.read()
                print(self.data_read)

            print("  [1] Delete")
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
                            print("  Data deleted.\n")
                            continue
                        file.write(line)
                    if not keyword_found:
                        print(f"  '{self.data_to_delete}' not found in diary.\n")
            elif self.option == "2":
                break
            else:
                print("  Invalid input. Please try again.")

    def diary(self):
        while True:
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Food Diary':^60}")
            print("+", "=" * 56, "+")
            print("  [1] Record Food")
            print("  [2] Food Diary")
            print("  [3] Exit")
            user_choice = input("  Enter choice: ")
            if user_choice == "1":
                print("\n")
                print("+", "=" * 56, "+")
                print(f"{'Record Food':^60}")
                print("+", "=" * 56, "+")
                self.record_food()
            elif user_choice == "2":
                print("\n")
                print("+", "=" * 56, "+")
                print(f"{'Food Diary':^60}")
                print("+", "=" * 56, "+")
                self.view_diary()
            elif user_choice == "3":
                break
            else:
                print("  Invalid action. Please try again.")


if __name__ == "__main__":
    diary = Food_Diary()
    diary.diary()
