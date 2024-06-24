import logging
import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt

from gui_reconstruction.gui_FileTab import FileTab
from gui_reconstruction.gui_imageprocessingtab import ImageProcessingTab
from gui_reconstruction.gui_HelpTab import HelpTab
from gui_reconstruction.gui_LogTab import LogTab
from gui_reconstruction.gui_ViewTab import ViewTab

class Reconstruction:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconstruction Window")
        width = 600
        height = 600
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self.upper_notebook = ttk.Notebook(self.paned_window, height=round(height*1/5))
        self.file_tab = FileTab(self.upper_notebook)
        self.imageprocessing_tab = ImageProcessingTab(self.upper_notebook, self.file_tab)
        self.view_tab = ViewTab(self.upper_notebook)
        self.help_tab = HelpTab(self.upper_notebook)
        self.log_tab = LogTab(self.upper_notebook)

        self.upper_notebook.add(self.file_tab, text='File')
        self.upper_notebook.add(self.imageprocessing_tab, text='Image Processing')
        self.upper_notebook.add(self.view_tab, text='View')
        self.upper_notebook.add(self.help_tab, text='Help')
        self.upper_notebook.add(self.log_tab, text='Log')

        self.paned_window.add(self.upper_notebook, weight=1)

        logging.info("Reconstruction window opened")

    def on_closing(self):
        logging.info("Closing reconstruction window...")
        if hasattr(self, 'file_tab'):
            self.file_tab.cleanup()
        if hasattr(self, 'image_processing_tab'):
            self.image_processing_tab.cleanup()

        self.root.destroy()
        self.root.quit()
        logging.info("Reconstruction window closed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Reconstruction(root)
    root.mainloop()