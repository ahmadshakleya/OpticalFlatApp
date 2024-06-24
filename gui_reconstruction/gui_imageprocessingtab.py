import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.interpolate import griddata
from matplotlib import cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage.restoration import unwrap_phase
import logging

from gui_reconstruction.reconstruction_algorithm import calculate_height_map, extract_phase, filter_frequencies, load_image, perform_fft, perform_ifft


class ImageProcessingTab(ttk.Frame):
    def __init__(self, parent, file_tab):
        super().__init__(parent)
        self.image_path = None
        self.canvas = None
        file_tab.image_loaded_callback = self.update_image_path 
        self.setup_widgets()
        logging.info("ImageProcessingTab initialized without image.")

    def update_image_path(self, path):
        self.image_path = path
        logging.info(f"Image path updated to {path}.")
        self.load_and_process_image()

    def setup_widgets(self):
        button_frame = ttk.Frame(self)  # Create a frame to hold buttons
        button_frame.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(button_frame, text="Load and Process Image", command=self.load_and_process_image).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete Plot", command=self.delete_plot).pack(side=tk.LEFT)
        settings_frame = ttk.Frame(self)
        settings_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(settings_frame, text="Wavelength (m):").pack(side=tk.LEFT)
        self.wavelength_entry = ttk.Entry(settings_frame, width=12)
        self.wavelength_entry.pack(side=tk.LEFT, padx=5)
        self.wavelength_entry.insert(0, "632.8e-9")

        ttk.Label(settings_frame, text="Refractive Index:").pack(side=tk.LEFT)
        self.refractive_index_entry = ttk.Entry(settings_frame, width=12)
        self.refractive_index_entry.pack(side=tk.LEFT, padx=5)
        self.refractive_index_entry.insert(0, "1.5")

        logging.info("Widgets setup: Load and Process Image, Delete Plot buttons and Entry fields for Wavelength and Refractive Index added.")

    def load_and_process_image(self):
        if not self.image_path:
            messagebox.showinfo("Error", "No image loaded to process.")
            logging.warning("No image path set when attempting to load and process image.")
            return

        image = load_image(self.image_path)
        fft_image = perform_fft(image)
        filtered_fft_image = filter_frequencies(fft_image)
        filtered_image = perform_ifft(filtered_fft_image)
        phase_map = extract_phase(filtered_image)
        unwrapped_phase = unwrap_phase(phase_map)
        wavelength = float(self.wavelength_entry.get())
        refractive_index = float(self.refractive_index_entry.get())
        self.height_map = calculate_height_map(unwrapped_phase, wavelength=wavelength, refractive_index=refractive_index)
        smoothed_height_map = gaussian_filter(self.height_map, sigma=1)
        min_height = np.min(smoothed_height_map)
        max_height = np.max(smoothed_height_map)
        mean_height = np.mean(smoothed_height_map)
        std_dev_height = np.std(smoothed_height_map)
        
        logging.info(f"Image processing complete. Statistics - Min: {min_height}, Max: {max_height}, Mean: {mean_height}, Std Dev: {std_dev_height}")
        
        self.plot_height_map(smoothed_height_map)

    def plot_height_map(self, height_map):
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        x = np.arange(0, height_map.shape[1], 1)
        y = np.arange(0, height_map.shape[0], 1)
        X, Y = np.meshgrid(x, y)
        Z = height_map.flatten()
        points = np.vstack((X.ravel(), Y.ravel())).T
        values = Z
        grid_x, grid_y = np.mgrid[0:height_map.shape[0]:1000j, 0:height_map.shape[1]:1000j]
        grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')
        surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap=cm.viridis, linewidth=0, antialiased=False)

        #X, Y = np.meshgrid(np.arange(height_map.shape[1]), np.arange(height_map.shape[0]))
        #surf = ax.plot_surface(X, Y, height_map, cmap=cm.viridis)
        ax.set_title('Height Map')
        ax.set_xlabel("X (pixels)")
        ax.set_ylabel("Y (pixels)")
        ax.set_zlabel("Height")
        #fig.colorbar(surf)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        logging.info("Height map plotted.")
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def delete_plot(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
            logging.info("Plot deleted successfully.")
            messagebox.showinfo("Plot Deleted", "The current plot has been removed.")
        else:
            messagebox.showinfo("No Plot", "There is no plot to delete.")
            logging.warning("Attempted to delete a plot when none was displayed.")

    def set_image_path(self, path):
        self.image_path = path
        logging.info(f"Image path set to {path}.")
        messagebox.showinfo("Image Path Set", "Image path has been updated.")

    def cleanup(self):
        logging.info("Cleaning up ImageProcessingTab resources...")
        if hasattr(self, 'fig'):
            plt.close(self.fig)
            logging.info("Matplotlib figure resources cleaned.")
        if self.canvas:
            plt.close(self.canvas.figure)
            logging.info("Matplotlib figure resources cleaned.")