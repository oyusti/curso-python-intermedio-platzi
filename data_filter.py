DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #*************************************************************************************************
    #Vamos a filtrar todos los trabajadores que saben de python.Lo hacemos con una list comprehension
    print("-----------------------------------------")
    print("TRABAJADORES QUE SABEN PYTHON")
    print("Utilizando List Comprehension")
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print(all_python_devs)#Con este print tendremos en pantalla los resultados pero en forma de lista
    #Con este "for" veremos en pantalla los resultados sin tener forma de lista
    for worker in all_python_devs:
        print(worker)
    print("\n")

    #Ahora lo mismo pero con HOF (High Order Function)
    print("Utilizando HOF")
    all_python_devs_hof = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_hof = list(map(lambda worker: worker["name"], all_python_devs_hof))
    for worker in all_python_devs_hof:
        print(worker)
    print("---------------------------------------\n")
    #**************************************************************************************************
    #Vamos a filtrar todos los trabajadores que trabajan en Platzi.Lo hacemos con una list comprehension
    print("TRABAJADORES QUE TRABAJAN EN PLATZI")
    print("Utilizando List Comprehension")
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print(all_platzi_workers)#Con este print tendremos en pantalla los resultados pero en forma de lista
    #Con este for veremos en pantalla los resultados sin tener forma de lista
    for worker in all_platzi_workers:
        print(worker)
    print("\n")

    #Ahora lo mismo pero con HOF (High Order Function)
    print("Utilizando HOF")
    all_platzi_workers_hof= list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers_hof = list(map(lambda worker: worker["name"], all_platzi_workers_hof))
    for worker in all_platzi_workers_hof:
        print(worker)
    print("---------------------------------------\n")
    #***************************************************************************************************
    #Ahora queremos saber cuantos devs son adultos (>18), pero lo haremos con la HOF "Filter" and "Map"
    print("TRABAJADORES ADULTOS")
    print("Utilizando HOF")
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    
    for worker in adults:
        print(worker)
    print("\n")

    #Ahora haremos lo mismo pero con list_comprehension
    print("Utilizando List Comprehension")
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    print(adults)#Con este print tendremos en pantalla los resultados pero en forma de lista
    #Con este "for" veremos en pantalla los resultados sin tener forma de lista
    for worker in adults:
        print(worker)
    print("---------------------------------------\n")
    #*****************************************************************************************************
    #Ahora crearemos un item en los diccionarios donde evalue si la persona
    #tiene mas de 50 anos de edad. Esto lo haremos con la HOF "Map"
    print("ASIGNAMOS UN NUEVO ITEM A LOS DICCIONARIOS DONDE SI TIENE MAS DE 50 ANOS NOS DICE SI ES TRUE O FALSE")
    print("Utilizando HOF")
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 50}, DATA))
    for worker in old_people:
        print(worker)
    print("\n")

if __name__== '__main__':
    run()