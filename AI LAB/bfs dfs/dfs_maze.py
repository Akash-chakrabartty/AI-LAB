from pyamaze import maze, agent, COLOR, textLabel
import sys


def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []

    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)

        if currCell == m._goal:
            break

        poss = 0
        for d in "ESNW":
            if m.maze_map[currCell][d]:

                if d == "E":
                    child = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    child = (currCell[0], currCell[1] - 1)
                elif d == "N":
                    child = (currCell[0] - 1, currCell[1])
                elif d == "S":
                    child = (currCell[0] + 1, currCell[1])

                if child in explored:
                    continue

                poss += 1
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell

        if poss > 1:
            m.markCells.append(currCell)

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return dSearch, fwdPath


m = maze(10, 10)
m.CreateMaze()

dSearch, fwdPath = DFS(m)

# Agent showing full DFS exploration
a = agent(m, footprints=True, shape="square",
          color=COLOR.green, filled=False)
m.tracePath({a: dSearch}, showMarked=True)

# Agent showing final DFS path
c = agent(m, footprints=True, color=COLOR.yellow, filled=True)
m.tracePath({c: fwdPath}, delay=300)

l = textLabel(m, "DFS Path Length", len(fwdPath) + 1)

m.run()
