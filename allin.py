import fdpt
import calorie
import progress

diary = fdpt.Food_Diary()
tracker = calorie.Calorie_Tracker()
view = progress.Progress()

def Main_Menu():
    while True:
        print("\nMain Menu")
        print("1. Suggestions") #recipe and meal and grocery list
        print("2. Record") #record food and food diary
        print("3. Calorie and Water Intake") # calorie and water intake
        print("4. View Progress") #progress
        print("5. Setting") #user info, program info
        print("6. Exit")
        main_choice = input("Enter action: ")

        if main_choice == "1":
            print("\n------------------ Suggestion -------------------")
            pass
        elif main_choice == "2":
            print("\n-------------------- Record ---------------------")
            fdpt.main()
        elif main_choice == "3":
            print("\n----------- Calorie and Water Intake ------------")
            calorie.main()
        elif main_choice == "4":
            print("\n----------------- View Progress -----------------")
            view.view_progress()
        elif main_choice == "5":
            print("\n-------------------- Setting --------------------")

        elif main_choice == "6":
            print("\nExiting the program.")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    Main_Menu()