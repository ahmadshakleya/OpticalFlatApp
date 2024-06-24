import tkinter as tk
from tkinter import ttk

from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.CylinderTab import CylinderTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.DiskTab import DiskTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.Flat_surfaceTab import FlatSurfaceTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.STLFigureTab import STLFigureTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.OpticalFlatTab import OpticalFlatTab

class InsertTab(ttk.Frame):
    def __init__(self, parent, three_d_view_tab):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.three_d_view_tab = three_d_view_tab
        self.setup_widgets()

    def setup_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)

        self.cylinder_tab = CylinderTab(self.notebook, self.three_d_view_tab)
        self.notebook.add(self.cylinder_tab, text='Cylinder')

        self.disk_tab = DiskTab(self.notebook, self.three_d_view_tab)
        self.notebook.add(self.disk_tab, text='Disk')

        self.flat_surface_tab = FlatSurfaceTab(self.notebook, self.three_d_view_tab)
        self.notebook.add(self.flat_surface_tab, text='Flat Surface')

        self.optical_flat_tab = OpticalFlatTab(self.notebook, self.three_d_view_tab)
        self.notebook.add(self.optical_flat_tab, text='Optical Flat')

        self.stl_figure_tab = STLFigureTab(self.notebook, self.three_d_view_tab)
        self.notebook.add(self.stl_figure_tab, text='STL Figure')

if __name__ == "__main__":
    root = tk.Tk()
    app = InsertTab(root)
    root.mainloop()
