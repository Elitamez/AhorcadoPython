import random
import os
import sys
import pyfiglet
import time
import random
import string

def clear():
    if os.name == "posix":
        os.system ("clear")
    else:
        os.system ("cls")

def read_archivo():
    with open("./ahorcado/ahorcado.txt", "r", encoding="utf-8") as f:
        palabras=[palabra.replace("\n", "") for palabra in f]
    return palabras

def quitar_acentos(palabras):
    letras={
        "á" : "a",
        "é" : "e",
        "í" : "i",
        "ó" : "o",
        "ú" : "u"
    }
    
    new_words=[]
    for palabra in palabras:
        for letra in letras:
            if letra in palabra:
                palabra=palabra.replace(letra, letras.get(letra))
        new_words.append(palabra)
    
    #convertimos a mayúsculas
    for i in range(len(new_words)):
        new_words[i]=new_words[i].upper()
    #print(new_words)
    return new_words

def victoria(word):
    clear()
    print(pyfiglet.figlet_format("You Win", font="doh"))
    print("la palabra era:", word)
    time.sleep(2)
    sys.exit()

def perder(word):
    clear()
    print(pyfiglet.figlet_format("You Lose", font="doh"))
    print("La palabra era:", word)
    time.sleep(2)

def juego(word, all_letters, list_word):
    vidas=7
    print(pyfiglet.figlet_format("HangMan", font="doh"))
    print("No presiones nada aún")
    time.sleep(2)

    incognita=["_" for i in range(len(word))]
    
    while vidas>0:
        clear()
        print("vidas disponibles:", vidas,"\n")
        print("\t", end="")
        for i in incognita:
            print(i, end="")
        print("\n")
        try:
            letra=input("Ingrese la letra: ")
            if letra=="":
                raise ValueError("Tienes que ingresar una letra")
            elif letra in all_letters:
                letra=letra.upper()
                if letra in word:
                    for i in range(len(word)):
                        if letra==word[i]:
                            incognita[i]=letra
                    if list_word==incognita:
                        victoria(word)
                else:
                    vidas-=1
            else:
                raise ValueError("Tienes que ingresar una letra")
        except ValueError as ve:
            print(ve)
            time.sleep(1)
    perder(word)

def run():
    palabras=read_archivo()
    new_words=quitar_acentos(palabras)
    numero=random.randint(0, len(new_words)-1)
    
    word=new_words[numero]
    all_letters=string.ascii_letters+"ñ"+"Ñ"
    list_word=list(word)

    juego(word, all_letters, list_word)


if __name__=="__main__":
    run()