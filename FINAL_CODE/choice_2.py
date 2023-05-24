from class_file import suggested_recipe

'''Main system - [2] Recipe Suggestion and Nutritional Information '''
def recipe_suggestion():
    while True:
        print("\n")
        print("+", "=" * 56, "+")
        print(f"{'Recipe Suggestion and Nutritional Information':^60}")
        print("+", "=" * 56, "+")
        print("  Do you want to have a recipe suggestion?")
        print("  [1] YES")
        print("  [2] NO (Exit)")


        user_choice = int(input("  Enter choice: "))
        if user_choice == 1:
            print("\n")
            suggested_recipe()

        elif user_choice == 2:
            break

        else:
            print("Invalid input. Please try again.")