import time 
import datetime as dt
from datetime import date
from lunarcalendar import Converter, Solar
def get_accurate_lunar_profile(birth_date):

  solar = Solar(birth_date.year, birth_date.month, birth_date.day)
  lunar = Converter.Solar2Lunar(solar)

  lunar_year = lunar.year

  animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", 
             "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
  elements = ["Metal", "Water", "Wood", "Fire", "Earth"]

  animal = animals[lunar_year % 12]
  element = elements[(lunar_year % 10) // 2]

  return element, animal

def typer(text, color=Fore.WHITE):
   for char in text:
      print(color + char, end='', flush=True)
      time.sleep(0.05)

def typei(text, color=Fore.WHITE):
   typer(text, color)
   user_input = input(Style.RESET_ALL)
   return user_input

typer("Welcome to the Birthday Countdown / Lunar New Year Horoscope predictor!\n", Fore.CYAN)
month=0
while True:
  while True:
    try:
      year = int(typei("What year were you born in?\n", Fore.YELLOW))
      break
    except ValueError:
      typer("Invalid input. Please enter a valid year.\n", Fore.RED)
      continue 
  while True:
    try:
      month = int(typei("What month were you born in? (January = 1, February = 2 ...)\n", Fore.YELLOW))
      break
    except ValueError:
      typer("Invalid input. Please enter a valid month.\n", Fore.RED)
      continue
  while True:
    try:
      day = int(typei("What day were you born in?\n", Fore.YELLOW))
      break
    except ValueError:
      typer("Invalid input. Please enter a valid day.\n", Fore.RED)
      continue
  try:
    datebirth = dt.datetime(year, month, day)
    break
  except ValueError:
    typer(f"Invalid date: {year}-{month}-{day}. Please enter a valid date.\n")
    continue
weekdaynames= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdaynum=datebirth.weekday()
weekday=weekdaynames[weekdaynum]
typer(f"You may not know, but you were born on a {weekday}.\n", Fore.GREEN)
ct = dt.datetime.now()
thisyear= ct.year 
thisyearbd=dt.datetime(thisyear, month, day)
if thisyearbd > ct:
  nextyearbd=thisyearbd
else:
  nextyearbd=dt.datetime(thisyear+1, month, day)
typer(f"Your next birthday is on {nextyearbd}\n", Fore.MAGENTA)
weekdaynum=nextyearbd.weekday()
weekday=weekdaynames[weekdaynum]
typer(f"Your next birthday will be on a {weekday}.\n", Fore.MAGENTA)
typer("But your birthday isn't all the calculator can do. Let's calculate your horoscope for the Lunar New Year!\n\n", Fore.CYAN)
typer("To settle the calendar, the Jade Emperor staged a high-stakes race across a river, promising a zodiac year to the first 12 animals to finish. The Rat famously took first place by hitching a ride on the Ox and jumping ahead at the last second, while the powerful Tiger and agile Rabbit followed behind. The Dragon arrived fifth after pausing to help villagers, and the rest of the animals—the Snake, Horse, Goat, Monkey, Rooster, and Dog—tricled in before the Pig finally claimed the twelfth spot after stopping for a snack. The poor Cat was left out entirely after being pushed into the river by the Rat, cementing an eternal rivalry and completing the Chinese Zodiac lineup we celebrate today at Lunar New Year.\n\n", Fore.YELLOW)
typer("In addition, The Wu Xing, or Five Elements, is a story of cosmic balance where Wood, Fire, Earth, Metal, and Water act as the dynamic life force behind the universe. These elements interact in two continuous cycles: a Generating Cycle where each element 'mothers' the next (like Wood feeding Fire), and an Overcoming Cycle that maintains order by having one element 'check' another (like Water putting out Fire). In the Chinese Zodiac, these elements layer onto the 12 animals in a 60-year rotation, meaning a person isn't just a 'Dragon' but specifically a 'Wood Dragon' or a 'Metal Dragon,' blending the animal's traits with the element’s specific virtues of creativity, passion, or wisdom.\n\n", Fore.GREEN)
typer("Lunar New Year is celebrated in China and other East Asian countries, and is the most important holiday of the year for many.\n", Fore.RED)
LunarSign= get_accurate_lunar_profile(datebirth)
Element=LunarSign[0]
Animal=LunarSign[1]
typer(f'You may not know, but your Chinese Zodiac sign is {Element} {Animal}.\n\n', Fore.LIGHTYELLOW_EX)
if Element=="Wood":
   typer("Wood is the element of growth, creativity, and adaptability. It represents the beginning of life and the potential for new beginnings. Wood is associated with the spring season, which is a time of renewal and growth.\n", Fore.GREEN)
   if Animal == 'Rat':
     typer("Rats are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Wood Rat, you are a creative problem-solver who uses their wit to build long-term security.\n", Fore.GREEN)
   elif Animal == 'Ox':
     typer("Oxen are hardworking and reliable, always putting in the effort to achieve their goals. They are also known for their patience and perseverance, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Ox, you are a patient worker with a hidden talent for artistic or innovative projects.\n", Fore.GREEN)
   elif Animal == 'Tiger':
     typer("Tigers are powerful and confident, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Tiger, you are a compassionate leader who fights fiercely for social justice and growth.\n", Fore.GREEN)
   elif Animal == 'Rabbit':
     typer("Rabbits are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Wood Rabbit, you are a gentle soul who excels at bringing people together through diplomacy.\n", Fore.GREEN)
   elif Animal == 'Dragon':
     typer("Dragons are powerful and wise, always seeking to improve themselves and the world around them. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Dragon, you are a visionary who uses their massive energy to build practical, lasting structures.\n", Fore.GREEN)
   elif Animal == 'Snake':
     typer("Snakes are wise and intelligent, always seeking to learn and grow. They are also known for their adaptability and resourcefulness, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Snake, you are an intuitive thinker who prefers to grow their wisdom in quiet, steady ways.\n", Fore.GREEN)
   elif Animal == 'Horse':
     typer("Horses are energetic and enthusiastic, always seeking to explore and experience new things. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Horse, you are a free spirit who seeks adventure but remains deeply loyal to their roots.\n", Fore.GREEN)
   elif Animal == 'Goat':
     typer("Goats are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Wood Goat, you are a sensitive artist who thrives when surrounded by nature and harmony.\n", Fore.GREEN)
   elif Animal == 'Monkey':
     typer("Monkeys are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Wood Monkey, you are a clever inventor who uses their adaptability to solve complex puzzles.\n", Fore.GREEN)
   elif Animal == 'Rooster':
     typer("Roosters are confident and assertive, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Rooster, you are a meticulous planner who values integrity and community growth.\n", Fore.GREEN)
   elif Animal == 'Dog':
     typer("Dogs are loyal and devoted, always looking out for the well-being of others. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Wood Dog, you are a devoted friend who is always looking for ways to improve the world.\n", Fore.GREEN)
   elif Animal == 'Pig':
     typer("Pigs are kind and gentle, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Wood Pig, you are a warm-hearted optimist who finds joy in simple, natural pleasures.\n", Fore.GREEN)
elif Element=="Fire":
   typer("Fire is the element of passion, energy, and transformation. It represents the power of creation and the ability to overcome obstacles. Fire is associated with the summer season, which is a time of growth and abundance.\n")
   if Animal == 'Rat':
     typer("Rats are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Fire Rat, you are a charismatic high-achiever who thrives on action and social recognition.\n", Fore.RED)
   elif Animal == 'Ox':
     typer("Oxen are hardworking and reliable, always putting in the effort to achieve their goals. They are also known for their patience and perseverance, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Ox, you are a powerhouse of stamina who leads others through sheer force of will.\n", Fore.RED)
   elif Animal == 'Tiger':
     typer("Tigers are powerful and confident, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Tiger, you are an unstoppable daredevil who lives life with intense, infectious passion.\n", Fore.RED)
   elif Animal == 'Rabbit':
     typer("Rabbits are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Fire Rabbit, you are a vibrant personality who hides a surprisingly competitive and spirited heart.\n", Fore.RED)
   elif Animal == 'Dragon':
     typer("Dragons are powerful and wise, always seeking to improve themselves and the world around them. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Dragon, you are a flamboyant leader who inspires others with their boldness and magnetism.\n", Fore.RED)
   elif Animal == 'Snake':
     typer("Snakes are wise and intelligent, always seeking to learn and grow. They are also known for their adaptability and resourcefulness, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Snake, you are a magnetic presence who uses their intense focus to achieve great power.\n", Fore.RED)
   elif Animal == 'Horse':
     typer("Horses are energetic and enthusiastic, always seeking to explore and experience new things. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Horse, you are a restless pioneer who moves through life with lightning speed and energy.\n", Fore.RED)
   elif Animal == 'Goat':
     typer("Goats are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Fire Goat, you are a assionate dreamer who is more assertive and expressive than other Goats.\n")
   elif Animal == 'Monkey':
     typer("Monkeys are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Fire Monkey, you are a confident showman who uses their brilliance to climb to the top.\n", Fore.RED)
   elif Animal == 'Rooster':
     typer("Roosters are confident and assertive, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Rooster, you are a dramatic perfectionist who demands excellence and commands attention.")
   elif Animal == 'Dog':
     typer("Dogs are loyal and devoted, always looking out for the well-being of others. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Fire Dog, you are a fierce protector who is deeply committed to their ideals and beliefs.\n", Fore.RED)
   elif Animal == 'Pig':
     typer("Pigs are kind and gentle, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Fire Pig, you are a courageous epicurean who pursues their desires with total enthusiasm.\n", Fore.RED)
elif Element=="Earth":
   typer("Earth is the element of stability, grounding, and nourishment. It represents the foundation of life and the ability to provide for others. Earth is associated with the transition between seasons, which is a time of change, where one must be grounded.\n")
   if Animal == 'Rat':
     typer("Rats are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As an Earth Rat, you are a pragmatic strategist who values material security and steady progress.\n")
   elif Animal == 'Ox':
     typer("Oxen are hardworking and reliable, always putting in the effort to achieve their goals. They are also known for their patience and perseverance, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Ox, you are the ultimate pillar of reliability—slow, steady, and incredibly grounded.\n")
   elif Animal == 'Tiger':
     typer("Tigers are powerful and confident, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Tiger, you are a realistic thinker who balances their bravery with careful calculation.\n")
   elif Animal == 'Rabbit':
     typer("Rabbits are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As an Earth Rabbit, you are a reserved individual who seeks peace through logic and careful planning.\n")
   elif Animal == 'Dragon':
     typer("Dragons are powerful and wise, always seeking to improve themselves and the world around them. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Dragon, you are a disciplined leader who focuses on building a solid and wealthy foundation.\n")
   elif Animal == 'Snake':
     typer("Snakes are wise and intelligent, always seeking to learn and grow. They are also known for their adaptability and resourcefulness, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Snake, you are a grounded intellectual who prefers facts and tangible results over theories.\n")
   elif Animal == 'Horse':
     typer("Horses are energetic and enthusiastic, always seeking to explore and experience new things. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Horse, you are a hard-working explorer who values consistency and physical endurance.\n")
   elif Animal == 'Goat':
     typer("Goats are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As an Earth Goat, you are a nurturing soul who finds stability in caring for their home and family.\n")
   elif Animal == 'Monkey':
     typer("Monkeys are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As an Earth Monkey, you are a focused professional who applies their cleverness to financial success.\n")
   elif Animal == 'Rooster':
     typer("Roosters are confident and assertive, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Rooster, you are a deep thinker who is highly organized and prefers a quiet, orderly life.\n")
   elif Animal == 'Dog':
     typer("Dogs are loyal and devoted, always looking out for the well-being of others. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As an Earth Dog, you are a stable guardian who is respected for their fairness and common sense.\n")
   elif Animal == 'Pig':
     typer("Pigs are kind and gentle, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As an Earth Pig, you are a productive worker who enjoys the rewards of their labor with family.\n")
elif Element=="Metal":
   typer("Metal is the element of strength, resilience, and perseverance. It represents the ability to bounce back, no matter what the the world throws at us. Metal is associated with the winter season, which is a time of reflection and introspection.\n")
   if Animal == 'Rat':
     typer("Rats are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Metal Rat, you are a sharp, ambitious individual who is driven by success and status.\n")
   elif Animal == 'Ox':
     typer("Oxen are hardworking and reliable, always putting in the effort to achieve their goals. They are also known for their patience and perseverance, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Ox, you are an iron-willed worker who is virtually impossible to sway from their path.\n")
   elif Animal == 'Tiger':
     typer("Tigers are powerful and confident, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Tiger, you are a fierce and independent warrior who demands respect and autonomy.\n")
   elif Animal == 'Rabbit':
     typer("Rabbits are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Metal Rabbit, you are a resilient survivor with a 'velvet glove' approach to hidden strength.\n")
   elif Animal == 'Dragon':
     typer("Dragons are powerful and wise, always seeking to improve themselves and the world around them. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Dragon, you are a powerful, uncompromising force who excels at massive undertakings.\n")
   elif Animal == 'Snake':
     typer("Snakes are wise and intelligent, always seeking to learn and grow. They are also known for their adaptability and resourcefulness, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Snake, you are a calculating, elegant individual with an incredibly focused mind.\n")
   elif Animal == 'Horse':
     typer("Horses are energetic and enthusiastic, always seeking to explore and experience new things. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Horse, you are a self-reliant traveler who prizes their freedom above all else.\n")
   elif Animal == 'Goat':
     typer("Goats are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Metal Goat, you are a creative person with a tough exterior who guards their artistic vision.\n")
   elif Animal == 'Monkey':
     typer("Monkeys are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Metal Monkey, you are a sophisticated strategist who is highly skilled in business and logic.\n")
   elif Animal == 'Rooster':
     typer("Roosters are confident and assertive, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Rooster, you are a sharp-tongued perfectionist with a brilliant eye for detail.\n")
   elif Animal == 'Dog':
     typer("Dogs are loyal and devoted, always looking out for the well-being of others. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Metal Dog, you are a disciplined protector who holds themselves and others to high standards.\n")
   elif Animal == 'Pig':
     typer("Pigs are kind and gentle, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Metal Pig, you are a proud and strong individual who is intensely loyal to their inner circle.\n")
elif Element=="Water":
   typer("Water is the element of adaptability, wisdom, and intuition. It represents the ability to flow with the current and the ability to find solutions to problems. Water is associated with the winter season, which is a time of reflection and introspection.\n")
   if Animal == 'Rat':
     typer("Rats are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Water Rat, you are a communicative charmer who can navigate any social or emotional tide.\n")
   elif Animal == 'Ox':
     typer("Oxen are hardworking and reliable, always putting in the effort to achieve their goals. They are also known for their patience and perseverance, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Ox, you are a flexible thinker who achieves their goals through patience and flow.\n")
   elif Animal == 'Tiger':
     typer("Tigers are powerful and confident, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Tiger, you are a reflective soul who uses their sensitivity to understand others' motives.\n")
   elif Animal == 'Rabbit':
     typer("Rabbits are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Water Rabbit, you are a highly intuitive empath who avoids conflict at all costs.\n")
   elif Animal == 'Dragon':
     typer("Dragons are powerful and wise, always seeking to improve themselves and the world around them. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Dragon, you are a wise leader who knows when to act and when to wait for the tide.\n")
   elif Animal == 'Snake':
     typer("Snakes are wise and intelligent, always seeking to learn and grow. They are also known for their adaptability and resourcefulness, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Snake, you are a profound thinker who is gifted at uncovering hidden truths.\n")
     typer("Water Snakes are the best sign!!!!!\n")
   elif Animal == 'Horse':
      typer("Horses are energetic and enthusiastic, always seeking to explore and experience new things. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
      typer("As a Water Horse, you are a versatile nomad who follows their intuition to find new horizons.\n")
   elif Animal == 'Goat':
     typer("Goats are gentle and kind, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Water Goat, you are a gentle, artistic spirit who is deeply attuned to the emotions of others.\n")
   elif Animal == 'Monkey':
     typer("Monkeys are clever and resourceful, always finding ways to adapt to their surroundings. They are also known for their strong sense of community and their ability to work together to achieve common goals.\n", Fore.GREEN)
     typer("As a Water Monkey, you are a persuasive genius who uses their wit to influence the world around them.\n")
   elif Animal == 'Rooster':
     typer("Roosters are confident and assertive, always taking charge of the situation. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Rooster, you are a refined intellectual who values clear communication and harmony.\n")
   elif Animal == 'Dog':
     typer("Dogs are loyal and devoted, always looking out for the well-being of others. They are also known for their strength and agility, which allows them to overcome even the most challenging obstacles.\n", Fore.GREEN)
     typer("As a Water Dog, you are a compassionate listener who is always ready to offer wise advice.\n")
   elif Animal == 'Pig':
     typer("Pigs are kind and gentle, always looking out for the well-being of others. They are also known for their creativity and imagination, which allows them to come up with unique and innovative solutions to problems.\n", Fore.GREEN)
     typer("As a Water Pig, you are a sociable soul who uses their intuition to create a happy, peaceful life.\n")

thisyearzodiac=get_accurate_lunar_profile(ct)
thisyearzodiacelement=thisyearzodiac[0]
thisyearzodiacanimal=thisyearzodiac[1]
typer(f"The current year is the year of the {thisyearzodiacelement} {thisyearzodiacanimal}.\n\n")
if thisyearzodiac==LunarSign:
  typer("This year is your year!\n")
elif thisyearzodiacanimal==Animal:
  typer("This year is your animal year!\n")
elif thisyearzodiacelement==Element:
  typer("This year is your element year!\n")

typer("But enough with Lunar new Year, now, let's calculate how long until your next birthday and start the countdown!\n\n")

while nextyearbd>ct:
  
  ct = dt.datetime.now()
  dd=nextyearbd-ct
  daysleft=dd.days
  totalsecondsleft=dd.seconds
  secondsleft=totalsecondsleft%60
  totalminutessleft=totalsecondsleft//60
  minutesleft=totalminutessleft%60
  hoursleft=totalminutessleft//60
  print(f"You have {daysleft} days, {hoursleft} hours, {minutesleft} minutes, and {secondsleft} seconds left until your next birthday.", end='\r')
  time.sleep(1)