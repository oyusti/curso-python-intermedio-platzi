#programa que imprime una lista con los numeros divisibles entre 4, 6 y 9  con una list comprehension
def run():
    square = [i for i in range (1, 10000) if (i%4==0) and (i%6==0) and (i%9==0)]
    print(square)

if __name__== '__main__':
    run()


