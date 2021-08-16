'''
Task
You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1]. Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

Location altitude is defined as an integer number (0-9).

Path Finder Series:
#1: can you reach the exit?
#2: shortest path
#3: the Alpinist
#4: where are you?
#5: there's someone here
'''

from heapq import *
from collections import defaultdict
from math import sqrt, floor

dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def path_finder(maze):
    n = floor(sqrt(len(maze)))
    N = n * n
    edge = defaultdict(list)
    maze = [int(i) for i in list(maze) if i !='\n']
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dirc[i][0]
                ny = y + dirc[i][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                d = abs(maze[nx * n + ny] - maze[x * n + y])
                edge[x * n + y] += [[nx * n + ny, d]]
    return find_ways(edge, 0, N)

def find_ways(edge, start, N):
    heap = []
    distance = [-1] * N
    distance[start] = 0
    heappush(heap, [start, distance[start]])
    while len(heap) > 0:
        d0 = heappop(heap)[0]
        if d0 == N - 1:
            return distance[d0]
        for i in range(len(edge[d0])):
            next = edge[d0][i][0]
            l = edge[d0][i][1]
            if distance[next] == -1 or distance[d0] + l < distance[next]:
                distance[next] = distance[d0] + l
                heappush(heap, [next, distance[next]])
    return distance[N - 1]