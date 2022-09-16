import random


class Cuestionador:

    def __init__(self):
        
        self.questions=[

            "¿Qué es el ALMICANTARAT?",
            "¿Donde se encuentra el zenit?",
            "¿Cuantos ordenes existen en la taxonomia de suelos?"
        ]

        self.answers=[
            "Circulo imaginario en esfera celeste",
            "90 gardos respecto a el horizonte" ,
            "12"
        ]
    def jugar(self):
        #Generar un numero aleatorio entre 0 y n-1 siendo n 
        # el tamaño de la lsita de preguntas
        n=len(self.questions)
        number=random.randint(0, n-1)
        print(self.questions[number])

        #Socilitar la respuesta al usuario
        respuesta=input("cual es tu respuesta mi perrito?")

        #Verificar si la respuesta es correcta

        if respuesta== self.answers[number]:
            print ("Eres genial bebé!!")
        else:
            print ("Deje de pensar que sus papas lo van a mantener")