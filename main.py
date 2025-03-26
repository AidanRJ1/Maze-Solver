from maze import Maze
from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800, 800)
    maze = Maze(10, 10, 12, 15, 100, 100, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()