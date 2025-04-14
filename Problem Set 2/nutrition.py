rawfruits={"Apple":130,
            "Avacado":50, 
            "Banana":110,
            "Cantaloupe":50,
            "Grapefruit":60,
            "Grapes":90,
            "Honeydew Melon":50,
            "Kiwifruit":90,
            "Lemon":15,
            "Lime":20,
            "Peach":60,
            "Pear":100,
            "Pineapple":50,
            "Plums":70,
            "Strawberries":50,
            "Sweet Cherries":100,
            "Tangerine":50,
            "Watermelon":80}
input=input("Item: ")
for fruit in rawfruits:
    if input==fruit:
        print("Calories: ", rawfruits[fruit])
