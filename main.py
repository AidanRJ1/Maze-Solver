from maze import Maze
from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800, 800)
    maze = Maze(10, 10, 5, 5, 100, 100, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()