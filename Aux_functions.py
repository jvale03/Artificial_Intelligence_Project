
# esta função vai organizar as encomendas por deadline e ao mesmo tempo por freguesia
# isto é, dá prioridade ao prazo, mas se houver mais do que uma encomenda nessa cidade, 
# mesmo que o seu prazo seja imenso, vai entregar de modo a ser economico
def sort_by_deadline(list):
    # Ordenar encomendas por data limite
    list.sort(key=lambda order: order.deadline)

    # Criar dicionário para armazenar encomendas por destino
    order_by_dest = {}

    # Agrupar encomendas por destino
    for order in list:
        parish = order.get_address().get_parish()
        if parish not in order_by_dest:
            order_by_dest[parish] = []
        order_by_dest[parish].append(order)

    list.clear()

    for parish in order_by_dest:
        for order in order_by_dest[parish]:
            list.append(order)

    return list

def line_parser(line):
    return line.split(";")