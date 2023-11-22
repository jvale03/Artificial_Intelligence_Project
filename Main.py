import Push_data


if __name__ == "__main__":

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

    print(data)