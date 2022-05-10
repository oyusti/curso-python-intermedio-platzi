
#Programa que calcula los divisores de un numero e imprime mensajes de error cuando
#se inserta un valor que no sea un numero asi como tambien, un valor cuando 
#se ingresa un numero negativo
def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i==0]
    return divisors

#Es importante saber que pueden existir varios "except" por un solo "Try". En este caso usaremos dos "except"
def run():
    try:
        print("Programa que calcula los divisores de un numero")
        value_entry = int(input("Ingrese un numero: "))
        if value_entry <= 0:#Condicion si insertan un numero negativo
            raise Exception("Solo debes ingresar numeros positivos")#Error cuando existe un numero negativo
    except ValueError:#Error cuando se inserta algo queno sea una letra
        print("Debes ingresar un numero")
    except Exception as ve:#Error cuando se da la condicion de insertar un numero negativo
        print(ve)  
    else:        
        print(divisors(value_entry))

    

if __name__== '__main__':
    run()