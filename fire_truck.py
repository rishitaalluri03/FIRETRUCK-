# Program to find the all possible routes from firestation to fire
# route of the graph from the given streets
# case 1 when street 6 is closest to the fire
graph1 = {
    1: [2, 3],
    2: [3, 4],
    3: [4, 5],
    4: [6],
    5: [6]
}
graph2 = {
    2: [3, 5],
    3: [2, 4],
    4: [3, 6],
    5: [1, 2, 7],
    6: [1, 4, 9],
    7: [8, 5],
    8: [7,9,1],
    9: [8, 6]
}

def find_all_routes(graph1, graph2, start, end, route=[]):
    route = route + [start]
    if start == end:
        return [route]
    routes = []
    for street in graph1[start]:
        if street not in route:
            newroutes = find_all_routes(graph1, street , end, route)
        for newroute in newroutes:
            routes.append(newroute)
    return routes

    if start == end:
        return [route]
    routes = []
    for street in graph2[start]:
        if street not in route:
            newroutes = find_all_routes(graph2, street , end, route)
        for newroute in newroutes:
            routes.append(newroute)
    return routes

print(find_all_routes(graph1,1, 6))
print(find_all_routes(graph2,1, 4))