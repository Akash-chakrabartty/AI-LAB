import sys
from collections import deque

from pyamaze import COLOR, agent, maze, textLabel

sys.setrecursionlimit(2000)


def BFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    start_cell = start
    goal_cell = m._goal

    queue = deque([start_cell])
    visited = [start_cell]
    bfsPath = {}
    bSearch = [start_cell]

    while queue:
        cell = queue.popleft()

        if cell == goal_cell:
            break

        for direction in "ESNW":
            if m.maze_map[cell][direction]:

                if direction == "E":
                    nextCell = (cell[0], cell[1] + 1)
                elif direction == "W":
                    nextCell = (cell[0], cell[1] - 1)
                elif direction == "N":
                    nextCell = (cell[0] - 1, cell[1])
                elif direction == "S":
                    nextCell = (cell[0] + 1, cell[1])

                if nextCell not in visited:
                    visited.append(nextCell)
                    queue.append(nextCell)
                    bfsPath[nextCell] = cell
                    bSearch.append(nextCell)

    path_list = []
    cell = goal_cell
    while cell != start_cell:
        path_list.append(cell)
        cell = bfsPath[cell]
    path_list.append(start_cell)
    path_list.reverse()

    fwdPath = {}
    for i in range(len(path_list) - 1):
        fwdPath[path_list[i]] = path_list[i + 1]

    return bSearch, fwdPath, bfsPath


if __name__ == "__main__":
    m = maze(10, 10)
    m.CreateMaze(loopPercent=50)

    bSearch_order, solution_path, pred_map = BFS(m)

    a = agent(m, footprints=True, color=COLOR.green, shape="square")
    m.tracePath({a: bSearch_order}, delay=50)

    b = agent(m, footprints=True, color=COLOR.yellow, shape="square", filled=True)
    m.tracePath({b: solution_path}, delay=10)

    l = textLabel(m, "BFS Path Length", len(solution_path) + 1)

    # Run the visualization
    m.run()