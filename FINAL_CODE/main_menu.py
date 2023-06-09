import time
import choice_1, choice_2, choice_3, choice_4, choice_5, choice_6

nutri_one = choice_1
nutri_two = choice_2
nutri_three = choice_3
nutri_four = choice_4
nutri_five = choice_5
nutri_six = choice_6


while True:
    print("\n")
    print("+", "=" * 56, "+")
    print(f"{'Embrace A Tasty, Well-balanced Eating Lifestyle':^60}")
    print(f"{'(EATWELL)':^60}")
    print(f"{'A Nutritional Guide Software':^60}")
    print("+", "=" * 56, "+")
    print("  [1] User Info")
    print("  [2] Recipe Suggestion and Nutritional Information")
    print("  [3] Meal Planning and Grocery List Creation")
    print("  [4] Calorie Tracking and Goal Setting")
    print("  [5] Water Intake Tracking")
    print("  [6] Food Diary")
    print("  [7] Log Out")

    choice = input("  Enter your choice: ")

    if choice == "1":
        nutri_one.users_info()
    elif choice == "2":
        nutri_two.recipe_suggestion()
    elif choice == "3":
        nutri_three.mealplanning()
    elif choice == "4":
        nutri_four.main()
    elif choice == "5":
        nutri_five.main()
    elif choice == "6":
        nutri_six_instance = nutri_six.Food_Diary()
        nutri_six_instance.diary()
    elif choice == "7":
        print("\n  Logging out.......\n\n")
        time.sleep(1)
        break
    else:
        print("  Invalid choice. Please try again.")