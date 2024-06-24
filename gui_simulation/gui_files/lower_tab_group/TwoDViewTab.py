import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TwoDViewTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_plot()

    def create_plot(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        self.ax.view_init(elev=90, azim=0)
        self.ax.grid(False)
        self.ax._axis3don = False

        self.canvas_widget.bind("<Configure>", lambda event: self.canvas.draw())

    def update_plot(self, objects):
        # This method would update the plot with new objects or transformations
        pass
