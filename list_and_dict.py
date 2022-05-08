#Programa para recorrer diccionarios dentro de listas 
#y listas dentro de diccionarios

def run():
    my_list =   [1, "Hello", True, 4.5]
    my_dict =   {"firstname": "Oscar", "Lastname": "Garcia"}

    super_list  =   [
        {"firstname": "Oscar", "Lastname": "Garcia"},
        {"firstname": "Miguel", "Lastname": "Torres"},
        {"firstname": "Pepe", "Lastname": "Rodelo"},
        {"firstname": "Susana", "Lastname": "Martinez"},
        {"firstname": "Jose", "Lastname": "Garcia"}
    ]

    super_dict  =   {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }
#Aplicamos un ciclo for para recorrer los dictionarios recordando 
#que necesitamos una llave y su valor (key and value) y para recorrer esto usamos
#metodo items
    for key, value in super_dict.items():
        print(key, "-", value)
        
    print("\n")
#Para recorrer las listas tenemos varias formas
#En esta primera forma recorreremos la lista con "i" e imprimimimos
#el valor de cada "i" en la posicion correspondiente cuando el
#ciclo for pasa por los valores
    for i in super_list:
        print(i["firstname"], "-", i["Lastname"])    
    print("\n")
#Aqui hay otra forma de hacerlo. Dos ciclos for, uno para la lista
#y otro para el diccionario. En este caso me imprime tambien las palabras
# "firstname" y "lastname"
    for i in super_list:
        for key, value in i.items():
            print(f'{key} - {value}')
    print("\n")
#Una tercera forma es la siguiente, aunque el formato de salida es mas
#riguroso y extenso
    for i in super_list:
        print(i.items())
            

if __name__== '__main__':
    run()