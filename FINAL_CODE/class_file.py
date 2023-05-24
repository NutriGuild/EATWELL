import random as rdm

class Recipe:
    def __init__(self, name, ingredients, nutritional_facts):
        self.name = name
        self.ingredients = ingredients
        self.nutritional_facts = nutritional_facts

    def __str__(self):
        return f"  Recipe: {self.name}"


class stored_recipe:
    def __init__(self, recipes):
        self.recipes = []
        for recipe in recipes:
            self.recipes.append(Recipe(recipe['Recipe'], recipe['Ingredients'], recipe['Nutritional facts']))

    def random_recipe(self):
        return rdm.choice(self.recipes)

'''Stored recipe data (approx. 30 items)'''
recipes = [
    {
        "Recipe": "Grilled Chicken Salad",
        "Ingredients": [
            "4 oz. boneless, skinless chicken breast",
            "2 cups mixed greens",
            "1/2 cup cherry tomatoes",
            "1/4 cup sliced cucumber",
            "2 tbsp balsamic vinaigrette"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 20g",
            "Carbs: 10g",
            "Fat: 15g"
        }
    },
    {
        "Recipe": "Greek Yogurt Parfait",
        "Ingredients": [
            "1 cup non-fat Greek yogurt",
            "1/2 cup sliced strawberries",
            "1/2 cup blueberries",
            "2 tbsp honey",
            "1/4 cup granola"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 20g",
            "Carbs: 35g",
            "Fat: 5g"
        }
    },
    {
        "Recipe": "Roasted Salmon with Asparagus",
        "Ingredients": [
            "4 oz. salmon fillet",
            "1 cup asparagus",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25g",
            "Carbs: 5g",
            "Fat: 20g"
        }
    },
    {
        "Recipe": "Turkey Chili",
        "Ingredients": [
            "1 lb. ground turkey",
            "1 can black beans",
            "1 can diced tomatoes",
            "1 onion, chopped",
            "1 green pepper, chopped",
            "2 cloves garlic, minced",
            "1 tbsp chili powder"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25g",
            "Carbs: 25g",
            "Fat: 10g"
        }
    },
    {
        "Recipe": "Quinoa Salad with Vegetables",
        "Ingredients": [
            "1 cup cooked quinoa",
            "1/2 cup diced tomatoes",
            "1/2 cup diced cucumbers",
            "1/4 cup diced red onion",
            "1/4 cup feta cheese",
            "1 tbsp olive oil",
            "1 tbsp lemon juice"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 10g",
            "Carbs: 40g",
            "Fat: 10g"
        }
    },
    {
        "Recipe": "Grilled Tuna Steak",
        "Ingredients": [
            "4 oz. tuna steak",
            "1 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 200",
            "Protein: 25g",
            "Carbs: 0g",
            "Fat: 10g"
        }
    },
    {
        "Recipe": "Broiled Pork Chop",
        "Ingredients": [
            "4 oz. pork chop",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25g",
            "Carbs: 0g",
            "Fat: 20g"
        }
    },
    {
        "Recipe": "Vegetable Stir Fry",
        "Ingredients": [
            "1 cup mixed vegetables (broccoli, bell peppers, carrots, onions)",
            "1/2 cup brown rice",
            "1/4 cup low-sodium soy sauce",
            "1/4 cup vegetable broth"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 10",
            "Carbs: 55",
            "Fat: 5"
        }
    },
    {
        "Recipe": "Chicken Fajitas",
        "Ingredients": [
            "4 oz. chicken breast",
            "1 green pepper, sliced",
            "1 onion, sliced",
            "1 tbsp olive oil",
            "1 tbsp chili powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 25",
            "Carbs: 15",
            "Fat: 10"
        }
    },
    {
        "Recipe": "Grilled Vegetable Skewers",
        "Ingredients": [
            "1 zucchini, sliced",
            "1 yellow squash, sliced",
            "1 red pepper, sliced",
            "1/4 cup balsamic vinaigrette"
        ],
        "Nutritional facts": {
            "Calories: 150",
            "Protein: 5",
            "Carbs: 15",
            "Fat: 10"
        }
    },
    {
        "Recipe": "Black Bean Soup",
        "Ingredients": [
            "1 can black beans",
            "1 cup low-sodium vegetable broth",
            "1 onion, chopped",
            "2 cloves garlic, minced",
            "1 tsp cumin",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 200",
            "Protein: 10",
            "Carbs: 30",
            "Fat: 5"
        }
    },
    {
        "Recipe": "Baked Salmon with Sweet Potato",
        "Ingredients": [
            "4 oz. salmon fillet",
            "1 medium sweet potato, chopped",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 350",
            "Protein: 25",
            "Carbs: 35",
            "Fat: 15"
        }
    },
    {
        "Recipe": "Turkey Meatballs with Spaghetti Squash",
        "Ingredients": [
            "1 lb. ground turkey",
            "1/2 cup breadcrumbs",
            "1 egg",
            "1 spaghetti squash, cooked and shredded",
            "1/2 cup marinara sauce"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25g",
            "Carbs: 20g",
            "Fat: 15g"
        }
    },
    {
        "Recipe": "Grilled Chicken with Roasted Vegetables",
        "Ingredients": [
            "4 oz. chicken breast",
            "1 cup mixed vegetables (broccoli, carrots, onions)",
            "1/2 tbsp olive oil",
            "1/2 tsp garlic powder",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25g",
            "Carbs: 10g",
            "Fat: 15g"
        }
    },
    {
        "Recipe": "Avocado Toast with Egg",
        "Ingredients": [
            "1 slice whole wheat bread",
            "1/4 avocado, mashed",
            "1 egg, fried or scrambled",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 10g",
            "Carbs: 20g",
            "Fat: 15g"
        }
    },
    {
        "Recipe": "Spinach and Feta Stuffed Chicken Breast",
        "Ingredients": [
            "4 oz. chicken breast",
            "1 cup spinach, chopped",
            "1/4 cup crumbled feta cheese",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 25g",
            "Carbs: 5g",
            "Fat: 10g"
        }
    },
    {
        "Recipe": "Lentil Soup",
        "Ingredients": [
            "1 cup cooked lentils",
            "1 cup low-sodium vegetable broth",
            "1 carrot, chopped",
            "1 celery stalk, chopped",
            "1 onion, chopped",
            "1 tsp cumin",
            "Salt and pepper to taste"
        ],
        "Nutritional facts": {
            "Calories: 200",
            "Protein: 10g",
            "Carbs: 30g",
            "Fat: 5g"
        }
    },
    {
        "Recipe": "Shrimp and Vegetable Stir Fry",
        "Ingredients": [
            "4 oz. shrimp",
            "1 cup mixed vegetables (broccoli, bell peppers, onions)",
            "1/2 cup brown rice",
            "1/4 cup low-sodium soy sauce",
            "1/4 cup vegetable broth"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 20g",
            "Carbs: 40g",
            "Fat: 5g"
        }
    },
    {
        "Recipe": "Beef and Broccoli",
        "Ingredients": [
            "4 oz. flank steak, sliced",
            "1 cup broccoli florets",
            "1 tbsp low-sodium soy sauce",
            "1 tbsp cornstarch",
            "1 tsp sesame oil"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25",
            "Carbs: 10",
            "Fat: 15"
        }
    },
    {
        "Recipe": "Greek Chicken Wrap",
        "Ingredients": [
            "4 oz. grilled chicken breast",
            "1 whole wheat wrap",
            "1/4 cup hummus",
            "1/4 cup diced tomatoes",
            "1/4 cup diced cucumbers",
            "1/4 cup crumbled feta cheese",
            "1/4 cup diced red onion"
        ],
        "Nutritional facts": {
            "Calories: 400",
            "Protein: 30",
            "Carbs: 30",
            "Fat: 20"
        }
    },
    {
        "Recipe": "Tuna Salad",
        "Ingredients": [
            "1 can tuna, drained",
            "2 tbsp Greek yogurt",
            "1/4 cup diced celery",
            "1/4 cup diced red onion",
            "1 tbsp lemon juice"
        ],
        "Nutritional facts": {
            "Calories: 220",
            "Protein: 30",
            "Carbs: 4",
            "Fat: 8"
        }
    },
    {
        "Recipe": "Salmon with Asparagus",
        "Ingredients": [
            "1 salmon fillet",
            "1/2 lb asparagus, trimmed",
            "1 tbsp olive oil",
            "1 tbsp lemon juice"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 25",
            "Carbs: 8",
            "Fat: 20"
        }
    },
    {
        "Recipe": "Sweet Potato and Black Bean Quesadillas",
        "Ingredients": [
            "2 small sweet potatoes, peeled and cubed",
            "1 can black beans, drained and rinsed",
            "4 whole wheat tortillas",
            "1/2 cup shredded cheddar cheese"
        ],
        "Nutritional facts": {
            "Calories: 400",
            "Protein: 16",
            "Carbs: 60",
            "Fat: 10"
        }
    },
    {
        "Recipe": "Tofu and Vegetable Curry",
        "Ingredients": [
            "1 block firm tofu, cubed",
            "2 cups mixed vegetables (such as cauliflower, carrots, and bell peppers)",
            "1 can coconut milk",
            "2 tbsp curry powder"
        ],
        "Nutritional facts": {
            "Calories: 350",
            "Protein: 20",
            "Carbs: 20",
            "Fat: 20"
        }
    },
    {
        "Recipe": "Grilled Chicken Skewers",
        "Ingredients": [
            "1 lb boneless, skinless chicken breast, cut into cubes",
            "1 red bell pepper, cut into cubes",
            "1 green bell pepper, cut into cubes",
            "1 red onion, cut into cubes",
            "2 tbsp olive oil"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 35",
            "Carbs: 8",
            "Fat: 14"
        }
    },
    {
        "Recipe": "Caprese Salad",
        "Ingredients": [
            "1 large tomato, sliced",
            "4 oz fresh mozzarella, sliced",
            "1/4 cup fresh basil leaves",
            "2 tbsp balsamic vinegar"
        ],
        "Nutritional facts": {
            "Calories: 250",
            "Protein: 14",
            "Carbs: 10",
            "Fat: 18"
        }
    },
    {
        "Recipe": "Mediterranean Bowl",
        "Ingredients": [
            "1/2 cup cooked quinoa",
            "1/2 cup chickpeas, drained and rinsed",
            "1/4 cup sliced cucumber",
            "1/4 cup cherry tomatoes, halved",
            "1/4 cup crumbled feta cheese"
        ],
        "Nutritional facts": {
            "Calories: 300",
            "Protein: 14",
            "Carbs: 40",
            "Fat: 10"
        }
    },
    {
        "Recipe": "Turkey and Veggie Chili",
        "Ingredients": [
            "1 lb ground turkey",
            "1 can kidney beans, drained and rinsed",
            "1 can diced tomatoes",
            "2 cups mixed vegetables (such as zucchini, bell peppers, and onion)"
        ],
        "Nutritional facts": {
            "Calories: 350",
            "Protein: 30",
            "Carbs: 25",
            "Fat: 14"
        }
    },
    {
        "Recipe": "Sautéed Zucchini and Squash",
        "Ingredients": [
            "2 small zucchini, sliced",
            "2 small yellow squash, sliced",
            "2 cloves garlic, minced",
            "1 tbsp olive oil"
        ],
        "Nutritional facts": {
            "Calories: 100",
            "Protein: 2",
            "Carbs: 8",
            "Fat: 7"
        }
    },
    {
        "Recipe": "Cauliflower Fried Rice",
        "Ingredients": [
            "1 small head cauliflower, grated",
            "1/2 cup mixed vegetables (such as peas, carrots, and onions)",
            "1 egg, beaten",
            "1 tbsp soy sauce"
        ],
        "Nutritional facts": {
            "Calories: 150",
            "Protein: 8",
            "Carbs: 20",
            "Fat: 5"
        }
    }
]

def border():
    print("+", "=" * 56, "+")
    print(f"{'Recipe Suggestion and Nutritional Information':^60}")
    print("+", "=" * 56, "+")

def suggested_recipe():
    recipe_list = stored_recipe(recipes)
    random_recipe = recipe_list.random_recipe()
    border()
    print(random_recipe)

    print("  Ingredients:")
    for ingredient in random_recipe.ingredients:
        print("  - " + ingredient)

    print("\n  Nutritional facts:")
    for fact in random_recipe.nutritional_facts:
        print("  - " + fact)
