# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import sys, pygame

pygame.init()
pygame.display.set_caption("A-Star Example App")
icon = pygame.image.load("icon.png") # Icon Made By Becris From www.flaticon.com
pygame.display.set_icon(icon)       
          
def heuristic_func(start,end):
    return math.sqrt(pow(start.x-end.x,2)+pow(start.y-end.y,2))

def A_star_Route(result):
    route = []
    while result.parent:
        route.insert(0, result)
        result = result.parent
    return route

def A_star(start,end):
    start.h = heuristic_func(start,end)
    start.f = start.g + start.h
    open_list = [start]
    closed_list = []
    while open_list:
        minimum = 10000
        indx = -1
        for item in open_list:
            if minimum > item.f:
                minimum = item.f
                indx = open_list.index(item)
        q = open_list.pop(indx)
        if q.x == end.x and q.y == end.y:
            return q
    
        for i in range (0,q.komsu.__len__()):
            q.komsu[i].g = q.g + 1
            q.komsu[i].h = heuristic_func(q.komsu[i],end)
            q.komsu[i].f = q.komsu[i].g + q.komsu[i].h
            q.komsu[i].parent = q
            q.komsu[i].komsu = Nodes[q.komsu[i].y*y_const + q.komsu[i].x].komsu
            temp = Node(-1,-1)
            temp.g = 99
            for item in open_list:
                if item.x == q.komsu[i].x and item.y == q.komsu[i].y:
                    temp = item
            if q.komsu[i].g > temp.g:
                continue
            temp.g = 99
            for item in closed_list:
                if item.x == q.komsu[i].x and item.y == q.komsu[i].y:
                    temp = item
            if q.komsu[i].g > temp.g:
                continue
            else:
                open_list.append(q.komsu[i])
        closed_list.append(q)

class Node:
    def __init__(self,y,x):
        self.x = x
        self.y = y
        self.komsu = []
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = 0

Nodes = []

size = width, heigth = 320,240
black = 0,0,0
speed = 23
OffsetX = 16
OffsetY = 15

screen = pygame.display.set_mode(size)

mazemap = pygame.image.load("Map.png")
mazemaprect = mazemap.get_rect()

pacman = pygame.image.load("pacman.png")
pacmanrect = pacman.get_rect()
pacmanrect.left = OffsetX
pacmanrect.top = OffsetY

enemy = pygame.image.load("enemy.png")
enemyrect = enemy.get_rect()
enemyrect.left = OffsetX + 7*speed
enemyrect.top = OffsetY + 4*speed

x, y = 1,1
enemy_x , enemy_y = 8,5
Col_Map = [[1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,1,0,0,0,0,1],
           [1,0,1,1,0,1,0,1,1,0,1],
           [1,0,1,0,0,0,0,0,1,0,1],
           [1,0,1,0,1,1,1,0,1,0,1],
           [1,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,0,1,1,1,0,1,0,1],
           [1,0,1,0,0,0,0,0,1,0,1],
           [1,0,1,1,0,1,0,1,1,0,1],
           [1,0,0,0,0,1,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1]]
y_const = 11

for i in range(11):
    for j in range(11):
        if i == 0 or i == 10 or j == 0 or j == 10:
            Nodes.append(0)
            continue
        if Col_Map[i][j] == 0:
            temp = Node(i,j)
            if Col_Map[i-1][j] == 0:
                temp.komsu.append(Node(i-1,j))
            if Col_Map[i][j-1] == 0:
                temp.komsu.append(Node(i,j-1))
            if Col_Map[i+1][j] == 0:
                temp.komsu.append(Node(i+1,j))
            if Col_Map[i][j+1] == 0:
                temp.komsu.append(Node(i,j+1))
            Nodes.append(temp)
        if Col_Map[i][j] == 1:
            Nodes.append(0)


route = []
result = Node(0,0)
AI_Time = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and Col_Map[y][x+1] != 1:
            pacmanrect = pacmanrect.move([speed,0])
            x = x+1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and Col_Map[y][x-1] != 1:
            pacmanrect = pacmanrect.move([-speed,0])
            x = x-1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and Col_Map[y+1][x] != 1:
            pacmanrect = pacmanrect.move([0,speed])
            y = y+1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and Col_Map[y-1][x] != 1:
            pacmanrect = pacmanrect.move([0,-speed])
            y = y-1
    
    if result.x != x or result.y != y and AI_Time > 499:
        result = A_star(Nodes[enemy_y*y_const + enemy_x],Nodes[y*y_const+x])
        route = A_star_Route(result)
    
    if route and AI_Time > 499:
        enemyrect = enemyrect.move([(route[0].x-enemy_x)*speed,(route[0].y-enemy_y)*speed])
        enemy_x = route[0].x
        enemy_y = route[0].y
        route.pop(0)
        
    if AI_Time > 499:
        AI_Time = 0
        
    screen.fill(black)
    screen.blit(mazemap,mazemaprect)
    screen.blit(pacman,pacmanrect)
    screen.blit(enemy,enemyrect)
    pygame.display.flip()
    AI_Time += 13
    pygame.time.wait(13)
    

