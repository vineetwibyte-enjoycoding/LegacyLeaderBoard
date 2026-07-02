import random

car = {'brand':'Ferrari', 'Model': 'Daytona', 'Engine': 'V8'}

print('\033[0;34m Welcome to Car dealership.')
print('\033[0;34m We have a huge variety of supercars.')
print('\033[0;34m Please indicate your preference.')
print()

def append_s(name):
    return name + 's'

print()

cars_list = []

specs = ['Brand', 'Model', 'Engine', 'TopSpeed', 'GearSystem', 'Horsepower', 'FuelType', 'Price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)

master_dict['Brand'] = ['Ferrari','Lamborghini','McLaren','Porsche','Bugatti','Koenigsegg','Pagani','Lotus']
master_dict['Model'] = ['812 Superfast', 'F8 Tributo', 'Roma', 'SF90 Stradale', '488 GTB', 'GTC4 Lusso', 'Portofino M', 'FXX-K', 'LaFerrari', 'Enzo', 'Huracan', 'Aventador', 'Urus', 'Huracan STO', 'Sián', 'Countach', 'Diablo', 'Murcielago', 'Gallardo', 'Aventador SVJ', '720S', 'GT', 'Artura', 'Senna', 'Speedtail', 'P1', '650S', '570S', 'MP4-12C', 'F1', '911', '718 Cayman', 'Taycan', 'Panamera', 'Macan', 'Carrera GT', '918 Spyder', 'Mission E', 'Cayenne', 'Boxster', 'Chiron', 'Veyron', 'Divo', 'Centodieci', 'Bolide', 'EB 110', 'EB Veyron', 'EB 218', 'Royale', 'La Voiture Noire', 'Agera', 'Regera', 'Jesko', 'Gemera', 'One:1', 'Agera RS', 'Regera Koenigsegg Christian von Koenigsegg', 'CCR', 'CCX', 'CGT', 'Huayra', 'Zonda', 'Huayra BC', 'Zonda Cinque', 'Huayra Roadster', 'Zonda Tricolore', 'Huayra R', 'Zonda F', 'Huayra Imola', 'Zonda HP Barchetta', 'Evija', 'Evora', 'Exige', 'Elise', 'Esprit', 'Europa', '2-Eleven', '3-Eleven', '4-Eleven', 'Exige Sport 350']
master_dict['Engine'] = ['V8','V10','V12','V16 5.6l','V8 5.6','V12 5.6','V10 5.6']
master_dict['TopSpeed'] = ['200Kmph','220Kmph','240Kmph','260Kmph','280Kmph','300Kmph','320Kmph']
master_dict['GearSystem'] = ['Manual', 'Automatic', 'Fusion']
master_dict['Horsepower'] = ['300 HP', '400 HP', '500 HP', '1000 HP']
master_dict['FuelType'] = ['Petrol', 'Diesel', 'EV', 'Hybrid']
master_dict['Price'] = ['INR 20000', 'INR 30000', 'INR 40000']

brand_model_map = {
    'Ferrari': ['812 Superfast', 'F8 Tributo', 'Roma', 'SF90 Stradale', '488 GTB', 'GTC4 Lusso', 'Portofino M', 'FXX-K', 'LaFerrari', 'Enzo'],
    'Lamborghini': ['Huracan', 'Aventador', 'Urus', 'Huracan STO', 'Sián', 'Countach', 'Diablo', 'Murcielago', 'Gallardo', 'Aventador SVJ'],
    'McLaren': ['720S', 'GT', 'Artura', 'Senna', 'Speedtail', 'P1', '650S', '570S', 'MP4-12C', 'F1'],
    'Porsche': ['911', '718 Cayman', 'Taycan', 'Panamera', 'Macan', 'Carrera GT', '918 Spyder', 'Mission E', 'Cayenne', 'Boxster'],
    'Bugatti': ['Chiron', 'Veyron', 'Divo', 'Centodieci', 'Bolide', 'EB 110', 'EB Veyron', 'EB 218', 'Royale', 'La Voiture Noire'],
    'Koenigsegg': ['Agera', 'Regera', 'Jesko', 'Gemera', 'One:1', 'Agera RS', 'CCR', 'CCX', 'CGT'],
    'Pagani': ['Huayra', 'Zonda', 'Huayra BC', 'Zonda Cinque', 'Huayra Roadster', 'Zonda Tricolore', 'Huayra R', 'Zonda F', 'Huayra Imola', 'Zonda HP Barchetta'],
    'Lotus': ['Evija', 'Evora', 'Exige', 'Elise', 'Esprit', 'Europa', '2-Eleven', '3-Eleven', '4-Eleven', 'Exige Sport 350']
}

# Generate car list
cars_list = []
used_cars = set()

for _ in range(60):
    valid = False
    while not valid:
        new_car = {}
        new_car['Brand'] = random.choice(master_dict['Brand'])
        new_car['Model'] = random.choice(master_dict['Model'])
        
        # Validate brand and model pairing
        if new_car['Model'] in brand_model_map[new_car['Brand']]:
            valid = True

    # Add other specifications
    for spec in specs[2:]:  # Skip 'Brand' and 'Model'
        new_car[spec] = random.choice(master_dict[(spec)])
    
    # Ensure uniqueness
    car_tuple = tuple(new_car.items())
    if car_tuple not in used_cars:
        used_cars.add(car_tuple)
        cars_list.append(new_car)

user_choice = dict.fromkeys(specs)
for kk in specs:
    user_choice[kk] = input('\033[0;32m Any preference for ' + kk + ' (Enter none for no preference)'+'\n')

query = ''

for kk in user_choice:
    if user_choice[kk].lower() == 'none':
        pass
    else:
        query = query + 'car[' + '\'' + kk + '\'] == ' + '\'' + user_choice[kk] + '\' and '

print(query)

input()

query = query[0:-4:1]

if query != '':
    selected = [car for car in cars_list if eval(query)]
else:
    selected = [car for car in cars_list]

print(len(selected), '\033[0;36m cars met your preference.')

characters = 0
for kk in specs:
    print(kk, end = '')
    characters = len(kk)
    print((12 - characters)*' ', end = '')
print()

characters = 0

for car in selected:
    for kk in car:
        print(car[kk], end = '')
        characters = len(car[kk])
        print((12 - characters)*' ', end = '')
    print()