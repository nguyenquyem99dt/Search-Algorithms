import mapio
import numpy as np

def ucs(p_map, start, goal):
    _from = dict()
    _cost_to = dict()
    q = []
    cost = np.zeros((p_map.shape[0], p_map.shape[1]), dtype = int)
    q.append(start)
    _from[str(start)] = start
    _cost_to[str(start)] = 0

    while q.__len__() > 0:
        current = get_promissing(q, cost)
        q.remove(current)
        if np.all(current == goal):
            return _from, _cost_to[str(goal)]
            
        for point in extend(p_map, current):
            cost_to = _cost_to[str(current)] + 1
            if str(point) not in _cost_to or cost_to < _cost_to[str(point)]:
                _cost_to[str(point)] = cost_to
                cost[point[1], point[0]] = cost_to
                q.append(point)
                _from[str(point)] = current
    
    return _from, np.inf



def get_promissing(q, cost):
    min_cost = -1
    min_point = q[0]
    for point in q:
        if min_cost == -1 or cost[point[1], point[0]] < min_cost:
            min_point = point
            min_cost = cost[point[1], point[0]]
    return min_point

def extend(p_map, current):
    dt = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    near = []
    for vt in dt:
        new_vertex = (current[0] + vt[0], current[1] + vt[1])
        if new_vertex[0] < p_map.shape[1] and new_vertex[0] > 0 and new_vertex[1] > 0 and new_vertex[1] < p_map.shape[0]:
            if not np.all(p_map[new_vertex[1], new_vertex[0]] == [255, 255, 102]) and not np.all(p_map[new_vertex[1], new_vertex[0]] == [183, 183, 183]):
                near.append(new_vertex)
    return near


_map, vertex = mapio.load_map('input.txt')

mapio.find_path(ucs, _map, vertex)

mapio.draw(_map,'Uniform Cost Search')