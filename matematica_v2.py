#!/usr/bin/env python3
"""
Author:      Hans Saldias
Creador:    Viernes 07 de julio
Uso :          Practica de matematicas
motivo:      Practica de programacion
lenguaje:    python

"""
import os
from random import randint
from colorama import init, Fore, Style, Back
init()

class Ejercicios:
    
    def __init__ (self):
       self.n1 = 0
       self.n2 = 0
       self.buenos =0
       self.malos = 0
        
    def suma(self):
        print("""  
                       ################
                       ||    SUMAS   ||
                       ################
                       
                 para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            self.n2 = randint(0, 9)
            res = int(input(f"    ¿cuanto es {self.n1} + {self.n2} ?: "))
            if res == self.n1 + self.n2:
                self.buenos += 1 
                print(f"Intentos buenos {self.buenos}\n")   
                print("Correcto Sigue Asi !!!!\n")
                s.suma()
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}\n")
                print(f"la respiesta era: {self.n1+self.n2}\n")
                


    def resta(self):
        print("""  
                       ################
                       ||    RESTAS   ||
                       ################
                   
                   para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            self.n2 = randint(0, 9)
            res = int(input(f"    ¿cuanto es {self.n1} - {self.n2} ?: "))
            if res == self.n1 - self.n2:
                self.buenos += 1 
                print(f"Intentos buenos {self.buenos}")   
                print("Correcto Sigue Asi !!!!\n")
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}")
                print(f"la respiesta era: {self.n1-self.n2}\n")
               
              
    def division(self):
        print("""  
                       ################
                       ||    DIVISIONES   ||
                       ################
                   
                   para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            self.n2 = randint(0, 9)
            res = int(input(f"     ¿cuanto es {self.n1} ÷  {self.n2} ?: "))
            if res == self.n1 / self.n2:
                self.buenos += 1 
                print(f"Intentos buenos {self.buenos}")   
                print("Correcto Sigue Asi !!!!\n")
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}")
                print(f"la respiesta era: {self.n1/self.n2}\n")

                       
    def multiplicacion(self):
        print("""  
                       ######################
                       ||    MULTIPLICACIONES   ||
                       ######################
                       
                   para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            self.n2 = randint(0, 9)
            res = int(input(f"    ¿cuanto es {self.n1} x  {self.n2} ?: "))
            if res == self.n1 *  self.n2:
                self.buenos += 1 
                print(f"Intentos buenos {self.buenos}")   
                print("Correcto Sigue Asi !!!!\n")
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}")
                print(f"la respiesta era: {self.n1*self.n2}\n")
                                                              
                                                                  
    def exponentes(self):
        print("""  
                       ################
                       ||    EXPON3NTES   ||
                       ################
                       
                   para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            self.n2 = randint(0, 9)
            res = int(input(f"      ¿cuanto es {self.n1} elevado a  {self.n2} ?: "))
            if res == self.n1 ** self.n2:
                self.buenos += 1 
                print(f"Intentos buenos {self.buenos}")   
                print("Correcto Sigue Asi !!!!\n")
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}")
                print(f"la respiesta era: {self.n1**self.n2}\n")
                                                                                                            
                                                                                                                         
    def raiz(self):
        print("""  
                       ####################
                       ||    RAIZ CUADRADAS   ||
                       ####################
                       
                   para ir al menu responda 0
            \n\n""")
        while True:
            self.n1 = randint(0, 9)
            res = int(input(f"   ¿cual es la raiz cuadrada de {self.n1} ?: "))
            if res == self.n1**0.5:
                self.buenos += 1 
                print(f"\nIntentos buenos {self.buenos}")   
                print("Correcto Sigue Asi !!!!\n")
            elif res == 0:
                os.system("clear")
                s.menu()
            else:
                print("Has perdido sigue intentando !!  \n")
                self.malos += 1
                print(f"Intentos malos {self.malos}")
                print(f"la respuesta era: {round(self.n1**0.5)}\n")

                  
                
    def menu(self):
                pd = input("""
                SOLO INGRESO PERSONAL AUTORIZADO 
                
                CURSO (3 Y 4 A) LICEO POLIVALENTE DE MOLINA
                
                INGRESE CONTRASEÑA:  """)
                if pd == "Luis Cid":
                    while True:
                        try:
                            print(Style.BRIGHT+Fore.RED+"""
                        ##########################################
                        || PRACTICA DE EJERCICIOS DE MATEMATICAS ||
                        ############################################
                 
                        creador: Hans Saldias
                
                        Para Profesor: Luis Cid
                
                
                        [ 1 ]         >            SUMAS         <
                
                
                        [ 2 ]         >             RESTAS        <
                
                
                        [ 3 ]        >          DIVISIONES     <
                
                
                        [ 4 ]        >        MULTIPLICACIONES    <
                
                
                        [ 5 ]        >        EXPONENTES     < 
               
               
               
                        [ 6 ]        >        RAIZ CUADRADA  <
                
                
                        [ 0 ]        >                SALIR            <
                
                
                                """)
                
                            op = int(input("INGRESE OPCION:  "))
                            if op == 1:
                                os.system("clear")
                                s.suma()
                            elif op == 2:
                                os.system("clear")
                                s.resta()
                            elif op == 3:
                                os.system("clear")
                                s.division()
                            elif op == 4:
                                os.system("clear")
                                s.multiplicacion()
                            elif op == 5:
                                os.system("clear")
                                s.exponentes()
                            elif op == 6:
                                os.system("clear")
                                s.raiz()
                            elif op == 0:
                                os.system("clear")
                                print("Gracias por usar mi script Hans Saldias")
                                break
                        except ValueError:
                            print("Ingreso incorrecto, Intenta nuevamente")
                            os.system("clear")
                else:
                    print("""
                    COMUNIQUESE CON EL CREADOR DEL SCRIPT 
                    
                    EN EL LICEO POLIVALENTE DE MOLINA 
                    
                    PREGUNTAR POR: HANS SALDIAS
                    
                    """)                
                
s = Ejercicios()                
s.menu()                                     
                                                                                                                                               