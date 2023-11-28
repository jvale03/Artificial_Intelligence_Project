import Push_data
import Search_algorithms
import Data.Data_generator as Generator
import Aux_functions


import Order
import Route
import Vehicle
import Driver


driver = Driver.Driver(1,"joao")

order1 = Order.Order(1,"Lijo","Norte",1,2,1,15)
order2 = Order.Order(2,"Roriz","Norte",0,1,1,10)
order3 = Order.Order(3,"Carapecos","Norte",3,1,1,7)
order4 = Order.Order(4,"Tamel","Norte",0,1,1,35)

order_list = []
order_list.append(order1)
order_list.append(order2)
order_list.append(order3)
order_list.append(order4)

bicileta = Vehicle.Bicycle()

route_barcelos = Route.Route(1,driver,None,"Barcelos",order_list)
route_barcelos.set_vehicle()

order3.set_as_delivered()

order4.set_rating(4)
order2.set_rating(10)

route_barcelos.prices_update()


def menu(data,option):
    if option == 1:
        data.display_graph()
    elif option == 2:
        mapa = data.get_map()
        #freguesia = input("Insere aqui a freguesia de destino: ")  # para depois tornar iterativo
        
        route = []
        Aux_functions.sort_by_deadline(route_barcelos.get_sorted_order_list()) # organizar por deadline
        for order in route_barcelos.get_sorted_order_list():
            route.append(order.get_address().get_parish())


        try:
            path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',route)
            print(path)
        except Exception:
            print("\033[31mFreguesia inexistente!\033[m")

    elif option == 3:
        print(data)

    elif option == 4:
        Generator.generator()
    
    elif option != 5:
        print("\033[31mOpção inválida!\033[m")


if __name__ == "__main__":

    
    option = input("\033[36mDar Upload dos dados (1)\nSair\n\033[m")
    if option.isdigit():
        option = int(option)

    if option == 1:
        # criar metodo que irá guardar os dados
        data = Push_data.Data()

        # dar upload dos dados a partir dos ficheiros
        try:
            data.init_graph()
            data.init_drivers()
            data.init_orders()
            print("\033[32mUpload realizado com sucesso!\033[m")
        except Exception as e:
            print(f"\033[31mErro no Upload: {e}\033[m")
        
        
        option = ''
        while option != 5:
            option = input("\033[36mMostrar Mapa(1)\nFazer caminho(2)\nMostrar dados(3)\nGerar Novos Dados(4)\nSair(5)\n\033[m")
            if option.isdigit():
                option = int(option)
            menu(data,option)
        
        print("\033[31mSair...\033[m")

    else:
        print("\033[31mSair...\033[m")










