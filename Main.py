import Push_data
import Data.Data_generator as Generator
import time
import Aux_functions


def menu(data,option):
    if option == 1:
        data.display_graph()

    elif option == 2:
        mapa = data.get_map()
        drivers_list = []
        driver = input('\033[33mInsira o id de um estafeta: \033[m')
        while driver.isdigit():            
            if int(driver) in drivers_list or int(driver) > len(data.get_drivers()):
                print('\033[31mEstafeta inválido!\033[m')
            else:
                drivers_list.append(int(driver))
            driver = input('\033[33mInsira o id de um estafeta: \033[m')

        print('\033[33mA realizar rotas...\033[m\n')
        time.sleep(0.5)

        routes_list = data.realize_routes(drivers_list)
        for route in routes_list:
            print('\033[31m--------\033[m')
            
            print(f'\033[1mRoute {route.get_id()}, {route.get_area()}\033[m')
            print(f'{route.str_orders_parish()}')
            
            path = Aux_functions.priority_astar(mapa,route)
            print(f'\033[1mPercurso Prioritário:\033[m {path[0]}\n\033[1mDistancia:\033[m {route.get_distance()}km, {Aux_functions.convert_to_hours_str(round(route.get_distance()/route.get_vehicle().get_average_speed(),2))}\n\033[1mVeículo:\033[m {route.get_vehicle()}')
            print(f'{path[1]}\n')

            path = Aux_functions.eco_astar(mapa,route)
            print(f'\033[1mPercurso Eco:\033[m {path[0]}\n\033[1mDistancia:\033[m {route.get_distance()}km, {Aux_functions.convert_to_hours_str(round(route.get_distance()/route.get_vehicle().get_average_speed(),2))}\n\033[1mVeículo:\033[m {route.get_vehicle()}')
            print(f'{path[1]}\n')
        
            data.delete_route(route)


    elif option == 3:
        option = ''
        option = input('\033[33mEstafetas(1)\nEncomendas(2)\nRotas(3)\nSair\n\033[m')
        if option.isdigit():
            option = int(option)
        if option == 1:
            for driver in data.get_drivers():
                print(driver)
                print('\n')
        elif option == 2:
            for area in data.get_orders():
                for order in data.get_orders()[area]:
                    print(order)
                    print('\n')
        elif option == 3:
            for route in data.get_routes():
                print(route)
                print('\n')

    elif option == 4:
        print("\033[32mDados limpos\033[m")
        Generator.generator()
        time.sleep(0.3)
        print("\033[32mReinicie o programa!\033[m")
    
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
            data.init_routes()
            print("\033[32mUpload realizado com sucesso!\033[m")
        except Exception as e:
            print(f"\033[31mErro no Upload: {e}\033[m")
        
        
        option = ''
        while option != 5:
            option = input("\033[36mMostrar Mapa(1)\nFazer entregas(2)\nMostrar dados(3)\nGerar Novos Dados(4)\nSair(5)\n\033[m")
            if option.isdigit():
                option = int(option)
            menu(data,option)
        
        print("\033[31mSair...\033[m")

    else:
        print("\033[31mSair...\033[m")







