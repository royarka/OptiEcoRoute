graph={
    "Kolkata":{
        'pos':(22.57947979291229, 88.37750002351007),
        'edges':{
            "Kharagpur":135,
            "Bardhaman":102,
            "Durgapur":172,
            "Asansol":213,
        }
    },
    "Kharagpur":{
            'pos':(22.3258, 87.3204),
            'edges':{
                "Kolkata":135,
                "Tatanagar":151
            }
        },
    "Tatanagar":{
        'pos':(22.7687,86.20268),
        'edges':{
            "Kharagpur":151,
            "Rourkela":163
        }
    },
    "Rourkela":{
        'pos':(22.22496,84.86414),
        'edges':{
            "Tatanagar":163
        }
    }
    ,
    "Bardhaman": {
    'pos': (23.233, 87.867),
    'edges': {
        "Durgapur": 75.4,
        "Kolkata": 102,
        "Malda": 240
    }
    },
    "Durgapur":{
            'pos':(23.5334,87.3219),
            'edges':{
                "Asansol":42.3,
                "Bardhaman":75.4,
                "Kolkata":172
            }
        },
    "Asansol":{
            'pos':(23.6889,86.9749),
            'edges':{
                "Durgapur":42.3,
                "Bardhaman":116,
                "Kolkata":213
            }
        },
    "Malda":{
            'pos':(25.0108,88.1411),
            'edges':{
                "Siliguri":242,
                "Bardhaman":240
            }
        },
    "Siliguri":{
            'pos':(26.732311,88.410286),
            'edges':{
                "Bardhaman":240,
                "Jalpaiguri":51.5,
                "Malda":242
            }
        },
    "Jalpaiguri":{
            'pos':(26.5405,88.7194),
            'edges':{
                "Siliguri":51.5,
                "Malda":260
            }
        }
}

import math
import heapq

def heuristic(current,goal):
    lat1,lon1=graph[current]["pos"]
    lat2,lon2=graph[goal]["pos"]
    return math.sqrt((lat2-lat1)**2+(lon2-lon1)**2)

def astar(start,goal):
    queue=[(0,start)]
    cost={start:0}
    parent={start:None}
    while queue:
        i,current=heapq.heappop(queue)
        if current==goal:
            break
        for neighbour,dist in graph[current]["edges"].items():
            n_cost=cost[current]+dist
            if neighbour not in cost or n_cost<cost[neighbour]:
                cost[neighbour]=n_cost
                res=n_cost+heuristic(neighbour,goal)
                heapq.heappush(queue,(res,neighbour))
                parent[neighbour]=current
    route=[]
    current=goal
    while current is not None:
        route.append(current)
        current = parent[current]
    route.reverse()
    return route,cost[goal]
print(astar("Kolkata","Siliguri"))