import os


import os

def easy():
    pass

def hard():
    pass

def main():
    
    opcion=""
    while opcion!="3":
        print("1) Facil")
        print("2) Dificil")
        print("3) Salir del juego")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            easy()
        elif opcion =="2":
            hard()
        elif opcion =="3":
            print("Saliendo...")
            opcion=="3"
        else:
            print("Opcion incorrecta")
        os.system("cls")




def run():
    main()


if __name__=="__main__":
    run()