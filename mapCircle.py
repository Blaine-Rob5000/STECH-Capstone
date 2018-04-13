"""
Map Circle

by R.G. Blaine, 4/12/2018
"""

import math

def mapCircle(centerX, centerY, radius):
    TOL = math.sqrt(2) - 1
    startX = centerX - radius
    startY = centerY - radius
    endX = centerX + radius + 1
    endY = centerY + radius + 1
    circleCoords = []
    for mapY in range(startY, endY):
        for mapX in range(startX, endX):
            diffX = mapX - centerX
            diffY = mapY - centerY
            if math.sqrt(diffX ** 2 + diffY ** 2) <= (radius + TOL):
                circleCoords.append((mapX, mapY))
    return circleCoords


def drawMap(circleCoords):
    mapWidth = 0
    mapHeight = 0
    for coords in circleCoords:
        x, y = coords
        if x > mapWidth:
            mapWidth = x
        if y > mapHeight:
            mapHeight = y
    print("Radius:", mapWidth//2)
    for mapY in range(mapHeight + 1):
        for mapX in range(mapWidth + 1):
            if (mapX, mapY) in circleCoords:
                print("-@", end = "")
            else:
                print("--", end = "")
        print("-")


for x in range(1, 11):
    drawMap(mapCircle(x, x, x))
    print()
