import Push_data


if __name__ == "__main__":

    # criar metodo que irá guardar os dados
    data = Push_data.Data()

    # dar upload dos dados a partir dos ficheiros
    try:
        # data.init_graph()
        # data.display_graph()
        data.init_drivers()
        data.init_orders()
        print("\033[32mUpload realizado com sucesso!\033[m")
    except Exception as e:
        print(f"\033[31mErro no Upload: {e}\033[m")
    
    print(data)


# import Order
# import Route
# import Vehicle
# import Driver

# driver = Driver.Driver(1,"joao")

# order1 = Order.Order(1,"Arcozelo","Barcelos","21/10",2,1,15)
# order2 = Order.Order(2,"Martim","Barcelos","21/10",1,1,10)
# order3 = Order.Order(3,"Galegos","Barcelos","21/10",1,1,7)
# order4 = Order.Order(4,"Pousa","Barcelos","21/10",1,1,35)

# order_list = []
# order_list.append(order1)
# order_list.append(order2)
# order_list.append(order3)
# order_list.append(order4)

# bicileta = Vehicle.Bicycle()

# route_barcelos = Route.Route(1,driver,None,"Barcelos",order_list)
# route_barcelos.set_vehicle()

# order3.set_as_delivered()

# order4.set_rating(4)
# order2.set_rating(10)

# route_barcelos.prices_update()


# print(route_barcelos)
# print("------------")
# for order in order_list:
#     print(order)
#     print("---")

