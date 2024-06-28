# Makes the screen semi-transparent and allows the user to select a region on the screen by dragging the mouse. The selected region is returned as a tuple of (x1, y1, x2, y2) coordinates. This is useful for selecting a region on the screen to capture or perform OCR on. This module is used in the main.py script to select a region on the screen to capture and translate text from.
import tkinter as tk

class SelectionTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.configure(background='black')
        self.root.attributes("-topmost", True)

        # Coordinate Variables
        self.start_x = None
        self.start_y = None
        self.rect = None

        # Canvas
        self.canvas = tk.Canvas(self.root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        self.selected_region = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        self.selected_region = (self.start_x, self.start_y, event.x, event.y)
        self.root.quit()

    def get_selection(self):
        self.root.mainloop()
        self.root.destroy()
        return self.selected_region

def select_screen_region():
    tool = SelectionTool()
    print("Select a region on the screen...")
    return tool.get_selection()
