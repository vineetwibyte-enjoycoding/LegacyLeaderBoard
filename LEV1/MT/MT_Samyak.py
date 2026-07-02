

#Choose which tool u want to use

print('This is the new all-in-one useful app.')
print('There are 4 different things it can do: Check the strength of your password, convert currency, calculate, and find the word count of a particular text.')
print('Pick 1, 2, 3 or 4\n')
print('1. Password strength checker 2.Currency converter')
print('3. Calculator                4. Word count')
print()
tool = input()

#password checker(try to ask password againafter suggestions)
if int(tool) == 1:
  
  print('I will make sure that you never get hacked!!')
  print(
  'Just tell me your password and I will tell you how strong it is and give you some ideas to strengthen it.\n'
)

  response = input('Give me a password. \n')
  strength = 0

  #length of password
  if len(response) > 9:
    strength = strength + 1

  number = 0
  caps = 0
  specs = 0

  #finding number, caps, and special characters
  for x in response:
    if x.isnumeric():
      number += 1
      strength = strength + 1

    if x != x.lower():
      caps += 1
      strength = strength + 1

    if x.isalnum():
      specs += 1

  char = len(response) - specs
  if char > 0:
    strength = strength + 1

  print('Your password has',             len(response), 'character(s), ', caps,
      'capital letter(s), ', number, 'number(s), ', char,
      'special character(s).', '\n')

  print('Your password strength is', strength * 9, '%', '\n')

  #suggestions
  if strength == 0:
    print('Completely change your password')
    print('You are very vulnerable to hackers')

  elif strength == 1:
    print('You need work to become a less vulnerable target for hackers')

  elif 2 <= strength <= 4:
    print('Well done! Just a few changes and you should be safe')

  else:
    print('Excellent! You will definitely be safe. However, make sure to use different passwords for different accounts.''\n')

  if len(response) < 9:
    print()
    print('Your Password is too short!')
    print('Try adding more characters.\n')

  if caps < 2:
    print('Add capital letters')

  if number < 2:
    print('Add some numbers')

  if char < 1:
    print('Add special characters')


#Currency converter

if int(tool) == 2:
    # Define the exchange rates
    exchange_rates = {
        'usd': 1.34,       # 1 USD = 1.34 SGD
        'sgd': 0.74,       # 1 SGD = 0.74 USD
        'rupees': 0.0162,  # 1 Rupee = 0.0162 SGD
    }

    # Ask for the amount and base currency
    amount = float(input("Enter the amount: "))
    base_currency = input("Enter the base currency (Rupees, SGD, or USD): ").lower()

    # Ask for the target currency
    target_currency = input("Enter the target currency (Rupees, SGD, or USD): ").lower()

    # Check if both currencies are valid
    if base_currency not in exchange_rates:
        print(f"Invalid base currency: {base_currency.capitalize()}")
    elif target_currency not in exchange_rates:
        print(f"Invalid target currency: {target_currency.capitalize()}")
    else:
        # Perform the currency conversion
        if base_currency == 'rupees':
            converted_amount = amount * exchange_rates[target_currency]
            print(f"{amount} Rupees = {converted_amount} {target_currency.capitalize()}")
        elif target_currency == 'rupees':
            converted_amount = amount / exchange_rates[base_currency]
            print(f"{amount} {base_currency.capitalize()} = {converted_amount} Rupees")
        else:
            converted_amount = amount * exchange_rates[base_currency] / exchange_rates[target_currency]
            print(f"{amount} {base_currency.capitalize()} = {converted_amount} {target_currency.capitalize()}")



#Calculator

if int(tool) == 3:
  print('pick an operator.') 

  #Which operator
  print('You have 4 choices')
  print('1. Addition', '    ',    '3. Multiplication' )
  print('2. Subtraction', ' ', '4. Division')
  print()
  choice = int(input('pick 1-4 (click enter when done)\n'))
  #numbers
  num_1 = int(input('Enter the first number\n'))
  num_2 = int(input('Enter the second number\n'))

  #addition
  if choice == 1:
    print()
    print('Your answer is', num_1 + num_2)

  #subtraction
  elif choice == 2:
    print()
    print('Your answer is', num_1 - num_2)
  #multiplication
  elif choice == 3:
    print()
    print('Your answer is', num_1 * num_2)
  #division
  elif choice == 4:
    if num_2 == 0:
      answer = 'Infinity'
    else:
      print()
      answer = num_1 / num_2
    print('Your answer is', answer)

# Word and character count
if int(tool) == 4:
  
  print()
  answer = input('Enter a text: ')
  
  word_count = len(answer.split())
  print("Word count:", word_count)
  
  character_count = len(answer)
  print("Number of characters:", character_count)

  
  
