import random



score = 0




rhs = 0
while True:
  try:
    num1 = int(input('Please give a number: \n'))
    break
  except ValueError:
    print("It must be a number")
    continue

while True:
  try:
    num2 = int(input('Please give another number: \n'))
    break
  except ValueError:
    print("It must be a number")
    continue
print('\n')

# list of operators
op_list = ['+', '-', '*']

op = random.randint(0,2)
#compute the output

#addition
if op == 0:
  rhs = num1 + num2

#subtract
if op ==1:
  rhs = num1 - num2

#multipy
if op == 2:
  rhs = num1 * num2

print('Can you guess the missing operator?')
answer = input(str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n')


#check if the answer is correct

if answer == op_list[op]:
  print("Good Job")
  score = score + 1
else:
  print("You have no skills.")
  score = score
  print("The correct answer is " + op_list[op], sep = ' ')
  print(str(num1) + ' ' + op_list[op] + ' ' + str(num2) + ' = ' + str(rhs) + '\n', sep = '')

print()
print()
print('Now a 3 number question...')

#3rd number
num3 = random.randint(1,100)

#2 operators


#+,- only
op1 = random.randint(0,1)
op2 = random.randint(0,1)

if op1 == 0:
  rhs = num1 + num2

if op1==1:
  rhs = num1 - num2

if op2 == 0:
  rhs = rhs + num3

if op2 == 1:
  rhs = rhs - num3

print('Can you guess the missing operator?')
qn = str(num1) + '__' + str(num2) + '__' + str(num3) + '=' + str(rhs) + '\n'

answer = input(qn + '\n')

if len(answer) >= 2:
  if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
    print('Well done')
    score = score + 1
  else:
    print("*Snort*", 'Wrong as ever', sep = '\n')
    score = score
    print('The corerct answer is', op_list[op1], op_list[op2], sep = ' ')
    print(str(num1) + op_list[op1] + str(num2) + op_list[op2] + str(num3) + '=' + str(rhs) + '\n', sep = ' ')
else:
  print('Erm...')

#Start the longer question
print()
print('Now for a long question... \n')

n_numbers = 6
list_numbers = []
list_ops = []

#Getting numbers and operators

for kk in range(n_numbers):
  list_numbers.append(random.randint(1,100))

for kk in range(n_numbers-1):
  list_ops.append(op_list[random.randint(0, 2)])

list_numbers_new = []
list_ops_new = []

for kk in range(len(list_numbers)):
  list_numbers_new.append(list_numbers[kk])

for kk in range(len(list_ops)):
  list_ops_new.append(list_ops[kk])


while '*' in list_ops_new:
  idx = list_ops_new.index('*')
  res = list_numbers_new[idx] * list_numbers_new[idx+1]
  del list_ops_new[idx]
  list_numbers_new[idx] = res
  del list_numbers_new[idx + 1]




print()



#Generate RHS

rhs = list_numbers_new[0]
for kk in range(len(list_ops_new)):
  if list_ops_new[kk] == '+':
    rhs = rhs + list_numbers_new[kk+1]
  elif list_ops_new[kk] == '-':
    rhs = rhs - list_numbers_new[kk+1]

temp = ''
for kk in range(n_numbers):
  if kk <= n_numbers - 2:
    temp = temp + str(list_numbers[kk]) + list_ops[kk]
  else:
    temp = temp + str(list_numbers[kk])

rhs1 = eval(temp)


print()
print("Can you guess the missing operators?")

qn = ''

for kk in range(n_numbers):
  if kk <= n_numbers - 2:
    qn = qn + str(list_numbers[kk]) + '__'
  else:
    qn = qn + str(list_numbers[kk]) + ' = ' + str(rhs) + '\n'


answer = input(qn + '\n')
while True:
  if len(answer) >= 2:
    break
  else:
    print("Ummm... I don't think so.")
    break

#Prepare correct staement
qn = ' '

for kk in range(n_numbers):
  if kk <= n_numbers - 2:
    qn = qn + str(list_numbers[kk]) + ' ' + list_ops[kk] + ' '
  else:
    qn = qn + str(list_numbers[kk]) + ' = ' + str(rhs) + '\n'




#Checking answer

for kk in range(n_numbers-1):
  if answer[kk] == list_ops[kk]:
    if kk == n_numbers-2:
      print('I suppose you passed this question...')
      score = score + 1
  else:
    print('Wrong as ever.')
    score = score
    print('The correct answer is', list_ops)
    print(qn)
    break 
print()

#Score


print(score, 'out of 3')

