import random
import os
import colorama
from colorama import Fore, Back, Style

specs = ['Brand', 'OS', 'Battery', 'Display', 'GPU', 'CPU', 'Storage', 'RAM', 'Colour', 'Camera', 'Screensize', 'Speed', 'Price']
master_dict = {}
master_dict = dict.fromkeys(specs)


master_dict['Brand'] = ['Apple', 'HP', 'Dell', 'Asus', 'Acer', 'Lenovo']
master_dict['OS'] = ['macOS', 'Windows', 'Linux']
master_dict['Battery'] = ['10000mAh', '7000mAh', '4000mAh', '2000mAh']
master_dict['Display'] = ['Touchscreen', 'QLED', 'OLED']
master_dict['GPU'] = ['M3 Max', 'M4 Max', 'RTX 5090', 'RTX 3080 Ti', 'RX 7900M', 'Radeon 8060S', 'Arc 140V']
master_dict['CPU'] = ['M4 Max 16 Core', 'M4 9 Core', 'i9 14900HX', 'i7 14650HX', 'Ryzen 7 250', 'Ryzen 3 8440U']
master_dict['Storage'] = ['256GB', '512GB', '1TB', '2TB']
master_dict['RAM'] = ['8GB', '16GB', '32GB']
master_dict['Colour'] = ['Blue', 'Gray', 'Black', 'Red']
master_dict['Camera'] = ['3840x2160', '1920x1080', '1280x720']
master_dict['Screensize'] = ['13\'','14.9\'','15.2\'','16\'']
master_dict['Speed'] = ['3.5GHz', '2.5GHz', '1.6GHz']
master_dict['Price'] = ['70000', '80000', '90000', '100000', '120000']

n_laptops = 500

laptop_list = []
#Apple = False
for _ in range(n_laptops):
    newlaptop = dict.fromkeys(specs)
    for kk in specs:
        newlaptop[kk] = random.choice(master_dict[kk])
    laptop_list.append(newlaptop)


selected = []


query = ""
for kk in specs:
    print('\n')
    for jj in range(len(master_dict[kk])):
        print(master_dict[kk][jj], end = ' '*(15 - len(master_dict[kk][jj])))
    question ='\nDo you have any preference for the ' + kk + '?(Enter for none)\n'
    Q = input(question)    
    if Q == '':
        pass

    else:
        query = query + 'laptop'+'[\'' + kk + '\'] ' + '==' + '\'' + Q + '\'' + ' and '
        print(kk)


query = query[0:-4:1]


if query == '':
    selected = laptop_list
else:
    for laptop in laptop_list:
        if eval(query):
            selected.append(laptop)


characters = 0
os.system('cls')
print("We have", len(selected), 'laptop(s) that have met your preference.(Enter to continue). Prefered Specicfications are hilighted')
for kk in range(len(selected)):
    for spec in specs:
        characters = len(spec)    
        if spec in query:
            print(Fore.RED + spec, end = ' '*(12-characters))
            a = selected[kk]
            print(a[spec])
        else:      
            print(Fore.RESET + spec, end = ' '*(12-characters))
            a = selected[kk]
            print(a[spec])
    print('')    
    input()    







