import Order
import Route
import Driver
import Vehicle

driver = Driver.Driver("joao",None)

address1 = Order.Address("Arcozelo","Barcelos")
address2 = Order.Address("Martim","Barcelos")
address3 = Order.Address("Galegos","Barcelos")
address4 = Order.Address("Pousa","Barcelos")

order1 = Order.Order(1,address1,"21/10",2,10,15)
order2 = Order.Order(2,address2,"21/10",7,10,10)
order3 = Order.Order(3,address3,"21/10",4,10,7)
order4 = Order.Order(4,address4,"21/10",1,10,35)

order_list = []
order_list.append(order1)
order_list.append(order2)
order_list.append(order3)
order_list.append(order4)

bicileta = Vehicle.Bicycle()

route_barcelos = Route.Route(driver,bicileta,"Barcelos",order_list)
route_barcelos.set_vehicle()


print(route_barcelos)
