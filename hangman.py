import os


#global variables
level1=[]
level2=[]

#read the file and return all the words in the document "data"
def getFile():
    with open("files/datos.txt", "r", encoding="utf-8") as file:
        level1=[word.rstrip("\n") for word in file]
        return level1
        

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
    #get the information and choose if a word is level 1 or level 2
    information=getFile()
    level1=list(filter(lambda word: len(word)<=5,information))
    level2=list(filter(lambda word: len(word)>5, information))
    #start the game
    main()


if __name__=="__main__":
    run()