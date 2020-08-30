import numpy as np
import mapio

def extend(p_map, current):
    dt = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    near = []
    for vt in dt:
        new_vertex = (current[0] + vt[0], current[1] + vt[1])
        if new_vertex[0] < p_map.shape[1] and new_vertex[0] > 0 and new_vertex[1] > 0 and new_vertex[1] < p_map.shape[0]:
            if not np.all(p_map[new_vertex[1], new_vertex[0]] == [255, 255, 102]) and not np.all(p_map[new_vertex[1], new_vertex[0]] == [183, 183, 183]):
                near.append(new_vertex)
    return near

def dfs(p_map,start,goal):
    queue=[]
    visited=[]
    previous=dict()
    _cost_to=dict()
    queue.append(start)
    _cost_to[str(start)]=0
    while len(queue)>0:
        current=queue.pop()
        visited.append(current)
        if np.all(current==goal):
            return previous, _cost_to[str(goal)]
        for point in extend(p_map,current):
            cost_to=_cost_to[str(current)]+1
            if point not in visited and point not in queue:
                _cost_to[str(point)]=cost_to
                previous[str(point)]=current
                queue.append(point)
    return previous, np.inf

_map, vertex = mapio.load_map('input.txt')
mapio.find_path(dfs,_map,vertex)
mapio.draw(_map,'Depth First Search')