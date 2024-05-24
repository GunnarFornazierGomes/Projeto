#calculadora uhul

running = True
while running:
  def soma():
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))
      print(f'O resultado da operação é {n1+n2}')
      calculadora()
  
  def sub():
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))
      print(f'O resultado da operação é {n1-n2}')
    
  
  def mult():
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))
      print(f'O resultado da operação é {n1*n2}')
  
  def div():
      n1 = int(input('Digite o primeiro número: '))
      n2 = int(input('Digite o segundo número: '))
      print(f'O resultado da operação é {n1/n2}')
  
  def calculadora():
      global running
      print('''
      /  _.| _    | _. _| _ .__. 
      \_(_||(_ |_||(_|(_|(_)|(_| 
  
      [1]soma  [2]subtração  [3]multiplicação  [4]divisão  [5]sair
      ''')
      inp = input("Qual operação gostaria de fazer?: ")
      match inp:
          case "1":
              soma()
          case "2":
              sub()
          case "3":
              mult()
          case "4":
              div()
          case "5":
              running = False
          case _:
              print("Opção inválida")
  
  calculadora()