


from random import randint
import os

os.system("clear")
def read_file():
    with open("./files/data.txt", "r", encoding = "utf-8") as f:
        data_file = [(name.strip()) for name in f]
        data_file = [(name.replace("á", "a") and name.replace("é", "e") and name.replace("í", "i") and name.replace("ó", "o") and name.replace("ú", "u")) for name in data_file]
        dict_data = {key: value for key, value in enumerate(data_file)}
        #print(dict_data)
        return dict_data
        

def run():
    data = read_file()
    print("\nBienvenido al juego del horcado\n")
    aleatory_word = data.get(randint(0, len(data)))
    guess_word = len(aleatory_word)* " - "   
    print("Adivina la Palabra\n")
    print(guess_word)
    #while aleatory_word != guess_word:
        #caracter = input("Inserte una letra")
            #if caracter in aleatory_word
    
    # print(size_word)

    print(aleatory_word)


if __name__== '__main__':
    run()