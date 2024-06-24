import logging
import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt

from reconstruction import Reconstruction
from simulation import Simulation

class OpticalFlatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Optical Flat Simulation and Reconstruction Tool")
        width = 400
        height = 400
        self.root.geometry(str(width)+"x"+str(height))
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        btn_simulation = tk.Button(self.frame, text="SIMULATION", bg="lightblue", font=("Arial", int(min(width,height)/30)), command=self.open_simulation)
        btn_reconstruction = tk.Button(self.frame, text="RECONSTRUCTION", bg="lightgreen", font=("Arial", int(min(width,height)/30)), command=self.open_reconstruction)
        btn_simulation.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn_reconstruction.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        logging.info("Application started")

    def on_closing(self):
        print("Closing application...")
        self.root.destroy()
        self.root.quit()

    def open_simulation(self):
        simulation_window = tk.Toplevel()
        Simulation(simulation_window)

    def open_reconstruction(self):
        reconstruction_window = tk.Toplevel()
        Reconstruction(reconstruction_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = OpticalFlatApp(root)
    root.mainloop()
