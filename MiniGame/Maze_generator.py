# todo ссылка - https://habr.com/ru/post/262345/
# todo ссылка - https://habr.com/ru/post/176671/ https://habr.com/ru/post/320140/

import numpy as np
import random


class Cell(object):
    """структура, хранящая координаты клетки в матрице"""

    def __init__(self, x, y):
        """Construction"""
        self.x = x
        self.y = y


class CellString(object):
    """"структура, хранящая координаты клетки в матрице"""
    cells = []


class MazeGenerator(object):
    """azazaza"""

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.CELL = 0
        self.WALL = 1
        self.VISITED = 2
        self.distance = 2
        self.maze = np.random.randint(10, size=(self.height, self.width))
        # print("maze =", self.maze, "\n")





    def getNeighbours(self, c):
        """проверка, были на соседних клетках
           и сохранение непосещенных клеток
        """
        cell_up = Cell(c.x, c.y - self.distance)
        cell_rt = Cell(c.x + self.distance, c.y)
        cell_dw = Cell(c.x, c.y + self.distance)
        cell_lt = Cell(c.x - self.distance, c.y)

        cell_d = [cell_up, cell_rt, cell_dw, cell_lt]

        cell_nepos = CellString()
        cell_nepos.cells.clear()

        for i in cell_d:
            if i.x > 0 and i.x < self.height and i.y > 0 and i.y < self.width:
                # print("AA", i.x, i.y)
                mazeCellcurrent = self.maze[i.x][i.y]
                # print("AA - done")
                if mazeCellcurrent != self.WALL and mazeCellcurrent != self.VISITED:
                    # print("AA", i.x, i.y)
                    cell_nepos.cells.append(i)
        return cell_nepos


    def removeWall(self, first, second):
        """
        удаление стенок
        """
        xDiff = second.x - first.x
        yDiff = second.y - first.y

        if xDiff != 0:
            addX = int(xDiff / abs(xDiff))
        else:
            addX = 0

        if yDiff != 0:
            addY = int(yDiff / abs(yDiff))
        else:
            addY = 0

        target = Cell(first.x + addX, first.y + addY)
        self.maze[target.x][target.y] = self.VISITED


    def unvisitedCount(self):
        unvisited = 0
        for i in self.maze:
            for j in i:
                if j == self.CELL:
                    unvisited = unvisited + 1
        return unvisited


    def getunvisitedCells(self):
        returnValue = CellString()
        for i in range(1, self.width - 1):
            for j in range(1, self.height - 1):
                if self.maze[i][j] == self.CELL:
                    returnValue.cells.append(Cell(i, j))
        return returnValue

    def generate(self):
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                if ((i % 2 != 0) and (j % 2 != 0)) and ((i < self.height - 1) and (j < self.width - 1)):
                    self.maze[i][j] = self.CELL
                else:
                    self.maze[i][j] = self.WALL
                j = j + 1
                # print("j =", j)
            i = i + 1
            # print("i =", i)
        # print(self.maze)

        startCell = Cell(1, 1)  # начальная точка
        currentCell = startCell
        neighbourCell = Cell(1, 1)
        stack = []

        self.maze[startCell.x][startCell.y] = self.VISITED

        while self.unvisitedCount() > 0:
            neighbour = CellString()
            neighbour.cells.clear()
            neighbour = self.getNeighbours(currentCell)

            if len(neighbour.cells) > 0:
                randNum = random.randint(0, len(neighbour.cells) - 1)
                neighbourCell = neighbour.cells[randNum]
                stack.append(currentCell)
                self.removeWall(currentCell, neighbourCell)
                # print(neighbourCell.x, neighbourCell.y)
                currentCell = neighbourCell
                self.maze[currentCell.x][currentCell.y] = self.VISITED

                # print("neighbourCell - ", type(neighbourCell), currentCell.x, currentCell.y)

            elif len(stack) > 0:
                # print(2)
                currentCell = stack.pop()
            else:
                # print(3)
                cellStringUnvisited = self.getunvisitedCells()
                randNum = random.randint(0, len(cellStringUnvisited.cells) - 1)
                currentCell = cellStringUnvisited.cells[randNum]

            # print(self.maze, "\n")
        return self.maze
#
# class ExitPoint(object):
#     def __init__(self):
#         self.