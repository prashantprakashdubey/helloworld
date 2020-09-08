import random
n=20
a=int(n*random.random())+1
b=0
while a!=b:
  b=int(input('Enter a number between 1 to 20:'))
  if b>0 and b<=20:
    if a<b:
      print('number is too large')
    elif a>b:
      print('number is too small')
  else:
    print('You Quit')
    break
else:
  print('Congratulations!!! You Won')