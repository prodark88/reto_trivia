import random  # Importamos la librería random
import sys  #para finalizar el juego
import time  #para definir tiempo
#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0, tambien agregaremos intentos que iniciara en 0
iniciar_trivia = True
intentos = 0
puntaje = random.randint(0, 10)

#bienvenida del juego
time.sleep(1)  # Espera 1 segundos antes de continuar.
print(CYAN +'====BIENVENIDOS AL JUEGO DE LA TRIVIA====\n====HOY PONDREMOS A PRUEBA TU PASIÓN POR EL FUTBOL====\n')
time.sleep(2)  # Espera 2 segundos antes de continuar.
print(f'Empezaras el juego con {puntaje} puntos ')
#datos del usuario
time.sleep(1)  # Espera 2 segundos antes de continuar.
user_name = input("hola, para empezar el juego escribe tu nombre: "+RESET)


#loop del programa
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  time.sleep(1)  # Espera 1 segundos antes de continuar.
  #instruciones para el juego
  print(MAGENTA+f"\nEmpecemos {YELLOW+(user_name)} :D\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta:\n"+RESET)
  time.sleep(2)  # Espera 2 segundos antes de continuar.
  
  #datos
  question_1 = '¿Cuál fue el primer país africano en jugar un mundial?'
  question_2 = '¿Cuál de los siguientes jugadores hizo el primer gol en un mundial de fútbol?'
  question_3 = '¿Cuál fue el primer jugador más joven en anotar un gol en un mundial?'
  question_4 = '¿En qué año se jugó el partido de mayor goleada contra otro equipo en la historia de un mundial?'
  answer_1 = ['a) Egipto', 'b) Zimbabue', 'c) Etiopía', 'd) Nigeria']
  answer_2 = ['a) Delfín Benitez Cáceres', 'b) Lucien Laurent', 'c) Rafael Garza','d) Paolo Guerrero']
  answer_3 = ['a) Pelé', 'b) Roger Milla', 'c) Ronaldo', 'd) Maradona']
  answer_4 = ['a) 1981', 'b) 1979', 'c) 1982', 'd) 1970']
  
  #primera pregunta
  time.sleep(2)  # Espera 2 segundos antes de continuar.
  print(MAGENTA+ f'1) {question_1}\n'+RESET)
  for x in answer_1:
      print(x)
  respuesta_1 = input("\ningrese su respuesta:")
  while respuesta_1 not in ('a', 'b', 'c', 'd'):
      respuesta_1 = input(
          'tu alternativa no existe,elije unas de las opciones correctas: ')
  if respuesta_1 != 'a':
      puntaje -= random.randint(0, 10)
      print(
          RED +
          '\nincorrecto… Egipto fue el primer país africano en jugar un mundial.\nEsto ocurrió en el año 1934 en la edición que se jugó en Italia.\nSu primer, y único juego, fue contra Hungría,con el que perdieron 4 a 2.'
          + RESET)
  else:
      puntaje += random.randint(0, 10)
      print(BLUE+'\ncorrecto… Egipto fue el primer país africano en jugar un mundial.\nEsto ocurrió en el año 1934 en la edición que se jugó en Italia.\nSu primer, y único juego, fue contra Hungría,con el que perdieron 4 a 2.'+RESET)
  
  #segunda pregunta
  time.sleep(2)  # Espera 2 segundos antes de continuar.
  print(MAGENTA+f'\n2) {question_2}\n'+RESET)
  for x in answer_2:
      print(x)
  
  respuesta_2 = input("\ningrese su respuesta:")
  while respuesta_2 not in ('a', 'b', 'c', 'd'):
      respuesta_2 = input(
          'tu alternativa no existe,elije unas de las opciones correctas: ')
  if respuesta_2 != 'b':
      puntaje -= random.randint(0, 10)
      print(
          RED +
          '\n¡incorrecto! El Jugador francés, quien fue el autor del primer gol del primer mundial de fútbol.Fue en un juego Francia contra México.El gol se hizo en el minuto 19, y 4 minutos después vino el segundo. Esa disputa la ganó Francia 4 a 1.\n'
          + RESET)
  else:
      puntaje += random.randint(0, 10)
      print(BLUE+'\n¡correcto! El Jugador francés, quien fue el autor del primer gol del primer mundial de fútbol.Fue en un juego Francia contra México.El gol se hizo en el minuto 19,y 4 minutos después vino el segundo. Esa disputa la ganó Francia 4 a 1.'+RESET)
  
  #tercera pregunta
  time.sleep(2)  # Espera 2 segundos antes de continuar.
  print(MAGENTA+f'\n3) {question_3}\n'+RESET)
  for x in answer_3:
      print(x)
  
  respuesta_3 = input("\ningrese su respuesta:")
  while respuesta_3 not in ('a', 'b', 'c', 'd'):
      respuesta_3 = input(
          'tu alternativa no existe,elije unas de las opciones correctas: ')
  if respuesta_3 != 'a':
      puntaje -= random.randint(0, 10)
      print(RED +'\n¡Incorrecto!\nPelé tenía solo 17 años cuando anotó su primer gol en el mundial de 1958. El jugador de origen brasilero es el bicampeón más joven y el único en haber ganado tres títulos mundiales.\n'+ RESET)
  else:
      puntaje += random.randint(0, 10)
      print(BLUE+ '\n¡Correcto!\nPelé tenía solo 17 años cuando anotó su primer gol en el mundial de 1958. El jugador de origen brasilero es el bicampeón más joven y el único en haber ganado tres títulos mundiales.\n'+RESET)
  
  #numero de la suerte
  num_suerte = int(input('ingresa tu numero de la suerte del 1 al 10: '))
  
  #cuarta pregunta
  time.sleep(2)  # Espera 2 segundos antes de continuar.
  print(MAGENTA+f'\n4) {question_4}\n'+RESET)
  for x in answer_4:
      print(x)
  respuesta_4 = input("\ningrese su respuesta:")
  while respuesta_4 not in ('a', 'b', 'c', 'd'):
      respuesta_4 = input(
          'tu alternativa no existe,elije unas de las opciones correctas: ')
  if respuesta_4 != 'c' and respuesta_4 == 'a':
      puntaje = puntaje / 2
      print(MAGENTA +'\n¡ya estas mas cerca! En el Mundial de España 1982 se llevó a cabo un partido entre Hungría y El Salvador, dicho partido es recordado por la cantidad de goles que se anotaron, ya que Hungría ganó la disputa 10 goles por 0.\n'+ RESET)
  elif respuesta_4 == 'b' and respuesta_4 != 'c':
      puntaje += 5
      print(YELLOW + '\n¡Medianamente incorrecto! En el Mundial de España 1982 se llevó a cabo un partido entre Hungría y El Salvador, dicho partido es recordado por la cantidad de goles que se anotaron, ya que Hungría ganó la disputa 10 goles por 0.\n' + RESET)
  elif respuesta_4 == 'd' and respuesta_4 != 'c':
      puntaje -= 5
      print(RED +'\n¡Totalmente incorrecto! En el Mundial de España 1982 se llevó a cabo un partido entre Hungría y El Salvador, dicho partido es recordado por la cantidad de goles que se anotaron, ya que Hungría ganó la disputa 10 goles por 0.\n'+ RESET)
  else:
      puntaje = puntaje * 2
      print(BLUE +'\n¡Correcto! En el Mundial de España 1982 se llevó a cabo un partido entre Hungría y El Salvador, dicho partido es recordado por la cantidad de goles que se anotaron, ya que Hungría ganó la disputa 10 goles por 0.\n'+RESET)
  
  #felicitaciones por pasar el reto
  time.sleep(4)  # Espera 2 segundos antes de continuar.
  if respuesta_1 == 'a' and respuesta_2 == 'b' and respuesta_3 == 'a' and respuesta_4 == 'c':
      print(YELLOW+f'felicidades {user_name} pasaste el reto, tu puntaje final es de : {int(puntaje) + int(num_suerte)} '+RESET)
  else:print(RED+f' {user_name} fallaste el reto, solo acumulaste {int(puntaje) + int(num_suerte)} puntos'+RESET)


  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para   finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
    print(f'\n{user_name} Espero que lo hayas pasado bien, hasta pronto!')
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia 