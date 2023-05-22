import calorie, trycalorie,  water, food_diary

#nutri_one = pass
#nutri_two = pass
#nutri_three = pass
nutri_four = trycalorie
nutri_five = water
nutri_six = food_diary


while True:
    print("\n+", "=" * 56, "+")
    print(f"{'NutriGuild':^60}")
    print("+", "=" * 56, "+")
    print("  [1] User Info")
    print("  [2] Recipe Suggestion and Nutritional Information")
    print("  [3] Meal Planning and Grocery List Creation")
    print("  [4] Calorie Tracking and Goal Setting")
    print("  [5] Water Intake Tracking")
    print("  [6] Food Diary and Progress Tracking")
    print("  [7] Exit")

    choice = input("  Enter your choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        nutri_four.main()
    elif choice == "5":
        nutri_five.main()
    elif choice == "6":
        nutri_six.main()
    elif choice == "7":
        print("\n+", "=" * 56, "+")
        print(f"{'THANK YOU! EATWELL.':^60}")
        print("+", "=" * 56, "+")
        break
    else:
        print("Invalid choice!")