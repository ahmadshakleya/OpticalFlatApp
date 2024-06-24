import tkinter as tk
from tkinter import ttk
from shapes.cylinder import Cylinder

class CylinderTab(ttk.Frame):
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
            "height": "20.0",
            "radius": "5.0",
            "resolution": "100",
            "x_center": "0.0",
            "y_center": "0.0",
            "z_base": "0.0",
            "tilt_theta": "0.0",
            "tilt_phi": "0.0",
            "color": "red",
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
        
        ttk.Label(col1, text="Height:").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.height = ttk.Entry(col1)
        if self.existing_shape is None:
            self.height.insert(0, default_values["height"])
        self.height.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col1, text="Radius:").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.radius = ttk.Entry(col1)
        if self.existing_shape is None:
            self.radius.insert(0, default_values["radius"])
        self.radius.grid(row=3, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col1, text="Resolution:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.resolution = ttk.Entry(col1)
        if self.existing_shape is None:
            self.resolution.insert(0, default_values["resolution"])
        self.resolution.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="X Center:").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.x_center = ttk.Entry(col2)
        if self.existing_shape is None:
            self.x_center.insert(0, default_values["x_center"])
        self.x_center.grid(row=1, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="Y Center:").grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.y_center = ttk.Entry(col2)
        if self.existing_shape is None:
            self.y_center.insert(0, default_values["y_center"])
        self.y_center.grid(row=3, column=0, padx=10, pady=2, sticky="ew")

        ttk.Label(col2, text="Z Base:").grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.z_base = ttk.Entry(col2)
        if self.existing_shape is None:
            self.z_base.insert(0, default_values["z_base"])
        self.z_base.grid(row=5, column=0, padx=10, pady=2, sticky="ew")

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

        button_text = "Update Cylinder" if self.existing_shape else "Insert Cylinder"
        action = self.update_cylinder if self.existing_shape else self.insert_cylinder
        self.insert_button = ttk.Button(self, text=button_text, command=action)
        self.insert_button.grid(row=1, column=0, columnspan=3, padx=10, pady=20, sticky="ew")
        if self.existing_shape:
            self.height.insert(0, str(self.existing_shape.height))
            self.radius.insert(0, str(self.existing_shape.radius))
            self.resolution.insert(0, str(self.existing_shape.resolution))
            self.x_center.insert(0, str(self.existing_shape.x_center))
            self.y_center.insert(0, str(self.existing_shape.y_center))
            self.z_base.insert(0, str(self.existing_shape.z_base))
            self.tilt_theta.insert(0, str(self.existing_shape.tilt_theta))
            self.tilt_phi.insert(0, str(self.existing_shape.tilt_phi))
            self.color.insert(0, str(self.existing_shape.color))
            self.alpha.insert(0, str(self.existing_shape.alpha))

    def insert_cylinder(self):
        h = float(self.height.get())
        r = float(self.radius.get())
        xc = float(self.x_center.get())
        yc = float(self.y_center.get())
        zb = float(self.z_base.get())
        res = int(self.resolution.get())
        theta = float(self.tilt_theta.get())
        phi = float(self.tilt_phi.get())
        color = self.color.get()
        alpha = float(self.alpha.get())

        cylinder = Cylinder(height=h, radius=r, x_center=0, y_center=0, z_base=0, resolution=res, theta=0, phi=0, color=color, alpha=alpha)
        cylinder.translate(dx=xc, dy=yc, dz=zb)

        cylinder.tilt(theta=theta, phi=phi)

        self.three_d_view_tab.add_shape(cylinder)

        print(f"Inserted Cylinder with height {h}, radius {r}, center ({xc}, {yc}, {zb}), resolution {res}, theta {theta} and phi {phi}")

    def update_cylinder(self):
        if self.existing_shape:
            new_height = float(self.height.get())
            new_radius = float(self.radius.get())
            new_resolution = int(self.resolution.get())
            new_x_center = float(self.x_center.get())
            new_y_center = float(self.y_center.get())
            new_z_base = float(self.z_base.get())
            new_tilt_theta = float(self.tilt_theta.get())
            new_tilt_phi = float(self.tilt_phi.get())
            new_color = self.color.get()
            new_alpha = float(self.alpha.get())

            new_cylinder = Cylinder(height=new_height, radius=new_radius, x_center=0, y_center=0, z_base=0, resolution=new_resolution, theta=0, phi=0, color=new_color, alpha=new_alpha)
            new_cylinder.translate(dx=new_x_center, dy=new_y_center, dz=new_z_base)
            new_cylinder.tilt(theta=new_tilt_theta, phi=new_tilt_phi)

            self.three_d_view_tab.delete_selected_shape()
            self.three_d_view_tab.add_shape(new_cylinder)

            if isinstance(self.master, tk.Toplevel):
                self.master.destroy()

            print(
                f"Updated Cylinder with height {new_height}, radius {new_radius}, center ({new_x_center}, {new_y_center}, {new_z_base}), resolution {new_resolution}, theta {new_tilt_theta} and phi {new_tilt_phi}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CylinderTab(root)
    root.mainloop()
