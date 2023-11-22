import random

# este ficheiro serve apenas para gerar data para ficheiros à parte


names = ["Joao","Vitor","Luis","Filipe","Rui","Tomas","Barreto","Oliveira","Ramos","Hugo","Duarte","Carlos","Gilberto","Manuel","Alberto","Lopes","Mariana","Maria","Beatriz","Ana","Jose","Renata"]
zonas = {"Norte": ["Silva","Lijo","Carapecos","Roriz","Tamel","Alvito"],
        "Sul": ["Barcelinhos","Rio Covo","Gamil","Remelhe","Pereira","Alvelos","Gilmonde"],
        "Este": ["Arcozelo","Galegos","Oliveira","Manhente","Varzea","Airo"],
        "Oeste": ["Abade de Neiva","Creixomil","Parelhal","Fornelos","Vila Boa","Vila Cova"]}

def driver_generator(number):
    file = open("Drivers.txt",'w')

    for x in range(1,number+1):
        file.write(f"{x};{random.choice(names)}\n")

    file.close()

def order_generator(number):
    file = open("Orders.txt",'w')

    for x in range(1,number+1):
        zona = random.choice(list(zonas.keys()))
        freguesia = random.choice(zonas[zona])
        deadline = " "
        weight = round(random.uniform(0.1,25),1)
        volume = round(random.uniform(0.001,0.5),3)
        price = round(random.uniform(0.99,100),2)
        file.write(f'{x};{freguesia};{zona};{deadline};{weight};{volume};{price}\n')

    file.close()

if __name__ == "__main__":
    number_driver = int(input("Insere o numero de estafetas: "))
    number_orders = int(input("Insere o numero de encomendas: "))
    driver_generator(number_driver)
    order_generator(number_orders)
    print("Dados Gerados!")
