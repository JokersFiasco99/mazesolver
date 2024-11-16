from window import MainWindow, Point, Line, Cell

def main():
    win = MainWindow(800, 600)
    
    # Test different cell configurations
    cell1 = Cell(win, 50, 50, 150, 150)  # All walls (default)
    cell1.draw()
    
    cell2 = Cell(win, 200, 50, 300, 150)  # No left wall
    cell2.has_left_wall = False
    cell2.draw()
    
    cell3 = Cell(win, 350, 50, 450, 150)  # Only top and bottom walls
    cell3.has_left_wall = False
    cell3.has_right_wall = False
    cell3.draw()
    
    cell4 = Cell(win, 50, 200, 150, 300)  # Only side walls
    cell4.has_top_wall = False
    cell4.has_bottom_wall = False
    cell4.draw()
    
    cell5 = Cell(win, 200, 200, 300, 300)  # Single wall
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell5.has_bottom_wall = False
    cell5.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()