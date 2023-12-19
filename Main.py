import Push_data
import Data.Data_generator as Generator
import time
import Aux_functions
import threading

def get_estafetas():
    drivers_list = []
    driver = input('Insira o id de um estafeta: ')
    while driver.isdigit():            
        if int(driver) in drivers_list or int(driver) > len(data.get_drivers()):
            print('\033[31mEstafeta inválido!\033[m')
        else:
            drivers_list.append(int(driver))
        driver = input('Insira o id de um estafeta: ')
    return drivers_list

def menu(data,option):
    if option == 1:
        data.display_graph()   
        

    elif option == 2:
        option = ''
        option = input('Remover Caminho(1)\nAdicionar Caminho(2)\nSair\n')
        if option.isdigit():
            option = int(option)
        if option == 1:
            node1 = input("Insere freguesia: ")
            node2 = input("Insere freguesia: ")
            data.remove_edge(node1,node2)
        elif option == 2:
            node1 = input("Insere freguesia: ")
            node2 = input("Insere freguesia: ")
            data.add_edge(node1,node2)
        

    elif option == 3:
        mapa = data.get_map()

        drivers_list = get_estafetas()

        print('\033[32mA realizar rotas...\033[m\n')
        time.sleep(0.5)

        routes_list = data.realize_routes(drivers_list)

        for route in routes_list:
            print('\033[31m--------\033[m')

            print(f'\033[1;33mRota {route.get_id()}, {route.get_area()}\033[m')
            print(f'{route.str_orders_parish()}')
            
            path = Aux_functions.priority(mapa,route)
            print(f'\033[1;33mPercurso Prioritário:\033[m {path[0]}\n\033[1;33mDistancia:\033[m {route.get_distance()}km, {Aux_functions.convert_to_hours_str(round(route.get_distance()/route.get_vehicle().get_average_speed(),2))}\n\033[1;33mVeículo:\033[m {route.get_vehicle()}, {route.get_vehicle().get_average_speed()}km/h')
            print(f'\033[1;33mAStar: \033[m{path[1]} -> \033[1;4m{path[4][0]}s\033[m')
            print(f'\033[1;33mBFS: \033[m{path[2]} -> \033[1;4m{path[4][1]}s\033[m')
            print(f'\033[1;33mDFS: \033[m{path[3]} -> \033[1;4m{path[4][2]}s\033[m\n')

            path = Aux_functions.eco(mapa,route)
            print(f'\033[1;33mPercurso Eco:\033[m {path[0]}\n\033[1;33mDistancia:\033[m {route.get_distance()}km, {Aux_functions.convert_to_hours_str(round(route.get_distance()/route.get_vehicle().get_average_speed(),2))}\n\033[1;33mVeículo:\033[m {route.get_vehicle()}, {route.get_vehicle().get_average_speed()}km/h')
            print(f'\033[1;33mAStar: \033[m{path[1]} -> \033[1;4m{path[4][0]}s\033[m')
            print(f'\033[1;33mBFS: \033[m{path[2]} -> \033[1;4m{path[4][1]}s\033[m')
            print(f'\033[1;33mDFS: \033[m{path[3]} -> \033[1;4m{path[4][2]}s\033[m\n')

        
            data.delete_route(route)
        
        threads = []

        option = input('Realizar rota prioritária(1)\nRealizar rota eco(2)\n')
        while option != '1' or option != '2':
            if option == '1':
                for route in routes_list:
                    new_thread = threading.Thread(target=Aux_functions.run_route, args=(mapa,route,'Priority'))
                    threads.append(new_thread)
                    new_thread.start()  

                break

            elif option == '2':
                for route in routes_list:
                    new_thread = threading.Thread(target=Aux_functions.run_route, args=(mapa,route,'Eco'))
                    new_thread.start()   

                break
            option = input('Realizar rota prioritária(1)\nRealizar rota eco(2)\n')    


    elif option == 4:
        option = ''
        option = input('Estafetas(1)\nEncomendas(2)\nRotas(3)\nSair\n')
        if option.isdigit():
            option = int(option)
        if option == 1:
            for driver in data.get_drivers():
                print(driver)
                print('\n')
        elif option == 2:
            orders = data.sorted_orders()
            for order in orders:
                print(order)
                print('\n')
        elif option == 3:
            for route in data.get_routes():
                print(route)
                print('\n')

    elif option == 5:
        print("\033[32mDados limpos\033[m")
        Generator.generator()
        time.sleep(0.3)
        data.clear()
        data.init_graph()
        data.init_drivers()
        data.init_orders()
        data.init_routes()
    
    elif option != 6:
        print("\033[31mOpção inválida!\033[m")



if __name__ == "__main__":    

    # criar metodo que irá guardar os dados
    data = Push_data.Data()

    # dar upload dos dados a partir dos ficheiros
    try:
        data.init_graph()
        data.init_drivers()
        data.init_orders()
        data.init_routes()
        print("\033[32mUpload realizado com sucesso!\033[m")
    except Exception as e:
        print(f"\033[31mErro no Upload: {e}\033[m")

    Aux_functions.update_heuristic(data.get_map(),"Centro de Entregas")

    if Aux_functions.nodes_test(data) != False:
        print("\033[32mSegundo o algoritmo BFS, o 'Centro de Entregas' tem acesso a todas as freguesias!\033[m")
        option = ''

        while option != 6:
            option = input("\033[36mMostrar Mapa(1)\nAlterar Mapa(2)\nFazer entregas(3)\nMostrar dados(4)\nGerar Novos Dados(5)\nSair(6)\n\033[m")
            if option.isdigit():
                option = int(option)
            menu(data,option)
        
        print("\033[31mSair...\033[m")

    else:
        print(f"\033[31mFreguesias sem acesso!\033[m")
        







