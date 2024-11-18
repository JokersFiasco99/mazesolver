from tkinter import Tk, BOTH, Canvas    
import time

class MainWindow:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Drawing App")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):    
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win, x1, y1, x2, y2):
        self._win = win
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
            
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
            
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
            
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        # Calculate center points
        from_x = (self._x1 + self._x2) // 2
        from_y = (self._y1 + self._y2) // 2
        to_x = (to_cell._x1 + to_cell._x2) // 2
        to_y = (to_cell._y1 + to_cell._y2) // 2
        
        # Create and draw the line
        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        self._win.draw_line(line, "gray" if undo else "red")

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                self._draw_cell(i, j)
                row_cells.append(self._cells[i][j])
            self._cells.append(row_cells)
    
    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + j * self._cell_size_x
        cell_y1 = self._y1 + i * self._cell_size_y
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        
        if len(self._cells) <= i:
            self._cells.append([])
        while len(self._cells[i]) <= j:
            self._cells[i].append(None)
            
        cell = Cell(self._win, cell_x1, cell_y1, cell_x2, cell_y2)
        self._cells[i][j] = cell
        cell.draw()
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

