#Programa que calcula los divisores de un numero e imprime mensajes de error cuando
#se inserta un valor que no sea un numero asi como tambien, un valor cuando 
#se ingresa un numero negativo
def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i==0]
    return divisors
#Con assert confirma la expresion y despues de la coma va lo que queremos que haga siempre que la expresion sea False
def run():
    print("Programa que calcula los divisores de un numero")
    value_entry = input("Ingrese un numero: ")
    assert value_entry.isnumeric(), "Debes ingresar un numero positivo"
    print(divisors(int(value_entry)))
            
    
if __name__== '__main__':
    run()