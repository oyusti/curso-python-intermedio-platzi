from multiprocessing.sharedctypes import Value
from random import randint
import os

os.system("clear")
def read_file():
    with open("./files/data.txt", "r", encoding = "utf-8") as f:#abrir el archivo data.txt (archivo donde estan los palabras)
        data_file = [(name.strip()) for name in f]# Limpio el archivo eliminando todos espacios en blanco y los anexo en una lista
        dict_data = {key: value for key, value in enumerate(data_file)}#creo un diccionario donde key sera elvalor enumerado de la funcion "enumerate"
        return dict_data
        
def del_accents(word):#Funcion que reemplaza las letras acentuadas y en mayusculaspor letras sin acento y en minusculas
    replacements = (("á", "a"),("é", "e"),("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word

def work_aleatory_word(data):#Funcion que extrae un valor del diccionario de forma aleatoria
    aleatory_word = del_accents(data.get(randint(0, len(data)+1)))#Obtengo un valor dentro del diccionario de forma aleatoria
    return aleatory_word

def work_line(guess_word):#Funcion que cambia las letras por guiones
    line_create = len(guess_word)* "-"
    return line_create

# def validate(character):
#     try:
#         if len(character) > 1:
#             print(character)
#             raise ValueError ("Ingresa un valor correcto")
#     except ValueError as ve:
#         print(ve)     
    

def compare(guess_word,line):
    while(guess_word != line):
        print("HANGMAN GAME\n")
        print(line)
        print("\n")
        print("Adivina la Palabra\n")
        user_char = input("Ingrese una letra: ")      
        if user_char in guess_word:
            line = list(line)
            for i, x in enumerate(guess_word):   
                if x == user_char:
                    line[i] = x
            line= "".join(line)
        os.system("clear")
        print("\n")
    print(f'Ganaste! Tu palabra era {line}')
    
def run():
    data = read_file()#funcion para leer el archivo con los datos, asignarlos a un diccionario y limpiar sus espacios en blanco
    guess_word = work_aleatory_word(data)#funcion que escoge una plabara de forma aleatoria
    line = work_line(guess_word)#funcion que cambia las letras por guiones
    compare(guess_word,line)#funcion que compara si las letras ingresadas, coinciden con la palabra adivinar

if __name__== '__main__':
    run()