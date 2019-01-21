##Local Improvement && TSP
##Tyler Hackel
##Josie Zucca
##Avery Guething

#

import random, math
from itertools import permutations
import sys
import copy

##TO SEE SOLUTIONS CALL FUNCTIONS:
##   LOCAL IMPROVEMENT              *****local(getCoords(10))
##   TRAVELING SALESMAN             *****travel()

##LOCAL IMPROVEMENT
def getCoords(n):
      coords = []
      for x in range(n):
            coords.append((random.randint(0,100), random.randint(0,100)))
      return coords

def local(x):
      perm = permutations(x)
      curDist = 0
      curList = []
      bestDist = 0
      bestList = []
      for i in list(perm):
            curList = i
            curDist = 0
            for y in range(int(len(i)-1)):
            


                  
                  x1 = i[y][0]
                  x2 = i[(y+1)][0]
                  y1 = i[y][1]
                  y2 = i[(y+1)][1]
                  curDist += math.sqrt((x2-x1)**2 + (y2-y1)**2)

            if bestDist == 0:
                  bestDist = curDist
                  bestList = i
            elif curDist < bestDist:
                  bestDist = curDist
                  bestList = i
            print("Distance: " + str(curDist))
            print("List: " + str(curList))
                  
      print("Best Distance: " + str(bestDist))
      print("Best List: " + str(bestList))


##TRAVELING SALESMAN
      
travel_matrix = []
travel_list = []
for n in range(10):
      travel_list = []
      for p in range(10):
            if n == p:
                  travel_list.append(0)
            else:
                  travel_list.append(random.randint(0,100))
      travel_matrix.append(travel_list)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(data)
all_sets = []
g = {}
p = []

def travel():
    for x in range(1, n):
        g[x + 1, ()] = travel_matrix[x][0]

    get_minimum(1, (2,3,4,5,6,7,8,9,10))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(travel_matrix[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]
      
            
                  
                  
                  






      

