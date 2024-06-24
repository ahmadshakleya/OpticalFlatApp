import logging
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from gui_utility.utility import export_shapes, import_shapes

class FileTab(ttk.Frame):
    def __init__(self, parent, ThreeDViewTab):
        super().__init__(parent)
        self.ThreeDViewTab = ThreeDViewTab
        self.setup_widgets()

    def setup_widgets(self):
        ttk.Button(self, text="Export Configuration", command=self.export_configuration).pack(side=tk.LEFT)
        ttk.Button(self, text="Import Configuration", command=self.import_configuration).pack(side=tk.LEFT)

    def export_configuration(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.shapes = self.ThreeDViewTab.list_shapes
            export_shapes(self.shapes, filename)
            messagebox.showinfo("Export", "Configuration exported successfully.")
            logging.info("Configuration exported successfully to following file: "+ filename)

    def import_configuration(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            self.shapes = import_shapes(filename)
            for shape in self.shapes:
                print(shape[1])
                print(shape[0])
                self.ThreeDViewTab.add_shape(shape[0], shape[1])
            messagebox.showinfo("Import", "Configuration imported successfully.")
            logging.info("Configuration imported successfully from following file: "+ filename)