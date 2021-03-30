
a = 1 
while (a):
  print('''
  -- menu --
  1) saludar
  2) despedirse
  0) sali  
  ''')
  try:
    a = int(input('ingresa el dato: '))
    if a == 1:
      print('hola, como estas?')
    elif a == 2:
      print('chao! que tengas un buen dia')
    else: 
      print('ingresa una opcion valida')
  except:
    pass
