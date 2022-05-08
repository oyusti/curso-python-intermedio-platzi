
#Programa que muestra en una lista los cuadrados de los primeros
#100 numeros que no sean divisible entre 3
def run():
    square = []
    for i in range(1, 101):
        if i % 3 != 0:#Condicion de que no sean divisibles entre 3
            square.append(i**2)#Agrego los valores a la lista
        else:
            continue    
    print(square)           
    print("\n")
    #Otra forma mas facil de hacerlo es con un list_comprehension.
    #Su solucion seria la siguiente
    square1 = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(square1)

if __name__== '__main__':
    run()




