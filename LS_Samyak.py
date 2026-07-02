import random

print("Welcome to the BGT cricket store.")
item_type = input(
    "What type of item would you like to browse? (Bats/Balls)\n").lower()
currency = input(
    "What currency would you like to use? (SGD/INR/AUD)\n").lower()

# Bat

if item_type == 'bats':
    specs = ['Brand', 'Weight', 'Size', 'Grain', 'Price']
    multiplier = 1
    sign = ''
    if currency == 'inr':
        multiplier = 62.62
        sign = "₹"
    elif currency == 'aud':
        multiplier = 1.14
        sign = "$"
    elif currency == 'sgd':
        multiplier = 1
        sign = "$"
    else:
        print("Invalid currency, will proceed with SGD")
        multiplier = 1
        sign = "$"

    print()

    master_dict = {}
    master_dict['Brands'] = ['Kookaburra', 'SS', 'Gray Nicolls', 'MRF', 'CEAT']
    master_dict['Weights'] = [
        str(random.randint(900, 1500)) + "g" for _ in range(10)
    ]
    master_dict['Sizes'] = [
        'Short Handle', 'Harrow', 'Size 6', 'Size 5', 'Size 4'
    ]
    master_dict['Grains'] = [str(random.randint(4, 10)) for _ in range(10)]

    items_list = []
    n_items = 500
    for _ in range(n_items):
        grain = random.choice(master_dict['Grains'])
        grain_value = int(grain)
        weight = random.randint(900, 1500)
        price = 0
        if grain_value >= 8:
            price += 40
        elif grain_value >= 6:
            price += 20
        else:
            price += 10
        price = round(multiplier * (random.randint(140, 210) + price), 2)
        new_item = {
            'Brand': random.choice(master_dict['Brands']),
            'Weight': f"{weight}g",
            'Size': random.choice(master_dict['Sizes']),
            'Grain': grain,
            'Price': f"{sign}{price}",
            'Price_number': price,
            'Weight_number': weight
        }
        items_list.append(new_item)

    list = []
    user_choice = dict.fromkeys(specs)
    for kk in specs:
        user_choice[kk] = input(
            f"Any Preference for {kk} (Press Enter for no preference):\n")
        if "," in user_choice[kk]:
            list = user_choice[kk].split(",")

    query = ''
    for kk in user_choice:
        if user_choice[kk] == '':
            continue
        elif ", " in user_choice[kk]:
            list = user_choice[kk].split(",")
            query += f"(item['{kk}'] == '{list[0]}' or item['{kk}'] == '{list[1].strip()}') and "
        elif kk == 'Price' and "-" in user_choice[kk]:
            list = user_choice[kk].split("-")
            min_p = int(list[0])
            max_p = int(list[1])
            query += f"(item['Price_number'] >= {min_p} and item['Price_number'] <= {max_p}) and "
        elif kk == 'Weight' and "-" in user_choice[kk]:
            list = user_choice[kk].split("-")
            min_w = int(list[0])
            max_w = int(list[1])
            query += f"(item['Weight_number'] >= {min_w} and item['Weight_number'] <= {max_w}) and "

        else:
            query += f"item['{kk}'] == '{user_choice[kk]}' and "
    query = query[:-4]

    selected_items = []
    if query == "":
        selected_items = [item for item in items_list]
    else:
        selected_items = [item for item in items_list if eval(query)]

    if len(selected_items) == 0:
        print("No items match your preferences.")
    else:
        print(f"{len(selected_items)} items met your needs:\n")
        header = "| Brand            | Weight  | Size            | Grain  | Price      |"
        separator = "-" * (len(header) + 2)
        print(header)
        print(separator)
        for item in selected_items:
            row = f"| {item['Brand']:<16} | {item['Weight']:<7} | {item['Size']:<15} | {item['Grain']:<6} | {item['Price']:<10} |"
            print(row)
            print()
        print(separator)

#Ball

if item_type == 'balls':
    specs = ['Brand', 'Weight', 'Color', 'Type', 'Price']
    multiplier = 1
    sign = ''
    if currency == 'inr':
        multiplier = 62.62
        sign = "₹"
    elif currency == 'aud':
        multiplier = 1.14
        sign = "$"
    elif currency == 'sgd':
        multiplier = 1
        sign = "$"
    else:
        print("Invalid currency, will proceed with SGD")
        multiplier = 1
        sign = "$"

    print()

    master_dict = {}
    master_dict['Brands'] = ['Kookaburra', 'SS', 'Gray Nicolls', 'MRF', 'CEAT']
    master_dict['Colors'] = ['Red', 'White', 'Pink']
    master_dict['Types'] = ['Leather', 'Rubber', 'Plastic', 'Tennis Ball']

    items_list = []
    n_items = 300
    for _ in range(n_items):
        weight = random.randint(130, 163)
        type = random.choice(master_dict['Types'])

        if type == 'Leather':
            weight += random.randint(5, 10)
        elif type == 'Rubber':
            weight += random.randint(2, 5)
        elif type == 'Plastic':
            weight += 0
        elif type == 'Tennis Ball':
            weight -= random.randint(20, 30)

        price = 0
        if weight >= 156:
            price += 6
        elif weight >= 150:
            price += 4
        elif weight >= 140:
            price += 2
        elif weight >= 125:
            price += 0
        else:
            price -= 10
        price = round(multiplier * (random.randint(12, 15) + price), 2)

        new_item = {
            'Brand': random.choice(master_dict['Brands']),
            'Weight': f"{weight}g",
            'Color': random.choice(master_dict['Colors']),
            'Type': type,
            'Price': f"{sign}{price}",
            'Price_number': price,
            'Weight_number': weight
        }
        items_list.append(new_item)

    list = []
    user_choice = dict.fromkeys(specs)
    for kk in specs:
        user_choice[kk] = input(
            f"Any Preference for {kk} (Press Enter for no preference):\n")
        if "," in user_choice[kk]:
            list = user_choice[kk].split(",")

    query = ''
    for kk in user_choice:
        if user_choice[kk] == '':
            continue
        elif ", " in user_choice[kk]:
            list = user_choice[kk].split(",")
            query += f"(item['{kk}'] == '{list[0]}' or item['{kk}'] == '{list[1].strip()}') and "
        elif kk == 'Price' and "-" in user_choice[kk]:
            list = user_choice[kk].split("-")
            min_p = int(list[0])
            max_p = int(list[1])
            query += f"(item['Price_number'] >= {min_p} and item['Price_number'] <= {max_p}) and "
        elif kk == 'Weight' and "-" in user_choice[kk]:
            list = user_choice[kk].split("-")
            min_w = int(list[0])
            max_w = int(list[1])
            query += f"(item['Weight_number'] >= {min_w} and item['Weight_number'] <= {max_w}) and "

        else:
            query += f"item['{kk}'] == '{user_choice[kk]}' and "
    query = query[:-4]

    selected_items = []
    if query == "":
        selected_items = [item for item in items_list]
    else:
        selected_items = [item for item in items_list if eval(query)]

    if len(selected_items) == 0:
        print("No items match your preferences.")
    else:
        print(f"{len(selected_items)} items met your needs:\n")
        header = "| Brand            | Weight  | Color      | Type            | Price      |"
        separator = "-" * (len(header) + 2)
        print(header)
        print(separator)
        for item in selected_items:
            row = f"| {item['Brand']:<16} | {item['Weight']:<7} | {item['Color']:<9} | {item['Type']:<16} | {item['Price']:<10} |"
            print(row)
            print()
        print(separator)
else:
    print("Please reselect a valid type of item to browse.")
