from window import MainWindow, Point, Line

def main():
    win = MainWindow(800, 600)
    
    # Draw some test lines
    line1 = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(200, 200), Point(300, 100))
    line3 = Line(Point(300, 100), Point(400, 200))
    
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue") 
    win.draw_line(line3, "green")

    win.wait_for_close()

if __name__ == "__main__":
    main()