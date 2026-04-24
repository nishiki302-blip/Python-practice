#Assume that users will input fruits exactly as written in the poster 
#(e.g., strawberries, not strawberry)

fruits = {
        'apple' : 130,
        'avocado':  50,
        'banana' : 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew Melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80
    }

def main():
    item = input('Item: ').lower()
    if show_calories(item):
        print(show_calories(item))

def show_calories(food):
    for fruit in fruits:
        if food == fruit:
            return f'Calories: {fruits[fruit]}'
    return None

main()