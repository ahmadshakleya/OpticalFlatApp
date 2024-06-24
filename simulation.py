import logging
import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt

from gui_simulation.gui_files.lower_tab_group.ThreeDViewTab import ThreeDViewTab
from gui_simulation.gui_files.lower_tab_group.TwoDViewTab import TwoDViewTab
from gui_simulation.gui_files.upper_tab_group.gui_FileTab import FileTab 
from gui_simulation.gui_files.upper_tab_group.gui_HelpTab import HelpTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab import InsertTab
from gui_simulation.gui_files.upper_tab_group.gui_LogTab import LogTab
from gui_simulation.gui_files.upper_tab_group.gui_ViewTab import ViewTab

class Simulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulation Window")
        width = 600
        height = 600
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        self.shapes = None

        self.lower_notebook = ttk.Notebook(self.paned_window, height=round(height*4/5))
        self.three_d_view_tab = ThreeDViewTab(self.lower_notebook)
        self.lower_notebook.add(self.three_d_view_tab, text="3D View")

        self.upper_notebook = ttk.Notebook(self.paned_window, height=round(height*1/5))
        #self.file_tab = FileTab(self.upper_notebook)
        self.insert_tab = InsertTab(self.upper_notebook, self.three_d_view_tab)
        self.view_tab = ViewTab(self.upper_notebook)
        self.help_tab = HelpTab(self.upper_notebook)
        self.log_tab = LogTab(self.upper_notebook)
        self.file_tab = FileTab(self.upper_notebook, self.three_d_view_tab)

        self.upper_notebook.add(self.file_tab, text='File')
        self.upper_notebook.add(self.insert_tab, text='Insert')
        self.upper_notebook.add(self.view_tab, text='View')
        self.upper_notebook.add(self.help_tab, text='Help')
        self.upper_notebook.add(self.log_tab, text='Log')
        self.paned_window.add(self.upper_notebook, weight=1)
        self.paned_window.add(self.lower_notebook, weight=4)

        logging.info("Simulation window opened")

    def on_closing(self):
        print("Closing simulation window...")
        #self.three_d_view_tab.clear_shapes()
        self.three_d_view_tab.on_closing()
        #plt.close(self.three_d_view_tab.fig)
        self.root.destroy()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Simulation(root)
    root.mainloop()