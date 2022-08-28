#Juego de superheroes al estilo pokemon

import time
import numpy as np
import sys
import random

#IMAGEN import
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#NOTA: 180 PS "="


#Lista de superheroes
superheroes= ['* Superman', '* Homelander', '* Scarlet Witch', '* Doctor Strange', '* Deep', '* Daredevil', '* Wolverine', '* Batman', '* Moon Knight', '* Phoenix', '* Magneto', '* Raven', '* Spiderman', '* Black Widow', '* Green Arrow', '* Flash','* Storm', '* Deadpool', '* Baby Groot']

#Delay print()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


#Definir clase
class Superheroe:
    def __init__(self, name, types, moves, move1, move2, move3, move4, EVs, health='====================================================================================================================================================================================='):
        # información del superheroe variables
        self.name = name
        self.types = types
        self.moves = moves
        self.move1 = move1 ['VALOR1']
        self.move2 = move2['VALOR2']
        self.move3 = move3 ['VALOR3']
        self.move4 = move4['RESTAURAR']
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 180 # BARRA DE SALUD (cantidad de # puestos)

    def fight(self, Superheroe2):

        
        # BATALLA!!
        print(f"\n{self.name}")
        print("TIPO/", self.types)
        print("ATAQUE/", self.attack)
        print("DEFENSA/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Superheroe2.name}")
        print("TIPO/", Superheroe2.types)
        print("ATAQUE/", Superheroe2.attack)
        print("DEFENSA/", Superheroe2.defense)
        print("LVL/", 3*(1+np.mean([Superheroe2.attack,Superheroe2.defense])))

        # Ventajas y desventajas
        version = ['Habil', 'Mutante', 'Tecnologico', 'Cosmico', 'Mistico', 'Cientifico']
        for i,k in enumerate(version):
            if self.types == k:
                # Del mismo tipo
                if Superheroe2.types == k:
                    string_1_attack = '\nNeutro'
                    string_2_attack = '\nNeutro'
                    

                # Superheroe2 tiene ventaja
                if Superheroe2.types == version[(i+1)%6]:
                    Superheroe2.attack = Superheroe2.attack + Superheroe2.attack*0.2
                    Superheroe2.defense = Superheroe2.defense + Superheroe2.defense*0.2
                    self.attack = self.attack-self.attack*0.1
                    self.defense = self.defense-self.defense*0.1
                    string_1_attack = '\nNo es muy efectivo...'
                    string_2_attack = '\n¡Es super efectivo!'

                # Superheore2 es debil
                if Superheroe2.types == version[(i+5)%6]:
                    self.attack = self.attack+ self.attack*0.2
                    self.defense = self.defense + self.attack*0.2
                    Superheroe2.attack = Superheroe2.attack-Superheroe2.attack*0.1
                    Superheroe2.defense =Superheroe2.defense-Superheroe2.defense*0.1
                    string_1_attack = '\n¡Es superefectivo!'
                    string_2_attack = '\nNo es muy efectivo...'
                #Superheroe2 NEUTROS
                if Superheroe2.types == version[(i+2)%6]:
                  string_1_attack = ''
                  string_2_attack = ''

                if Superheroe2.types == version[(i+3)%6]:
                  string_1_attack = ''
                  string_2_attack = ''
                
                if Superheroe2.types == version[(i+4)%6]:
                  string_1_attack = ''
                  string_2_attack = ''


      #Turnos atacando  
        while (self.bars > 0) and (Superheroe2.bars > 0):
          # Print() salud de cada superheroe
          print(f"\n{self.name}\t\tPS\t{self.health}")
          print(f"{Superheroe2.name}\t\tPS\t{Superheroe2.health}\n")
            
          #Self / Pokemon1
          print(f"¡Adelante {self.name}!")
          for i, x in enumerate(self.moves):
              print(f"{i+1}.", x)
          index = int(input('Elige un movimiento: '))
          delay_print(f"\n¡{self.name} usó {self.moves[index-1]}!")
          time.sleep(1)
          delay_print(string_1_attack)
          
            
          # Determinar daño
          if index == 1:
            print(f"\nEste ataque vale: {self.move1}\n")
            Superheroe2.bars -= (self.move1+(self.attack*0.1))
            Superheroe2.health = ""
          elif index == 2:
            print(f"\nEste ataque vale: {self.move2}\n")
            Superheroe2.bars -= (self.move2+(self.attack*0.1))
            Superheroe2.health = ""
          elif index == 3:
            print(f"\nEste ataque vale: {self.move3}\n")
            Superheroe2.bars -= (self.move3+(self.attack*0.1))
            Superheroe2.health = ""
          elif index == 4:
            print(f"\nTu salud ha aumentado: {self.move4}\n")
            self.bars += self.move4
            self.health = ""
          else:
            print("ERROR")
          
          #CONITINUACION BATALLA
          Superheroe2.bars = Superheroe2.bars+0.1*Superheroe2.defense
          if index == 1:
            delay_print(f"\nLe quedan {Superheroe2.bars} PS a tu contrincante\n")
          elif index == 2:
            delay_print(f"\nLe quedan {Superheroe2.bars} PS a tu contrincante\n")
          elif index == 3:
            delay_print(f"\nLe quedan {Superheroe2.bars} PS a tu contrincante\n")
          elif index == 4:
            delay_print(f"\nLe quedan {Superheroe2.bars} PS a tu contrincante\n")
          else:
            print("ERROR")  
          
            
          # Agragar barras adicionales
          if index == 4:
            for j in range(int(self.bars+.1*self.defense)):
              self.health += "="
          else:
            for j in range(int(Superheroe2.bars)):
              Superheroe2.health += "="


          
          time.sleep(1)
          print(f"\n{self.name}\t\tPS\t{self.health}")
          print(f"{Superheroe2.name}\t\tPS\t{Superheroe2.health}\n")
          time.sleep(.5)
        
          # Comprobar si el superheroe esta fuera de combate
          if Superheroe2.bars <= 0:
              delay_print("\n..." + Superheroe2.name + ' está fuera de combate!')
              money = np.random.choice(5000)
              delay_print(f"\n{Superheroe2.name} te pagó {money}€\n")
              delay_print(f"Enhorabuena {self.name} hoy no te quedas sin comer")
            
              break

          # ¡HACER LO MISMO CON --SUPERHEROE2--!

          print(f"¡Adelante {Superheroe2.name}!")
          for i, x in enumerate(Superheroe2.moves):
              print(f"{i+1}.", x)
          index = int(input('Elige un movimiento: '))
          delay_print(f"\n¡{Superheroe2.name} usó {Superheroe2.moves[index-1]}!")
          time.sleep(1)
          delay_print(string_2_attack)

          # Determinar daño
          if index == 1:
            print(f"\nEste ataque vale: {Superheroe2.move1}\n")
            self.bars -= (Superheroe2.move1+(Superheroe2.attack*0.1))
            self.health = ""
          elif index == 2:
            print(f"\nEste ataque vale: {Superheroe2.move2}\n")
            self.bars -= (Superheroe2.move2+(Superheroe2.attack*0.1))
            self.health = ""
          elif index == 3:
            print(f"\nEste ataque vale: {Superheroe2.move3}\n")
            self.bars -= (Superheroe2.move3+(Superheroe2.attack*0.1))
            self.health = ""
          elif index == 4:
            print(f"\nTu salud sube: {Superheroe2.move4}\n")
            Superheroe2.bars += Superheroe2.move4
            Superheroe2.health = ""
          else:
            print("ERROR")
          
          #CONTINUACION BATALLA
          self.bars = self.bars+.1*self.defense
          if index == 1:
            delay_print(f"\nLe quedan {self.bars} PS a tu contrincante\n")
          elif index == 2:
            delay_print(f"\nLe quedan {self.bars} PS a tu contrincante\n")
          elif index == 3:
            delay_print(f"\nLe quedan {self.bars} PS a tu contrincante\n")
          elif index ==4:
            delay_print(f"\nLe quedan {self.bars} PS a tu contrincante\n")
          else:
            print("ERROR")

          # Agragar barras adicionales
          if index == 4:
            for j in range(int(Superheroe2.bars+0.1*Superheroe2.defense)):
              Superheroe2.health += "="
          else:
            for j in range(int(self.bars)):
              self.health += "="
                    
          
          time.sleep(1)
          print(f"\n{self.name}\t\tPS{self.health}")
          print(f"{Superheroe2.name}\t\tPS{Superheroe2.health}\n")
          time.sleep(.5)
          print("##############################################")
          

          # Comprobar si el superheroe esta fuera de combate
          if self.bars <= 0:
              delay_print("\n..." + self.name + ' esta fuera de combate!')
              money = np.random.choice(5000)
              delay_print(f"\n{self.name} te pagó {money}€\n")
              delay_print(f"Enhorabuena {Superheroe2.name} hoy no te quedas sin comer")
              break
              
        #Información de lucha
        #self.impress(Superheroe2)
        #Considerar la ventaja de tipo
        #string_1_attack, string_2_attack = self.ventaja(Superheroe2)
        #Continua mientras el pokemon aun tenfa puntos de salud
        #self.turno(Superheroe2, string_1_attack, string_2_attack)
        #Recibir dinero
        

