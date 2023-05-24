import openai

def get_api_key():
    with open("api.txt", "r") as file:
        api_key = file.read().strip()
    return api_key

def mealplanning():
    openai.api_key = get_api_key()

    while True:
        print("\n")
        print("+", "=" * 56, "+")
        print(f"{'Meal Planning and Grocery List Creation':^60}")
        print("+", "=" * 56, "+")
        print("  Do you want a grocery list for your meal?")
        print("  [1] YES")
        print("  [2] NO (Exit)")

        user_choice = input("  Enter your choice: ")

        if user_choice == "1":
            print("\n")
            print("+", "=" * 56, "+")
            print(f"{'Grocery List Creation':^60}")
            print("+", "=" * 56, "+")
            messages = []
            print("  What is your meal?")
            while input != "quit()":
                message = input("  Your Meal: ")
                messages.append({"role": "user", "content": "In bullet form give me a grocery list for " + message})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print(reply)
                break
        elif user_choice == "2":
            break
        else:
            print("  Invalid input. Please try again.")

if __name__ == "__main__":
    mealplanning()
