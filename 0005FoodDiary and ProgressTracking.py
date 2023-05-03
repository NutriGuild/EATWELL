import datetime

class Food_Diary:
    def __init__(self):
        self.date = []
        self.meal = []
        self.food = []
        self.calorie = []
    @property
    def record_food(self):
        self.date_save = input("Enter the date (MM/DD/YYYY): ")
        try:
            self.date_obj = datetime.datetime.strptime(self.date_save, "%m/%d/%Y")
        except ValueError:
            print("Incorrect format. Try again!")
            return self.record_food()
        while True:
            self.meal_type = input("Which meal is it? [breakfast/lunch/dinner/snack]: "
                                   "\nfor ")
            if self.meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                break
            else:
                print("Invalid. Please enter a valid input.")
        self.food_like = input("What food: ")
        while True:
            try:
                self.calories_count = int(input("Enter the number of calories: "))
                break
            except:
                print("Invalid. Please enter a number.")

        self.date.append(self.date_save)
        self.meal.append(self.meal_type)
        self.food.append(self.food_like)
        self.calorie.append(self.calories_count)

        with open ("values.txt", "a") as file:
            file.write(f"{self.date_save}: {self.meal_type} - {self.food_like} ({self.calories_count} calories) \n")

        print("Recorded Succesfully.")
        return main()

    def view_diary(self):
        while True:
            with open('values.txt', 'r') as file:
                self.data_read = file.read()
                print(self.data_read)

            self.option = input("\n(D)elete \t(B)ack:  ")
            if self.option == "D" or self.option == "d":
                self.data_to_delete = input("Enter data to delete: ")
                with open('values.txt', 'r') as file:
                    self.lines = file.readlines()
                with open('values.txt', 'w') as file:
                    keyword_found = False
                    for line in self.lines:
                        if self.data_to_delete in line:
                            keyword_found = True
                            print("Data deleted. \n")
                            continue
                        file.write(line)
                    if not keyword_found:
                        print(f"'{self.data_to_delete}' not found in diary. \n")
            elif self.option == "B" or self.option == "b":
                break
            else:
                print("Invalid input. Please try again.")

class Progress:
    def __init__(self):
        self.foods_for_progress = []
        self.date = []
        self.calorie_take = []
        self.calories = []
        self.water_take = []
    def view_progress(self):
        while True:
            self.total_calories = sum(self.calorie_take)
            self.total_water_intake = sum(self.water_take)

            print("\nProgress Report")
            print(f"Total calories consumed: {self.total_calories}")
            print(f"Total water intake: {self.total_water_intake} glass of water")
            print(f"Food taken: {self.foods_for_progress} ")
            for i in range(len(self.date)):
                print(f"{self.date[i]}: {self.foods_for_progress[i]} ({self.calories[i]} calories)")

            self.option = input("\n(B)ack:  ")
            if self.option != "B" and self.option != "b":
                print("Invalid input. Please try again.")
            else:
                break


def main():
    my_diary = Food_Diary()
    my_progress = Progress()

    while True:
        print("\nMenu")
        print("1. Record Food")
        print("2. Food Diary")
        print("3. View Progress")
        print("4. Exit")
        main_choice = input("Enter action: ")

        if main_choice == "1":
            print("\n----------------- Record Food -----------------")
            my_diary.record_food()
        elif main_choice == "2":
            print("\n")
            my_diary.view_diary()
        elif main_choice == "3":
            print("\n---------------- View Progress ----------------")
            my_progress.view_progress()
        elif main_choice == "4":
            print("\nExiting the program.")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()



