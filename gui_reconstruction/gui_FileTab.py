import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import logging

class FileTab(ttk.Frame):
    def __init__(self, parent, image_loaded_callback=None):
        super().__init__(parent)
        self.image = None
        self.image_path = None
        self.image_id = None
        self.zoom_scale = 1.0
        self.image_loaded_callback = image_loaded_callback
        self.setup_widgets()
        logging.info("Initialized FileTab with no image loaded.")
        self._drag_data = {"x": 0, "y": 0} 

    def setup_widgets(self):
        button_frame = ttk.Frame(self) 
        button_frame.pack(side=tk.TOP, fill=tk.X) 
        ttk.Button(button_frame, text="Import Image", command=self.import_image).pack(side=tk.LEFT)
        ttk.Button(button_frame, text="Delete Image", command=self.delete_image).pack(side=tk.LEFT)

        self.zoom_in_button = ttk.Button(button_frame, text="Zoom In", command=lambda: self.adjust_zoom(1.25))
        self.zoom_out_button = ttk.Button(button_frame, text="Zoom Out", command=lambda: self.adjust_zoom(0.8))
        self.zoom_in_button.pack(side=tk.LEFT)
        self.zoom_out_button.pack(side=tk.LEFT)
        self.zoom_in_button['state'] = 'disabled'
        self.zoom_out_button['state'] = 'disabled'

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True) 
        logging.info("Widgets set up: import and delete image buttons.")

    def import_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if filename:
            if self.image:
                messagebox.showinfo("Image Import", "An image is already loaded. Delete the current image before importing a new one.")
                logging.warning("Attempt to import a new image without deleting the existing one.")
                return

            self.image_path = filename
            self.image = Image.open(self.image_path)
            if self.image_loaded_callback:
                self.image_loaded_callback(self.image_path)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.display_image()
            messagebox.showinfo("Image Import", "Image imported successfully.")
            logging.info(f"Image imported successfully from {filename}.")


    def display_image(self):
        if self.image_tk:
            if self.image_id is not None:
                self.canvas.delete(self.image_id)
            self.canvas.create_image(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, image=self.image_tk, anchor='center')
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
            self.zoom_in_button['state'] = 'normal'
            self.zoom_out_button['state'] = 'normal'
            logging.info("Image displayed on the GUI.")
            self.add_image_bindings()

    def delete_image(self):
        if self.image is not None:
            self.image = None
            self.image_path = None
            self.image_tk = None
            if self.image_id:
                self.canvas.delete(self.image_id)
                self.image_id = None
            self.zoom_in_button['state'] = 'disabled'
            self.zoom_out_button['state'] = 'disabled'
            messagebox.showinfo("Image Delete", "Image deleted successfully.")
            logging.info("Current image deleted successfully.")
        else:
            messagebox.showinfo("Image Delete", "No image to delete.")
            logging.warning("Attempted to delete an image when none was loaded.")
    
    
    def add_image_bindings(self):
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)

    def adjust_zoom(self, factor):
        self.zoom_scale *= factor
        if self.image:
            self.image = self.image.resize((int(self.image.size[0] * self.zoom_scale), int(self.image.size[1] * self.zoom_scale)), Image.Resampling.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.display_image()
            #logging.info(f"Zoom adjusted to {self.zoom_scale}.")

    def start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        self.canvas.move(tk.ALL, dx, dy)
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def cleanup(self):
        logging.info("Cleaning up FileTab resources...")
        if hasattr(self, 'image_tk'):
            del self.image_tk
            logging.info("ImageTk resources cleaned.")

    
