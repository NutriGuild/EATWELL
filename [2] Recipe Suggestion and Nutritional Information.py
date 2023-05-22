from class_file import suggested_recipe

'''Main system - [2] Recipe Suggestion and Nutritional Information '''
while True:
    print("\nRECIPE SUGGESTION WITH NUTRITIONAL INFORMATION")
    print("\nDo you want to have a recipe suggestion?")
    print("1 - YES")
    print("2 - NO (Exit)\n")

    user_choice = int(input("Enter choice: "))
    if user_choice == 1:
        suggested_recipe()

    elif user_choice == 2:
        break

    else:
        print("Invalid input. Please try again.")
