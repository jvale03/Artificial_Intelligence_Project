import Order
import Route
import Vehicle
import Push_data


address1 = Order.Address("Arcozelo","Barcelos")
address2 = Order.Address("Martim","Barcelos")
address3 = Order.Address("Galegos","Barcelos")
address4 = Order.Address("Pousa","Barcelos")

order1 = Order.Order(1,address1,"21/10",2,4,15)
order2 = Order.Order(2,address2,"21/10",2,7,10)
order3 = Order.Order(3,address3,"21/10",1,1,7)
order4 = Order.Order(4,address4,"21/10",1,5,35)

order_list = []
order_list.append(order1)
order_list.append(order2)
order_list.append(order3)
order_list.append(order4)

bicileta = Vehicle.Bicycle()

route_barcelos = Route.Route("João",None,"Barcelos",order_list)
route_barcelos.set_vehicle()

order3.set_as_delivered()

order4.set_rating(4)
order2.set_rating(10)

route_barcelos.prices_update()


print(route_barcelos)
print("------------")
for order in order_list:
    print(order)
    print("---")



data = Push_data.Data(None,None)
map = data.get_map()
map.init_graph()
map.display_graph()