from datetime import datetime

class Calorie_Tracker:
    def __init__(self):
        self.height_to_m = []
        self.bmi = []
        self.cal_limit = 10
        self.bmr = None
        self.user_data = None

    def user_info(self):
        while True:
            with open('users.txt', 'r') as file:
                for line in file:
                    self.user_data = line.strip().split(':')
                print(f"  Age: {self.user_data[2]}")
                print(f"  Weight in kilograms: {self.user_data[3]}")
                print(f"  Height in centimeters: {self.user_data[4]}")
                self.height_m = int(self.user_data[4]) / 100  # convert height from cm to m
                print(f"  Sex (M or F): {self.user_data[5]}")
                if self.user_data[5] == "M" or self.user_data[5] == "m":
                    self.bmr = round(
                        66.5 + (13.75 * int(self.user_data[3])) + (5.003 * self.height_m) - (
                                    6.75 * int(self.user_data[2])),
                        2)
                elif self.user_data[5] == "F" or self.user_data[5] == "f":
                    self.bmr = round(
                        655.1 + (9.563 * int(self.user_data[3])) + (1.850 * self.height_m) - (
                                    4.676 * int(self.user_data[2])),
                        2)
                else:
                    print("  INVALID!")

                self.bmi_formula = int(self.user_data[3]) / (self.height_m ** 2)
                self.bmi = round(self.bmi_formula, 2)

                print(f"\n  Your daily calorie needs are: {self.bmr}")
                print(f"  Your Body Mass Index is: {self.bmi}")

                if self.bmi < 18.5:
                    print("  You are underweight. You need a Caloric Surplus.")
                elif self.bmi < 25:
                    print("  You are of normal weight. You can maintain your Caloric Intake.")
                elif self.bmi < 30:
                    print("  You are overweight. You need a Caloric Deficit.")

                self.option = input("\n  [B]ack: ")
                if self.option.lower() != "b":
                    print("  Invalid input. Please try again.")
                else:
                    break

    def calorie_intake(self):
        while True:
            print(f"\n  The calorie you need today is {self.bmr}.")

            with open("calorie.txt", "a+") as file:
                file.seek(0)  # Move the file pointer to the beginning
                content = file.read()

                if self.user_data[0] in content:
                    user_entries = content.split('\n\n')
                    for entry in user_entries:
                        if self.user_data[0] in entry:
                            last_entry_lines = entry.strip().split('\n')
                            last_cal_intake = float(last_entry_lines[-2].split(":")[1].strip())
                            print(f"\n  Your last recorded caloric intake was: {last_cal_intake}")
                            break

                    self.cal_intake = float(input("\n  Please enter your caloric intake for the day: "))
                    self.diff = round(self.bmr - self.cal_intake, 2)
                    diff_last_recorded = round(self.diff - self.cal_intake, 2)

                    if self.cal_intake > self.bmr:
                        print("\n  You have exceeded your caloric intake!")
                    else:
                        print(f"  \nThe calorie you need more of is {diff_last_recorded}.")

                    file.write(f"\n{self.user_data[0]}:\n")
                    file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write(f"Caloric Intake: {self.cal_intake}\n")
                    file.write(f"Remaining Needed Calorie: {diff_last_recorded}\n")
                else:
                    self.cal_intake = float(input("\n  Please enter your caloric intake for the day: "))
                    self.diff = round(self.bmr - self.cal_intake, 2)

                    if self.cal_intake > self.bmr:
                        print("\n  You have exceeded your caloric intake!")
                    else:
                        print(f"  \nThe calorie you need more of is {self.diff}.")

                    file.write(f"\n{self.user_data[0]}:\n")
                    file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write(f"Caloric Intake: {self.cal_intake}\n")
                    file.write(f"Remaining Needed Calorie: {self.diff}\n")

            self.option = input("\n  [B]ack: ")
            if self.option.lower() != "b":
                print("  Invalid input. Please try again.")
            else:
                break


    def main(self):
        calorie = Calorie_Tracker()

        while True:
            print("\n+", "=" * 56, "+")
            print(f"{'Calorie Tracking and Goal Setting':^60}")
            print("+", "=" * 56, "+")
            print("  [G]oal Setting")
            print("  [C]alorie Intake")
            print("  [B]ack")

            the_choice = input("  Enter an action: ")
            if the_choice == "G" or the_choice == "g":
                print("\n+", "=" * 56, "+")
                print(f"{'Calorie Tracking':^60}")
                print("+", "=" * 56, "+")
                calorie.user_info()
            elif the_choice == "C" or the_choice == "c":
                print("\n+", "=" * 56, "+")
                print(f"{'Calorie Intake':^60}")
                print("+", "=" * 56, "+")
                calorie.calorie_intake()
            elif the_choice == "B" or the_choice == "b":
                return exec(open("main_menu.py").read())
            else:
                print("Invalid. Try again.")

if __name__ == "__main__":
    calorie = Calorie_Tracker()
    calorie.main()
