import math
from typing import Match

pGreco = math.pi

def perimetroQuadrato():
    lato = int(input("Inserisci la dimensione del lato \n"))
    print("Il perimetro e' ",lato*4)
    
def circonferenzaCerchio():
    raggio = int(input("Inserisci il raggio del cechio \n"))
    print("Il raggio del cerchio e' ",2*pGreco*raggio)
    
def perimetroRettangolo():
    base = int(input("Inserisci la base del rettangolo \n"))
    altezza = int(input("Inserisci l'altezza del rettangolo \n"))
    print("Il perimetro del rettangolo e' ",base*2+altezza*2)
    
if __name__ == "__main__":
    sceltaPoligono = int(input("Premi 1 per il perimetro quadrato, 2 per la circonferenza del cerchio, 3 per il perimetro del rettangolo \n"))
    if(type(sceltaPoligono) == int):
        match sceltaPoligono:
            case 1:
                perimetroQuadrato()
            case 2:
                circonferenzaCerchio()
            case 3:
                perimetroRettangolo()
            case _:
                print("Invalid Input")
