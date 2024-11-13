from tkinter import Tk, BOTH, Canvas    

class MainWindow:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Drawing App")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

    def run(self):
        self.root.mainloop()