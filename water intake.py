import sys

class Beverage:
    def __init__(self, beverage_name, container, water_content):
        self.beverage_name = beverage_name
        self.container = container
        self.water_content = water_content

    def get_water_content(self):
        return self.water_content

    def info(self):
        return f"\nA {self.container} of {self.beverage_name} has approximately {self.water_content} mL of water"


class Prohibited_drinks(Beverage):
    def new_info(self):
        return f"\n{self.beverage_name} is considered unhealthy for you. However, a {self.container}\n" \
               f"of {self.beverage_name} has approximately {self.water_content} mL of water.\n" \
               f"We recommend taking this moderately and responsibly."

Water = Beverage("Water", "glass", 237)
Coffee = Beverage("Coffee", "cup", 125)
Tea = Beverage("Tea", "cup", 120)
Milk = Beverage("Milk", "glass", 206)
Juice = Beverage("Juice", "glass", 209)
Softdrinks = Prohibited_drinks("Softdrinks", "bottle", 200)
Alcoholic_drinks = Prohibited_drinks("Alcoholic drinks", "bottle", 188)

def submenu(drinks_name, container_type, amount, short_text, water_intake):
    while True:
        print("=*" * 50)
        print(f"{short_text}")
        print(f"\nHow many {container_type} of {drinks_name} did you take?")
        print(f"[1] 1 {container_type}")
        print(f"[2] 2 {container_type}")
        print(f"[3] 3 {container_type}")
        print("\n[4] Back to beverage tab")

        try:
            quantity = int(input("\nEnter quantity: "))

            if quantity in [1, 2, 3]:
                water_intake_formula = amount * quantity
                limit = 1896
                water_intake += water_intake_formula
                if water_intake < limit:
                    print(f"Your current water intake is: {water_intake} mL")
                    continue
                if water_intake >= limit:
                    print("\nGood job! You have reached your daily water intake.")
                    print(f"Overall, you have took a total of {water_intake} mL of water.")
                    print("See you tomorrow!")
                    sys.exit()
            elif quantity == 4:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    return water_intake

water_intake = 0

while True:
    print("=*" * 50)
    print("\nWATER INTAKE\n")
    print("Choose a beverage that you took:\n")
    print(f"Water Intake Level: {water_intake} / 1896 mL\n")
    print("[1] Water")
    print("[2] Coffee")
    print("[3] Tea")
    print("[4] Milk")
    print("[5] Juice")
    print("[6] Softdrinks")
    print("[7] Alcoholic drinks")
    print("[8] Back to the Main Menu\n")

    try:
        beverage_choice = int(input("Your choice: "))

        if beverage_choice == 1:
            water_intake = submenu(Water.beverage_name, Water.container, Water.water_content, Water.info(),
                                   water_intake)
        elif beverage_choice == 2:
            water_intake = submenu(Coffee.beverage_name, Coffee.container, Coffee.water_content, Coffee.info(),
                                   water_intake)
        elif beverage_choice == 3:
            water_intake = submenu(Tea.beverage_name, Tea.container, Tea.water_content, Tea.info(), water_intake)
        elif beverage_choice == 4:
            water_intake = submenu(Milk.beverage_name, Milk.container, Milk.water_content, Milk.info(), water_intake)
        elif beverage_choice == 5:
            water_intake = submenu(Juice.beverage_name, Juice.container, Juice.water_content, Juice.info(),
                                   water_intake)
        elif beverage_choice == 6:
            water_intake = submenu(Softdrinks.beverage_name, Softdrinks.container, Softdrinks.water_content,
                                   Softdrinks.new_info(), water_intake)
        elif beverage_choice == 7:
            water_intake = submenu(Alcoholic_drinks.beverage_name, Alcoholic_drinks.container,
                                   Alcoholic_drinks.water_content,
                                   Alcoholic_drinks.new_info(), water_intake)
        elif beverage_choice == 8:
            break
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nTotal water intake: {water_intake} / 1896 mL")