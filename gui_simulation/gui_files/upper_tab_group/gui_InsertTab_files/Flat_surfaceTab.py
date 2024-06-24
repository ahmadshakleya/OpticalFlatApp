import tkinter as tk
from tkinter import ttk

from shapes.flat_surface import FlatSurface

class FlatSurfaceTab(ttk.Frame):
    def __init__(self, parent, three_d_view_tab, existing_shape=None):
        super().__init__(parent)
        self.three_d_view_tab = three_d_view_tab
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.existing_shape = existing_shape
        self.create_widgets()

    def create_widgets(self):
        default_values = {
            "x_range_start": "-5",
            "x_range_end": "5",
            "y_range_start": "-5",
            "y_range_end": "5",
            "resolution": "100",
            "x_center": "0",
            "y_center": "0",
            "z_base": "0",
            "tilt_theta": "0",
            "tilt_phi": "0",
            "color": "green",
            "alpha": "0.5"
        }

        col1 = ttk.Frame(self)
        col2 = ttk.Frame(self)
        col3 = ttk.Frame(self)
        
        col1.grid(row=0, column=0, sticky="nsew")
        col2.grid(row=0, column=1, sticky="nsew")
        col3.grid(row=0, column=2, sticky="nsew")
        
        col1.grid_columnconfigure(0, weight=1)
        col2.grid_columnconfigure(0, weight=1)
        col3.grid_columnconfigure(0, weight=1)

        ttk.Label(col1, text="X Range Start:").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.x_range_start = ttk.Entry(col1)
        if self.existing_shape is None:
            self.x_range_start.insert(0, default_values["x_range_start"])
        self.x_range_start.grid(row=1, column=0, padx=5, pady=2, sticky="ew")

        ttk.Label(col1, text="X Range End:").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.x_range_end = ttk.Entry(col1)
        if self.existing_shape is None:
            self.x_range_end.insert(0, default_values["x_range_end"])
        self.x_range_end.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        ttk.Label(col1, text="Y Range Start:").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.y_range_start = ttk.Entry(col1)
        if self.existing_shape is None:
            self.y_range_start.insert(0, default_values["y_range_start"])
        self.y_range_start.grid(row=3, column=0, padx=5, pady=2, sticky="ew")

        ttk.Label(col1, text="Y Range End:").grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.y_range_end = ttk.Entry(col1)
        if self.existing_shape is None:
            self.y_range_end.insert(0, default_values["y_range_end"])
        self.y_range_end.grid(row=3, column=1, padx=5, pady=2, sticky="ew")

        ttk.Label(col1, text="Resolution:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.resolution = ttk.Entry(col1)
        if self.existing_shape is None:
            self.resolution.insert(0, default_values["resolution"])
        self.resolution.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="Z Value:").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.z_base = ttk.Entry(col2)
        if self.existing_shape is None:
            self.z_base.insert(0, default_values["z_base"])
        self.z_base.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="X Center:").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.x_center = ttk.Entry(col2)
        if self.existing_shape is None:
            self.x_center.insert(0, default_values["x_center"])
        self.x_center.grid(row=3, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="Y Center:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.y_center = ttk.Entry(col2)
        if self.existing_shape is None:
            self.y_center.insert(0, default_values["y_center"])
        self.y_center.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col3, text="Tilt Angle θ (Degrees):").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.tilt_theta = ttk.Entry(col3)
        if self.existing_shape is None:
            self.tilt_theta.insert(0, default_values["tilt_theta"])
        self.tilt_theta.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col3, text="Tilt Angle φ (Degrees):").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.tilt_phi = ttk.Entry(col3)
        if self.existing_shape is None:
            self.tilt_phi.insert(0, default_values["tilt_phi"])
        self.tilt_phi.grid(row=3, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col3, text="Color:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.color = ttk.Entry(col3)
        if self.existing_shape is None:
            self.color.insert(0, default_values["color"])
        self.color.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col3, text="Alpha:").grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        self.alpha = ttk.Entry(col3)
        if self.existing_shape is None:
            self.alpha.insert(0, default_values["alpha"])
        self.alpha.grid(row=7, column=0, padx=10, pady=2, sticky="ew")

        button_text = "Update Flat Surface" if self.existing_shape else "Insert Flat Surface"
        action = self.update_flat_surface if self.existing_shape else self.insert_flat_surface
        self.insert_button = ttk.Button(self, text=button_text, command=action)
        self.insert_button.grid(row=1, column=0, columnspan=3, padx=10, pady=20, sticky="ew")
        if self.existing_shape:
            self.resolution.insert(0, str(self.existing_shape.resolution))
            self.x_range_start.insert(0, str(self.existing_shape.x_range[0]))
            self.x_range_end.insert(0, str(self.existing_shape.x_range[1]))
            self.y_range_start.insert(0, str(self.existing_shape.y_range[0]))
            self.y_range_end.insert(0, str(self.existing_shape.y_range[1]))
            self.x_center.insert(0, str(self.existing_shape.x_center))
            self.y_center.insert(0, str(self.existing_shape.y_center))
            self.z_base.insert(0, str(self.existing_shape.z_base))
            self.tilt_theta.insert(0, str(self.existing_shape.tilt_theta))
            self.tilt_phi.insert(0, str(self.existing_shape.tilt_phi))
            self.color.insert(0, str(self.existing_shape.color))
            self.alpha.insert(0, str(self.existing_shape.alpha))

    def insert_flat_surface(self):
        x_range_start = float(self.x_range_start.get().strip())
        x_range_end = float(self.x_range_end.get().strip())
        y_range_start = float(self.y_range_start.get().strip())
        y_range_end = float(self.y_range_end.get().strip())
        resolution = int(self.resolution.get())
        x_center = float(self.x_center.get())
        y_center = float(self.y_center.get())
        z_base = float(self.z_base.get())
        tilt_theta = float(self.tilt_theta.get())
        tilt_phi = float(self.tilt_phi.get())
        color = self.color.get()
        alpha = float(self.alpha.get())

        flat_surface = FlatSurface(x_range=(x_range_start,x_range_end), y_range=(y_range_start, y_range_end), resolution=resolution,x_center=0, y_center=0, z_base=0, color=color, alpha=alpha)
        flat_surface.translate(dx=x_center, dy=y_center, dz=z_base)
        flat_surface.tilt(theta=tilt_theta, phi=tilt_phi)
        self.three_d_view_tab.add_shape(flat_surface)
        print(f"Inserting Flat Surface with X Range: {(x_range_start, x_range_end)}, Y Range: {(y_range_start, y_range_end)}, Resolution: {resolution}, Center: ({x_center}, {y_center}, Z Base: {z_base})")

    def update_flat_surface(self):
        if self.existing_shape:
            new_resolution = int(self.resolution.get())
            new_x_range_start = float(self.x_range_start.get().strip())
            new_x_range_end = float(self.x_range_end.get().strip())
            new_y_range_start = float(self.y_range_start.get().strip())
            new_y_range_end = float(self.y_range_end.get().strip())
            new_z_base = float(self.z_base.get())
            new_x_center = float(self.x_center.get())
            new_y_center = float(self.y_center.get())
            new_tilt_theta = float(self.tilt_theta.get())
            new_tilt_phi = float(self.tilt_phi.get())
            new_color = self.color.get()
            new_alpha = float(self.alpha.get())

            new_flat_surface = FlatSurface(x_range=(new_x_range_start, new_x_range_end), y_range=(new_y_range_start, new_y_range_end), z_base=0, resolution=new_resolution, color=new_color, alpha=new_alpha)
            new_flat_surface.translate(dx=new_x_center, dy=new_y_center, dz=new_z_base)
            new_flat_surface.tilt(theta=new_tilt_theta, phi=new_tilt_phi)

            self.three_d_view_tab.delete_selected_shape()
            self.three_d_view_tab.add_shape(new_flat_surface)

            if isinstance(self.master, tk.Toplevel):
                self.master.destroy()

            print(
                f"Updated Cylinder with center ({(new_x_range_start, new_x_range_end)}, {(new_y_range_start, new_y_range_end)}, {new_z_base}), resolution {new_resolution}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlatSurfaceTab(root)
    root.mainloop()
