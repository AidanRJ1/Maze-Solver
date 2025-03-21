from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2 ):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(min(self._x1, self._x2), min(self._y1, self._y2))
        top_right = Point(max(self._x1, self._x2), min(self._y1, self._y2))
        bottom_left = Point(min(self._x1, self._x2), max(self._y1, self._y2))
        bottom_right = Point(max(self._x1, self._x2), max(self._y1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), "black")
        else:
            self._win.draw_line(Line(top_left, bottom_left), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), "black")
        else:
            self._win.draw_line(Line(top_right, bottom_right), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), "black")
        else:
            self._win.draw_line(Line(top_left, top_right), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right), "black")
        else:
            self._win.draw_line(Line(bottom_left, bottom_right), "white")
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        fill_colour = "red"
        current_x = (self._x1 + self._x2) / 2
        current_y = (self._y1 + self._y2) / 2
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2
        current_point = Point(current_x, current_y)
        to_point = Point(to_x, to_y)
        if undo:
            fill_colour = "gray"
        self._win.draw_line(Line(current_point, to_point), fill_colour)
        