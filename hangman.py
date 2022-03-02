import os
import random

#read the file and return all the words in the document "data"
def getFile():
    with open("files/datos.txt", "r", encoding="utf-8") as file:
        level1=[word.rstrip("\n") for word in file]
        return level1
        
def game(level):
    os.system("cls")
    picture=["-----------","-         |","-         O","-        / ","-        /| ","-        /|\ ","-        /  ","-        / \ ","-","_________________"]
    mistakes=0
    wins=0
    wordsrandoms=[]
    wordsWritten=[]
    badWords=[]
    word=""
    num=-1
    while num==-1:
        num=random.randint(0,len(level))
        if(wordsrandoms.count(num)==0):
            wordsrandoms.append(num)
        else:
            num=-1
    
    
    word=level[num]
    print("_"*len(word))
    control=0
    win=False
    while control!=1:
        
        letter=input("Ingrese una letra:")
        wordPrint=""
        
        try:
            if not(letter.isalpha()) and len(letter)>1:
                raise  ValueError("Ingrese un valor correcto")
            
            letter=letter.lower()
            wordsWritten.append(letter)
            if word.find(letter)==-1:
                badWords.append(letter)
                mistakes=mistakes+1
                if mistakes==6:
                    control=1
            for x in word:
                if wordsWritten.count(x)==0:
                    wordPrint=wordPrint+"-"
                else:
                    wordPrint=wordPrint+x
            
            if wordPrint==word:
                control=1
                win=True
                wins=wins+1
            

        except ValueError as ve:
            print(ve)
        os.system("cls")
        print(wordPrint)
        print("Cantidad de errores: "+ str(mistakes))
        print("Palabras erroneas:"+str(badWords))

    if win:
        print("Ganaste!")
    if mistakes==6:
        print("Perdiste")
        print("La palabra correcta era: "+ word)
    input("Continuar")
    





def main(level1,level2):
    
    opcion=""
    while opcion!="3":
        print("1) Facil")
        print("2) Dificil")
        print("3) Salir del juego")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            game(level1)
        elif opcion =="2":
            game(level2)
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
    main(level1,level2)


if __name__=="__main__":
    run()