import Push_data
import Search_algorithms
import Data.Data_generator as Generator
import Aux_functions


def exemplo_de_viagem_respeitar_deadlines():
    mapa = data.get_map()

    # isto é so para um mero exemplo para testes de rotas criadas manualmente
    orders = data.get_orders()
    order_north = orders['Norte']
    route = []
    for x in range(4):
        print(order_north[x])
        print('\n')
        route.append(order_north[x])
    
    # organizar rota
    route = Aux_functions.sort_by_deadline(route) 
    # transformar encomendas numa lista onde apenas tem as freguesias por ordem de passagem das mesmas
    list = []
    for order in route:
        list.append(order.get_address().get_parish())  


    try:
        path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',list)
        print(path)
    except Exception:
        print("\033[31mFreguesia inexistente!\033[m")




def menu(data,option):
    if option == 1:
        data.display_graph()

    elif option == 2:
        mapa = data.get_map()

        # isto é so para um mero exemplo para testes de rotas criadas manualmente
        orders = data.get_orders()
        order_north = orders['Norte']
        route = []
        for x in range(4):
            print(order_north[x])
            print('\n')
            route.append(order_north[x])
        
        # organizar rota
        route = Aux_functions.sort_by_deadline(route) 
        # transformar encomendas numa lista onde apenas tem as freguesias por ordem de passagem das mesmas
        list = []
        for order in route:
            list.append(order.get_address().get_parish())  


        try:
            path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',list)
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