#CREAR PERSONAJE
if __name__ == '__main__':
  
  #TECNOLOGICO
  batman = Superheroe('Batman', 'Tecnologico', ['Superbatmovil' , 'Batpatada', 'Batostia'],{'VALOR1':40}, {'VALOR2':33}, {'VALOR3':25},{'RESTAURAR': 0}, {'ATTACK':14, 'DEFENSE': 11}) #HECHO
  greenarrow = Superheroe('Green Arrow', 'Tecnologico', ['Flecha explosiva', 'Flecha puño', 'Lluvia de flechas'],{'VALOR1':22}, {'VALOR2':30}, {'VALOR3':35},{'RESTAURAR': 0},{'ATTACK': 14, 'DEFENSE':11}) #HECHO
  
  #MUTANTE
  magneto = Superheroe('Magneto', 'Mutante', [ 'Rafaga de metales cortantes', 'Falta de hierro en sangre', 'Esferas metalicas flotantes'],{'VALOR1':32}, {'VALOR2':35}, {'VALOR3':20},{'RESTAURAR': 0},{'ATTACK': 18, 'DEFENSE':13}) #HECHO
  storm = Superheroe('Storm', 'Mutante', ['Rayo', 'Viento agitado', 'Tormenta electrica'],{'VALOR1':30}, {'VALOR2':18}, {'VALOR3':45},{'RESTAURAR': 0},{'ATTACK': 18, 'DEFENSE':13}) #HECHO
  phoenix = Superheroe('Phoenix', 'Mutante', ['Telequinsis', 'Control mental', 'Desintegración'],{'VALOR1':25}, {'VALOR2':40}, {'VALOR3':55},{'RESTAURAR': 0},{'ATTACK': 22, 'DEFENSE':22}) #HECHO
  wolverine = Superheroe('Wolverine', 'Mutante', ['Garras metalicas','Patada','Dobles garras','Curacion'],{'VALOR1':25}, {'VALOR2':18}, {'VALOR3':40},{'RESTAURAR': 15},{'ATTACK': 18, 'DEFENSE':13}) #HECHO
  deadpool = Superheroe('Deadpool', 'Mutante', ['Puño', 'Espada Samurai', 'Doble disparo', 'Curacion'],{'VALOR1':18}, {'VALOR2':35}, {'VALOR3':30},{'RESTAURAR': 15},{'ATTACK': 18, 'DEFENSE':13}) #HECHO
  
  #COSMICO
  superman = Superheroe('Superman', 'Cosmico', ['Viento congelante', 'Super Patada', 'Rayo laser'],{'VALOR1':20}, {'VALOR2':35}, {'VALOR3':50},{'RESTAURAR': 0},{'ATTACK': 20, 'DEFENSE':25}) #HECHO
  groot = Superheroe('Baby Groot', 'Cosmico', ['Brazos alargantes', 'Cara adorable', 'Yo soy Groot'],{'VALOR1':25}, {'VALOR2':35}, {'VALOR3':60},{'RESTAURAR': 0},{'ATTACK': 25, 'DEFENSE':25}) #HECHO
  
  #MÍSTICO
  raven = Superheroe('Raven', 'Mistico', ['Bola Sombra', 'Maleficio', 'Invocación demonios', 'Curación'],{'VALOR1':28}, {'VALOR2':38}, {'VALOR3':58},{'RESTAURAR': 10},{'ATTACK': 23, 'DEFENSE':22}) #HECHO
  doctorstrange = Superheroe('Doctor Strange', 'Mistico', ['Golpes Capa', 'Teletransportación', 'Libro de los Vishanti'],{'VALOR1':20}, {'VALOR2':33}, {'VALOR3':58},{'RESTAURAR': 0},{'ATTACK': 18, 'DEFENSE':17})
  scarletwitch = Superheroe('Scarlet Witch', 'Mistico', ['Telequinesis', 'Magia del Caos', 'Darkhold'],{'VALOR1':15}, {'VALOR2':48}, {'VALOR3':54}, {'RESTAURAR': 0},{'ATTACK': 25, 'DEFENSE':22})

  
  #CIENTIFICO
  homelander = Superheroe('Homelander', 'Cientifico', ['Mala Leche', 'Flecha puño', 'Flechas explosivas'],{'VALOR1':15}, {'VALOR2':30}, {'VALOR3':50},{'RESTAURAR': 0},{'ATTACK': 16, 'DEFENSE':19})
  spiderman = Superheroe('Spiderman', 'Cientifico', ['Telarañas', 'Patada voladora', 'Spiderman multiversal','Curacion'],{'VALOR1':25}, {'VALOR2':30}, {'VALOR3':60},{'RESTAURAR': 10},{'ATTACK': 17, 'DEFENSE':15})
  flash = Superheroe('Flash', 'Cientifico', ['Brazos tornado', 'Rayo', 'Viaje en el tiempo','Curacion'],{'VALOR1':25}, {'VALOR2':30}, {'VALOR3':60},{'RESTAURAR': 10},{'ATTACK': 18, 'DEFENSE':15})
  deep = Superheroe('Deep', 'Cientifico', ['Real eyes relize real lies', 'Pulpo Acompañante', 'Wannabe'],{'VALOR1':25}, {'VALOR2':30}, {'VALOR3':35},{'RESTAURAR': 0},{'ATTACK': 10, 'DEFENSE':8})
  
  #HABIL
  blackwidow = Superheroe('Black Widow', 'Habil', ['Patada letal', 'Bastones electricos', 'Widow Bites'],{'VALOR1':28}, {'VALOR2':34}, {'VALOR3':40},{'RESTAURAR': 0},{'ATTACK': 19, 'DEFENSE':13})
  moonknight = Superheroe('Moon Knight', 'Habil', ['Superpatada de Steven', 'Dardos de Media Luna de Marc', 'Tajada letal de Konshu', 'Curacion'],{'VALOR1':25}, {'VALOR2':33}, {'VALOR3':50},{'RESTAURAR': 10},{'ATTACK':19, 'DEFENSE':13})
  daredevil = Superheroe('Daredevil', 'Habil', ['Movimientos ninja', 'Bastones Billy Club', 'Combo de pueñetazos letales'],{'VALOR1':25}, {'VALOR2':38}, {'VALOR3':48},{'RESTAURAR': 0},{'ATTACK': 19, 'DEFENSE':13})
  
  # PERSONAJE LISTA RANDOM
  x= [batman, greenarrow, magneto, storm, phoenix, wolverine, deadpool, superman, groot, raven, doctorstrange, scarletwitch, homelander, spiderman, flash, deep, blackwidow, moonknight, daredevil]
  
 
  def imagen():
    img = mpimg.imread('DIAGRAMA.PNG')
    imgplot = plt.imshow(img)
    plt.show()

    
  # BATALLA
  
  #ACCION 1
  def accion():
    delay_print("\n-----SUPERHEROE BATTLE-----")
    print("\n--------（＞ｙ＜）---------\n")
    delay_print("Deadpool: Bienvenidos a la competición de los mejores Superheroes. \nPreparen sus palomitas porque empieza el combate.\n")
    print("")
    delay_print("\nINSTRUCCIONES\n")
    delay_print("\nPara seleccionar el moviemiento: introduzca su número correspondiente\n")
    time.sleep(1)
    print("\nLISTA DE SUPERHEROES\n")
    print(*superheroes, sep = "\n")
    print(" ") 
    time.sleep(1)
    delay_print("\nDIAGRAMA\n")
    delay_print("\nAntes de empezar observa el diagrama adjutado para poder elegir más concienzudamente\ntu personaje (cierra la imagen para el progama siga compilando)\n")
    imagen()
    time.sleep(2)
    personaje= input("\nElige a un superheroe: ")
    if personaje == 'Batman'or personaje == 'batman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        batman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        batman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        batman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        batman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        batman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        batman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        batman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        batman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        batman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        batman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        batman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        batman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        batman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        batman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        batman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        batman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        batman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        batman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        batman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Green Arrow' or personaje =='green arrow':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman'or personaje2 == 'batman':
        greenarrow.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        greenarrow.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        greenarrow.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        greenarrow.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        greenarrow.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        greenarrow.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        greenarrow.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        greenarrow.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        greenarrow.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        greenarrow.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        greenarrow.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        greenarrow.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        greenarrow.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        greenarrow.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        greenarrow.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        greenarrow.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        greenarrow.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        greenarrow.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        greenarrow.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Magneto' or personaje == 'magneto':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        magneto.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        magneto.fight(greenarrow)
      elif personaje2 == 'Magneto' or personaje2 == 'magneto':
        magneto.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        magneto.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        magneto.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        magneto.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        magneto.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        magneto.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        magneto.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        magneto.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        magneto.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        magneto.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        magneto.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        magneto.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        magneto.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        magneto.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        magneto.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        magneto.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        magneto.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Storm' or personaje == 'storm':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        storm.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        storm.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        storm.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        storm.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        storm.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        storm.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        storm.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        storm.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        storm.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        storm.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        storm.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        storm.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        storm.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        storm.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        storm.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        storm.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        storm.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        storm.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        storm.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Phoenix' or personaje == 'phoenix':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        phoenix.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        phoenix.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        phoenix.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        phoenix.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        phoenix.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        phoenix.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        phoenix.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        phoenix.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        phoenix.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        phoenix.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        phoenix.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        phoenix.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        phoenix.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        phoenix.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        phoenix.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        phoenix.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        phoenix.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        phoenix.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        phoenix.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Wolverine' or personaje == 'wolverine':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        wolverine.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        wolverine.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        wolverine.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        wolverine.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        wolverine.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        wolverine.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        wolverine.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        wolverine.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        wolverine.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        wolverine.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        wolverine.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        wolverine.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        wolverine.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        wolverine.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        wolverine.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        wolverine.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        wolverine.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        wolverine.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        wolverine.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Deadpool' or personaje == 'deadpool':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        deadpool.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        deadpool.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        deadpool.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        deadpool.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        deadpool.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        deadpool.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        deadpool.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        deadpool.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        deadpool.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        deadpool.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        deadpool.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        deadpool.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        deadpool.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        deadpool.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        deadpool.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        deadpool.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        deadpool.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        deadpool.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        deadpool.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Superman' or personaje == 'superman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        superman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        superman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        superman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        superman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        superman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        superman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        superman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        superman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        superman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        superman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        superman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        superman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        superman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        superman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flas':
        superman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        superman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'back widow':
        superman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        superman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        superman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Baby Groot' or personaje == 'baby groot':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        groot.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        groot.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        groot.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        groot.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        groot.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        groot.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        groot.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        groot.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        groot.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        groot.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        groot.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        groot.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        groot.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        groot.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        groot.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        groot.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        groot.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        groot.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        groot.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Raven' or personaje == 'raven':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        raven.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        raven.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        raven.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        raven.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        raven.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        raven.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        raven.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        raven.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        raven.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        raven.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        raven.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        raven.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        raven.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        raven.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        raven.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        raven.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        raven.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        raven.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        raven.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Doctor Strange' or personaje == 'doctor strange':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        doctorstrange.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        doctorstrange.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        doctorstrange.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        doctorstrange.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        doctorstrange.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        doctorstrange.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        doctorstrange.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        doctorstrange.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        doctorstrange.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        doctorstrange.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        doctorstrange.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        doctorstrange.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        doctorstrange.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        doctorstrange.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        doctorstrange.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        doctorstrange.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        doctorstrange.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        doctorstrange.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        doctorstrange.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Scarlet Witch' or personaje == 'scarlet witch' :
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        scarletwitch.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        scarletwitch.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        scarletwitch.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        scarletwitch.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        scarletwitch.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        scarletwitch.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        scarletwitch.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        scarletwitch.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        scarletwitch.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        scarletwitch.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strage':
        scarletwitch.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        scarletwitch.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        scarletwitch.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        scarletwitch.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        scarletwitch.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        scarletwitch.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        scarletwitch.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        scarletwitch.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        scarletwitch.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Homelander' or personaje == 'homelander':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        homelander.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        homelander.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        homelander.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        homelander.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        homelander.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        homelander.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        homelander.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        homelander.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        homelander.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        homelander.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        homelander.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        homelander.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        homelander.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        homelander.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        homelander.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        homelander.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        homelander.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        homelander.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        homelander.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Spiderman' or personaje == 'spiderman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        spiderman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        spiderman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        spiderman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        spiderman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        spiderman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        spiderman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        spiderman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        spiderman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        spiderman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        spiderman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        spiderman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        spiderman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        spiderman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        spiderman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        spiderman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        spiderman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        spiderman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        spiderman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        spiderman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Flash' or personaje == 'flash':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        flash.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        flash.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
         flash.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        flash.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        flash.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        flash.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        flash.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        flash.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        flash.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        flash.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        flash.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        flash.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        flash.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        flash.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        flash.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        flash.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        flash.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        flash.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        flash.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Deep' or personaje == 'deep':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        deep.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        deep.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        deep.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        deep.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        deep.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        deep.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        deep.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        deep.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        deep.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        deep.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        deep.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        deep.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        deep.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        deep.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        deep.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        deep.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        deep.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knigt':
        deep.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        deep.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Black Widow' or personaje == 'black widow':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        blackwidow.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        blackwidow.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        blackwidow.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        blackwidow.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        blackwidow.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        blackwidow.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        blackwidow.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        blackwidow.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        blackwidow.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        blackwidow.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor stange':
        blackwidow.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        blackwidow.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        blackwidow.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        blackwidow.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        blackwidow.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        blackwidow.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        blackwidow.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        blackwidow.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        blackwidow.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Moon Knight' or personaje == 'moon knight':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        moonknight.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        moonknight.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        moonknight.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        moonknight.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        moonknight.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        moonknight.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        moonknight.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        moonknight.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        moonknight.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        moonknight.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        moonknight.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        moonknight.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        moonknight.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        moonknight.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        moonknight.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        moonknight.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        moonknight.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        moonknight.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        moonknight.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Daredevil' or personaje == 'daredevil':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        daredevil.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        daredevil.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        daredevil.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        daredevil.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        daredevil.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        daredevil.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        daredevil.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        daredevil.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        daredevil.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        daredevil.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        daredevil.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        daredevil.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        daredevil.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        daredevil.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        daredevil.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        daredevil.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        daredevil.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        daredevil.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        daredevil.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        print("")
        accion()
    else:
      print("\nPrueba a introducir de nuevo al personaje\n")
      print("")
      accion()

  #ACCION 2
  def accion2():
    delay_print("\n-----SUPERHEROE BATTLE-----")
    print("\n--------（＞ｙ＜）---------\n")
    time.sleep(1)
    print("\nLISTA DE SUPERHEROES\n")
    print(*superheroes, sep = "\n")
    print(" ") 
    time.sleep(1)
    delay_print("\nDIAGRAMA\n")
    print("\nObserva el diagrama\n")
    imagen()
    time.sleep(2)
    personaje= input("\nElige a un superheroe: ")
    if personaje == 'Batman'or personaje == 'batman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        batman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        batman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        batman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        batman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        batman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        batman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        batman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        batman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        batman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        batman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        batman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        batman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        batman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        batman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        batman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        batman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        batman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        batman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        batman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Green Arrow' or personaje =='green arrow':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman'or personaje2 == 'batman':
        greenarrow.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        greenarrow.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        greenarrow.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        greenarrow.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        greenarrow.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        greenarrow.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        greenarrow.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        greenarrow.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        greenarrow.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        greenarrow.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        greenarrow.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        greenarrow.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        greenarrow.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        greenarrow.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        greenarrow.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        greenarrow.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        greenarrow.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        greenarrow.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        greenarrow.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Magneto' or personaje == 'magneto':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        magneto.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        magneto.fight(greenarrow)
      elif personaje2 == 'Magneto' or personaje2 == 'magneto':
        magneto.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        magneto.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        magneto.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        magneto.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        magneto.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        magneto.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        magneto.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        magneto.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        magneto.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        magneto.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        magneto.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        magneto.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        magneto.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        magneto.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        magneto.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        magneto.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        magneto.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Storm' or personaje == 'storm':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        storm.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        storm.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        storm.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        storm.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        storm.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        storm.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        storm.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        storm.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        storm.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        storm.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        storm.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        storm.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        storm.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        storm.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        storm.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        storm.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        storm.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        storm.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        storm.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Phoenix' or personaje == 'phoenix':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        phoenix.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        phoenix.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        phoenix.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        phoenix.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        phoenix.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        phoenix.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        phoenix.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        phoenix.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        phoenix.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        phoenix.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        phoenix.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        phoenix.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        phoenix.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        phoenix.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        phoenix.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        phoenix.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        phoenix.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        phoenix.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        phoenix.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Wolverine' or personaje == 'wolverine':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        wolverine.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        wolverine.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        wolverine.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        wolverine.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        wolverine.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        wolverine.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        wolverine.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        wolverine.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        wolverine.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        wolverine.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        wolverine.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        wolverine.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        wolverine.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        wolverine.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        wolverine.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        wolverine.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        wolverine.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        wolverine.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        wolverine.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Deadpool' or personaje == 'deadpool':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        deadpool.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        deadpool.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        deadpool.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        deadpool.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        deadpool.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        deadpool.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        deadpool.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        deadpool.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        deadpool.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        deadpool.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        deadpool.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        deadpool.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        deadpool.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        deadpool.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        deadpool.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        deadpool.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        deadpool.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        deadpool.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        deadpool.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Superman' or personaje == 'superman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        superman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        superman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        superman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        superman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        superman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        superman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        superman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        superman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        superman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        superman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        superman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        superman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        superman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        superman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flas':
        superman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        superman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'back widow':
        superman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        superman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        superman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Baby Groot' or personaje == 'baby groot':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        groot.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        groot.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        groot.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        groot.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        groot.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        groot.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        groot.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        groot.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        groot.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        groot.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        groot.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        groot.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        groot.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        groot.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        groot.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        groot.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        groot.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        groot.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        groot.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Raven' or personaje == 'raven':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        raven.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        raven.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        raven.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        raven.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        raven.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        raven.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        raven.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        raven.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        raven.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        raven.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        raven.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        raven.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        raven.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        raven.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        raven.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        raven.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        raven.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        raven.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        raven.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Doctor Strange' or personaje == 'doctor strange':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        doctorstrange.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        doctorstrange.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        doctorstrange.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        doctorstrange.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        doctorstrange.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        doctorstrange.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        doctorstrange.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        doctorstrange.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        doctorstrange.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        doctorstrange.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        doctorstrange.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        doctorstrange.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        doctorstrange.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        doctorstrange.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        doctorstrange.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        doctorstrange.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        doctorstrange.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        doctorstrange.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        doctorstrange.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Scarlet Witch' or personaje == 'scarlet witch' :
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        scarletwitch.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        scarletwitch.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        scarletwitch.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        scarletwitch.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        scarletwitch.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        scarletwitch.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        scarletwitch.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        scarletwitch.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        scarletwitch.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        scarletwitch.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strage':
        scarletwitch.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        scarletwitch.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        scarletwitch.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        scarletwitch.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        scarletwitch.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        scarletwitch.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        scarletwitch.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        scarletwitch.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        scarletwitch.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Homelander' or personaje == 'homelander':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        homelander.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        homelander.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        homelander.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        homelander.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        homelander.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        homelander.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        homelander.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        homelander.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        homelander.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        homelander.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        homelander.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        homelander.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        homelander.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        homelander.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        homelander.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        homelander.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        homelander.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        homelander.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        homelander.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Spiderman' or personaje == 'spiderman':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        spiderman.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        spiderman.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        spiderman.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        spiderman.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        spiderman.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        spiderman.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        spiderman.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        spiderman.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        spiderman.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        spiderman.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        spiderman.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        spiderman.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        spiderman.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        spiderman.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        spiderman.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        spiderman.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        spiderman.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        spiderman.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        spiderman.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Flash' or personaje == 'flash':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        flash.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        flash.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
         flash.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        flash.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        flash.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        flash.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        flash.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        flash.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        flash.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        flash.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        flash.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        flash.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        flash.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        flash.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        flash.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        flash.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        flash.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        flash.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        flash.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Deep' or personaje == 'deep':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        deep.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        deep.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        deep.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        deep.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        deep.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        deep.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        deep.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        deep.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        deep.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        deep.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        deep.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        deep.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        deep.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        deep.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        deep.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        deep.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        deep.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knigt':
        deep.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        deep.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Black Widow' or personaje == 'black widow':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        blackwidow.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        blackwidow.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        blackwidow.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        blackwidow.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        blackwidow.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        blackwidow.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        blackwidow.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        blackwidow.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        blackwidow.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        blackwidow.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor stange':
        blackwidow.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        blackwidow.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        blackwidow.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        blackwidow.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        blackwidow.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        blackwidow.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        blackwidow.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        blackwidow.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        blackwidow.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Moon Knight' or personaje == 'moon knight':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        moonknight.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        moonknight.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        moonknight.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        moonknight.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        moonknight.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        moonknight.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        moonknight.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        moonknight.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        moonknight.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        moonknight.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        moonknight.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        moonknight.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        moonknight.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        moonknight.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        moonknight.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        moonknight.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        moonknight.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        moonknight.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        moonknight.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        accion()
    elif personaje == 'Daredevil' or personaje == 'daredevil':
      personaje2 = input("Elige a otro superheroe: ")
      if personaje2 == 'Batman' or personaje2 == 'batman':
        daredevil.fight(batman)
      elif personaje2 == 'Green Arrow' or personaje2 =='green arrow':
        daredevil.fight(greenarrow)
      elif personaje2 == 'Mageneto' or personaje2 == 'magneto':
        daredevil.fight(magneto)
      elif personaje2== 'Storm' or personaje2 == 'storm':
        daredevil.fight(storm)
      elif personaje2 == 'Phoenix' or personaje2 == 'phoenix':
        daredevil.fight(phoenix)
      elif personaje2 == 'Wolverine' or personaje2 == 'wolverine':
        daredevil.fight(wolverine)
      elif personaje2 == 'Deadpool' or personaje2 == 'deadpool':
        daredevil.fight(deadpool)
      elif personaje2 == 'Superman' or personaje2 == 'superman':
        daredevil.fight(superman)
      elif personaje2 == 'Baby Groot' or personaje2 == 'baby groot':
        daredevil.fight(groot)
      elif personaje2 == 'Raven' or personaje2 == 'raven':
        daredevil.fight(raven)
      elif personaje2 == 'Doctor Strange' or personaje2 == 'doctor strange':
        daredevil.fight(doctorstrange)
      elif personaje2 == 'Scarlet Witch' or personaje2 == 'scarlet witch':
        daredevil.fight(scarletwitch)
      elif personaje2 == 'Homelander' or personaje2 == 'homelander':
        daredevil.fight(homelander)
      elif personaje2 == 'Spiderman' or personaje2 == 'spiderman':
        daredevil.fight(spiderman)
      elif personaje2 =='Flash' or personaje2 == 'flash':
        daredevil.fight(flash)
      elif personaje2 == 'Deep' or personaje2 == 'deep':
        daredevil.fight(deep)
      elif personaje2 == 'Black Widow' or personaje2 == 'black widow':
        daredevil.fight(blackwidow)
      elif personaje2 == 'Moon Knight' or personaje2 == 'moon knight':
        daredevil.fight(moonknight)
      elif personaje2 == 'Daredevil' or personaje2 == 'daredevil':
        daredevil.fight(daredevil)
      else:
        print("Prueba a introducir de nuevo al personaje")
        print("")
        accion()
    else:
      print("\nPrueba a introducir de nuevo al personaje\n")
      print("")
      accion2()

skip= str(input("SALTAR LA INTRODUCCIÓN (SI/NO): "))
if skip == "NO":
  accion()
elif skip == "SI":
  accion2()
else:
  print("ERROR")
    