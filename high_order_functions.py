from functools import reduce

def run():
#Codigo para filtrar y crear una lista con los  numeros impares
    my_list1 = [1, 4, 5, 6, 9, 13, 19, 21]
    filt = [i for i in my_list1 if i%2 !=0]
    print(filt)
    print("\n")

#Hacemos lo mismo que arriba pero con la funcion de orden superior "Filter"
#Ademas usamos Lambda para el recorrido de los datos
#"Filter" recibe dos parametros La funcion anonima (Lambda) y el iterable    
#Retorna un iterador y con la funcion list creamos la lista
    odd = list(filter(lambda x: x%2 !=0, my_list1))
    print (odd)
    print("\n")

#Ahora usaremos una lista y crearemos otra con esos datos pero elevados al cuadrado
    my_list2 = [1, 2, 3, 4, 5]
    square_list = [i**2 for i in my_list2]
    print (square_list)
    print("\n")

#Haremos lo mismo pero con la funcion de orden superior "Map" 
    square_list2 = list(map(lambda x: x**2, my_list2))
    print(square_list2)
    print("\n")

#Ahora queremos multiplicar todos los elementos de una lista con los  numeros
    my_list3 = [2, 2, 2, 2, 2]
    multiplica = 1
    for i in my_list3:
        multiplica = multiplica * i
    print(multiplica)
    print("\n")    
#Ahora haremos todo esto con la funcion de orden superior "Reduce"
    multiplica1 = reduce(lambda a, b: a * b, my_list3)
    print(multiplica1)

if __name__== '__main__':
    run()