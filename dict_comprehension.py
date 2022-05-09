def run():
    dict_cubo = {}
#Agregar datos al diccionario donde la llave son numeros naturales hasta 100 y el valor es dicho numero
#elevado al cubo
    # for i in range(1,101):
    #     dict_cubo[i] = i ** 3
    # print(dict_cubo)     


#Agregar datos a un diccionario donde la llave sean los 100 primeros numeros naturales y el valor sean 
#simplemente los numeros que no sean divisible por 3 elevados al cubo

    # dict_not_divi_three = {}

    # for j in range(1,101):
    #     if j % 3 != 0:
    #         dict_not_divi_three[j] = j ** 3
    # print(dict_not_divi_three)      

#Vamos hacer lo mismo pero con un dictionario comprehension
      
# dict_not_divi_three = {i:i**3 for i in range(1, 101) if i%3!=0}
# print(dict_not_divi_three)

#Ahora se va hacer lo mismo pero guardandose como valores solo las raices cuadradras de los numeros
dict_square = {i: round(i** 0.5, 3) for i in range(1, 100)}#con el round estbalezco solo 3 decimales
print(dict_square)


if __name__== '__main__':
    run()