import Push_data
import SearchAlgorithms
import Data.Data_generator as Generator

def menu(data,option):
    if option == 1:
        data.display_graph()
    elif option == 2:
        freguesia = input("Insere aqui a freguesia de destino: ")
        mapa = data.get_map()
        try:
            path = SearchAlgorithms.AStarSearch(mapa,'Centro de Entregas',[freguesia,'Airo','Manhente','Centro de Entregas'])
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
        
        while option != 5:
            option = int(input("\033[36mMostrar Mapa(1)\nFazer caminho(2)\nMostrar dados(3)\nGerar Novos Dados(4)\nSair(5)\n\033[m"))
            menu(data,option)
        
        print("\033[31mSair...\033[m")

    else:
        print("\033[31mSair...\033[m")






