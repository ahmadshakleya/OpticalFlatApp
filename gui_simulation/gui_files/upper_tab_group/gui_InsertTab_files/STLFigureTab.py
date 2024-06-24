import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from shapes.STLFigure import STLFigure

class STLFigureTab(ttk.Frame):
    def __init__(self, parent, three_d_view_tab, existing_shape=None):
        super().__init__(parent)
        self.three_d_view_tab = three_d_view_tab
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.existing_shape = existing_shape
        self.create_widgets()

    def create_widgets(self):
        default_values = {
            "x_center": "0.0",
            "y_center": "0.0",
            "z_base": "0.0",
            "file_path": "path_to_your_stl_file.stl",
            "tilt_theta": "0",
            "tilt_phi": "0",
            "color": "red",
            "alpha": "0.5"

        }
        ttk.Label(self, text="STL File Path:").grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.file_path = ttk.Entry(self)
        if self.existing_shape is None:
            self.file_path.insert(0, default_values["file_path"])
        self.file_path.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

        browse_button = ttk.Button(self, text="Browse", command=self.browse_file)
        browse_button.grid(row=1, column=1, padx=10, pady=2, sticky="ew")
        ttk.Label(self, text="X Center:").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.x_center = ttk.Entry(self)
        if self.existing_shape is None:
            self.x_center.insert(0, default_values["x_center"])
        self.x_center.grid(row=3, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(self, text="Y Center:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.y_center = ttk.Entry(self)
        if self.existing_shape is None:
            self.y_center.insert(0, default_values["y_center"])
        self.y_center.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(self, text="Z Base:").grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        self.z_base = ttk.Entry(self)
        if self.existing_shape is None:
            self.z_base.insert(0, default_values["z_base"])
        self.z_base.grid(row=7, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(self, text="Tilt Angle θ (Degrees):").grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.tilt_theta = ttk.Entry(self)
        if self.existing_shape is None:
            self.tilt_theta.insert(0, default_values["tilt_theta"])
        self.tilt_theta.grid(row=3, column=1, padx=10, pady=2, sticky="ew")

        ttk.Label(self, text="Tilt Angle φ (Degrees):").grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        self.tilt_phi = ttk.Entry(self)
        if self.existing_shape is None:
            self.tilt_phi.insert(0, default_values["tilt_phi"])
        self.tilt_phi.grid(row=5, column=1, padx=10, pady=2, sticky="ew")
        button_text = "Update STL Figure" if self.existing_shape else "Insert STL Figure"
        action = self.update_stl_figure if self.existing_shape else self.insert_stl_figure
        self.insert_button = ttk.Button(self, text=button_text, command=action)
        self.insert_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
        if self.existing_shape:
            self.x_center.insert(0, str(self.existing_shape.x_center))
            self.y_center.insert(0, str(self.existing_shape.y_center))
            self.z_base.insert(0, str(self.existing_shape.z_base))
            self.tilt_theta.insert(0, str(self.existing_shape.tilt_theta))
            self.tilt_phi.insert(0, str(self.existing_shape.tilt_phi))
            self.file_path.insert(0, str(self.existing_shape.file_path))
            self.color.insert(0, str(self.existing_shape.color))
            self.alpha.insert(0, str(self.existing_shape.alpha))

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("STL files", "*.stl"), ("All files", "*.*")])
        if filename:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, filename)

    def insert_stl_figure(self):
        file_path = self.file_path.get()
        x_center = float(self.x_center.get())
        y_center = float(self.y_center.get())
        z_base = float(self.z_base.get())
        tilt_theta = float(self.tilt_theta.get())
        tilt_phi = float(self.tilt_phi.get())
        color = self.color.get()
        alpha = float(self.alpha.get())

        if os.path.exists(file_path):
            stl_figure = STLFigure(file_path=file_path, x_center=0, y_center=0, z_base=0, color=color, alpha=alpha)
            stl_figure.translate(dx=x_center, dy=y_center, dz=z_base)
            stl_figure.tilt(theta=tilt_theta, phi=tilt_phi)
            self.three_d_view_tab.add_shape(stl_figure) 
            print(f"Inserted STL Figure from: {file_path} with center ({x_center}, {y_center}, {z_base})")
        else:
            print("File path does not exist.")

    def update_stl_figure(self):
        if self.existing_shape:
            new_x_center = float(self.x_center.get())
            new_y_center = float(self.y_center.get())
            new_z_base = float(self.z_base.get())
            new_file_path = self.file_path.get()
            new_tilt_theta = float(self.tilt_theta.get())
            new_tilt_phi = float(self.tilt_phi.get())
            new_color = self.color.get()
            new_alpha = float(self.alpha.get())

            new_stl_figure = STLFigure(x_center=0, y_center=0, z_base=0, file_path=new_file_path, color=new_color, alpha=new_alpha)
            new_stl_figure.translate(dx=new_x_center, dy=new_y_center, dz=new_z_base)
            new_stl_figure.tilt(theta=new_tilt_theta, phi=new_tilt_phi)

            self.three_d_view_tab.delete_selected_shape()
            self.three_d_view_tab.add_shape(new_stl_figure)
            if isinstance(self.master, tk.Toplevel):
                self.master.destroy()

            print(
                f"Updated Cylinder with center ({new_x_center}, {new_y_center}, {new_z_base}) and file_path = {new_file_path}")



if __name__ == "__main__":
    root = tk.Tk()
    app = STLFigureTab(root)
    root.mainloop()
