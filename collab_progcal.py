# Calorie Tracking
class Calorie_Tracker:
    def __init__(self):
        self.age = []
        self.sex = []
        self.weight = []
        self.height = []
        self.height_to_m = []
        self.bmi = []
        self.cal_limit = 10
        self.bmr = None


    def user_info(self):
        while True:
            self.age = int(input("Age in years: "))
            self.weight = float(input("Weight in kilograms: "))
            self.height = float(input("Height in centimeters: "))
            self.height_m = self.height / 100  # convert height from cm to m
            self.sex = input("Sex (M or F): ")
            if self.sex == "M" or self.sex == "m":
                self.bmr = round(66.5 + (13.75 * self.weight) + (5.003 * self.height_m) - (6.75 * self.age), 2)
            elif self.sex == "F" or self.sex == "f":
                self.bmr = round(655.1 + (9.563 * self.weight) + (1.850 * self.height_m) - (4.676 * self.age), 2)
            else:
                print("INVALID!")

            self.bmi_formula = self.weight / (self.height_m ** 2)
            self.bmi = round(self.bmi_formula, 2)

            print(f"\nYour daily calorie needs are: {self.bmr}")
            print(f"Your Body Mass Index is: {self.bmi}")

            if self.bmi < 18.5:
                print("You are underweight.You need a Caloric Surplus.")
            elif self.bmi < 25:
                print("You are of normal weight. \nYou can maintain your Caloric Intake.")
            elif self.bmi < 30:
                print("You are overweight. You need a Caloric Deficit.")

            self.option = input("\n(B)ack: ")
            if self.option != "B" and self.option != "b":
                print("Invalid input. Please try again.")
            else:
                break

    def calorie_intake(self):
        while True:
            print(f"\nThe calorie you need today is {self.bmr}.")
            self.cal_limit = self.bmr
            self.cal_intake = float(input("\nPlease enter your caloric intake for the day: "))
            self.diff = round(self.bmr - self.cal_intake, 2)

            if self.cal_intake <= self.cal_limit:
                print(f"You still have {self.diff} calorie for the day. But, well done!")
            elif self.cal_intake > self.cal_limit:
                print("You have exceeded your caloric intake!")

            self.option = input("\n(B)ack: ")
            if self.option != "B" and self.option != "b":
                print("Invalid input. Please try again.")
            else:
                break

#Water Intake
class Water_Tracker:
    def __init__(self):
        self.water_amount = 0

    def waterintake(self):
        while True:
            self.water_intake = int(input("Number of glasses: "))
            self.water_amount += self.water_intake
            self.option = input("\n(B)ack: ")
            if self.option != "B" and self.option != "b":
                print("Invalid input. Please try again.")
            else:
                break


#View Progress
class Progress(Calorie_Tracker, Water_Tracker):
    def __init__(self):
        self.total_water_intake = 0
        self.total_calories = 0
        self.date = []
        self.cal_intake = []
        self.water_take = []
        self.water_amount = 0
    def view_progress(self):

        self.total_calories = sum(self.cal_intake)
        self.total_water_intake += self.water_intake

        print("\nProgress Report")
        print(f"Total calories consumed: {self.total_calories}")
        print(f"Total water intake: {self.total_water_intake} glass of water")
        """ print(f"Food taken: {self.foods_for_progress} ")
        for i in range(len(self.date)):
            print(f"{self.date[i]}: {self.foods_for_progress[i]} ({self.calories[i]} calories)")"""

        while True:
            self.option = input("\n(B)ack:  ")
            if self.option != "B" and self.option != "b":
                print("Invalid input. Please try again.")
            else:
                break


def main():
    progress = Progress()

    while True:
        print("[U]ser")
        print("[C]alorie Intake")
        print("[W]ater Intake")
        print("[P]rogress")
        print("[B]ack")

        the_choice = input("Enter an action: ")
        if the_choice == "U" or the_choice == "u":
            print("\n---------------- User ----------------")
            progress.user_info()
        elif the_choice == "C" or the_choice == "c":
            print("\n----------- Calorie Intake -----------")
            progress.calorie_intake()
        elif the_choice == "W" or the_choice == "w":
            print("\n------------ Water Intake ------------")
            progress.waterintake()
        elif the_choice == "P" or the_choice == "p":
            print("\n----------- View Progress -----------")
            progress.view_progress()
        elif the_choice == "B" or the_choice == "b":
            break
        else:
            print("Invalid. Try again.")


if __name__ == "__main__":
    main()
