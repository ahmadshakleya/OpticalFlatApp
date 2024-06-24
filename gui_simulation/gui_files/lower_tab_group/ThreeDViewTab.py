import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.CylinderTab import CylinderTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.DiskTab import DiskTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.Flat_surfaceTab import FlatSurfaceTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.OpticalFlatTab import OpticalFlatTab
from gui_simulation.gui_files.upper_tab_group.gui_InsertTab_files.STLFigureTab import STLFigureTab
from gui_utility.intersection import find_intersection
from shapes.disk import Disk
from shapes.flat_surface import FlatSurface
from shapes.shape3D import Shape3D
from shapes.cylinder import Cylinder
from shapes.OpticalFlat import OpticalFlat
from shapes.STLFigure import STLFigure

class ThreeDViewTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.list_shapes = []
        self.create_widgets()
        self.update_button_state()
        self.parent = parent

    def create_widgets(self):
        self.paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.clear_button = ttk.Button(list_frame, text="Clear All Shapes", command=self.clear_shapes)
        self.clear_button.pack(side=tk.TOP, fill=tk.X)

        self.delete_button = ttk.Button(list_frame, text="Delete Selected Shape", state=tk.DISABLED, command=self.delete_selected_shape)
        self.delete_button.pack(side=tk.TOP, fill=tk.X)

        self.edit_button = ttk.Button(list_frame, text="Edit Parameters", state=tk.DISABLED, command=self.edit_selected_shape)
        self.edit_button.pack(side=tk.TOP, fill=tk.X)

        self.intersection_button = ttk.Button(list_frame, text="Calculate Intersection", command=self.calculate_intersections, state=tk.DISABLED)
        self.intersection_button.pack(side=tk.TOP, fill=tk.X)

        self.save_image_button = ttk.Button(list_frame, text="Save Optical Flat Measurement", command=self.save_image, state=tk.DISABLED)
        self.save_image_button.pack(side=tk.TOP, fill=tk.X)

        self.shape_list = ttk.Treeview(list_frame, columns=("type"))
        self.shape_list.column("#0", width=0, stretch=tk.NO)
        self.shape_list.heading("#0", text="", anchor=tk.W)
        self.shape_list.column("type", anchor=tk.CENTER, width=80)
        self.shape_list.heading("type", text="Type", anchor=tk.CENTER)
        self.shape_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.shape_list.bind('<<TreeviewSelect>>', self.on_shape_select)

        self.paned_window.add(list_frame)

        self.init_canvas()


    def init_canvas(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)
        self.paned_window.add(self.canvas_widget)

    def calculate_intersections(self):
        self.update_button_state()
        for shape1 in self.list_shapes:
            for shape2 in self.list_shapes:
                if shape1 != shape2 and isinstance(shape1, Shape3D) and isinstance(shape2, Shape3D):
                    x, y, z = find_intersection(shape1, shape2)
                    print(f"Intersection between {shape1} and {shape2}:")
                    print("X:", x)
                    print("Y:", y)
                    print("Z:", z)
                    self.ax.scatter(x, y, z, color='black', s=10)

    def on_shape_select(self, event):
        self.update_button_state()
        if self.shape_list.selection():
            self.delete_button['state'] = tk.NORMAL
            self.edit_button['state'] = tk.NORMAL
        else:
            self.delete_button['state'] = tk.DISABLED
            self.edit_button['state'] = tk.DISABLED

    def edit_selected_shape(self):
        self.update_button_state()
        selected_id = self.shape_list.selection()[0]
        print("edit_id:",selected_id)
        shape_to_edit = next((shape for shape in self.list_shapes if str(id(shape)) == selected_id), None)
        if shape_to_edit:
            self.edit_window = tk.Toplevel(self)
            if isinstance(shape_to_edit, Cylinder):
                self.edit_tab = CylinderTab(self.edit_window, self, existing_shape=shape_to_edit)
            elif isinstance(shape_to_edit, Disk):
                self.edit_tab = DiskTab(self.edit_window, self, existing_shape=shape_to_edit)
            elif isinstance(shape_to_edit, FlatSurface):
                self.edit_tab = FlatSurfaceTab(self.edit_window, self, existing_shape=shape_to_edit)
            elif isinstance(shape_to_edit, OpticalFlat):
                self.edit_tab = OpticalFlatTab(self.edit_window, self, existing_shape=shape_to_edit)
            elif isinstance(shape_to_edit, STLFigure):
                self.edit_tab = STLFigureTab(self.edit_window, self, existing_shape=shape_to_edit)
            self.edit_tab.pack(fill='both', expand=True) 
            self.edit_window.transient(self)
            self.edit_window.grab_set()
            self.edit_window.wait_window(self.edit_tab)

    def delete_selected_shape(self):
        selected_id = self.shape_list.selection()[0]
        print("delete_id:",selected_id)
        shape_to_remove = next((shape for shape in self.list_shapes if str(id(shape)) == selected_id), None)
        if shape_to_remove:
            self.list_shapes.remove(shape_to_remove)
            self.shape_list.delete(selected_id)
            self.draw_shapes()
            self.update_button_state()

    def add_shape(self, shape, ido=None):
        """Add a shape to the list without drawing."""
        if isinstance(shape, Shape3D):
            self.list_shapes.append(shape)
            if ido == None:
                self.shape_list.insert("", 'end', iid=str(id(shape)), text="", values=(type(shape).__name__,))
            else:
                self.shape_list.insert("", 'end', iid=str(ido), text="", values=(type(shape).__name__,))
            #try:
            #    self.shape_list.insert("", 'end', iid=str(id(shape)), text="", values=(type(shape).__name__,))
            #except tk.TclError:
            #    self.shape_list.insert("", 'end', iid=str(id(shape)+100000), text="", values=(type(shape).__name__,))
            self.update_button_state()
            self.draw_shapes()

    def draw_shapes(self):
        """Draw all shapes in the list."""
        self.update_button_state()
        self.ax.clear()
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        for shape in self.list_shapes:
            shape.plot(self.fig, self.ax)
        self.canvas.draw()

    def clear_shapes(self):
        self.list_shapes.clear()
        self.ax.clear()
        self.fig.clf()
        self.canvas.draw()
        self.shape_list.delete(*self.shape_list.get_children())
        self.update_button_state()

    def update_button_state(self):
        has_shapes = bool(self.list_shapes)
        self.clear_button['state'] = tk.NORMAL if has_shapes else tk.DISABLED
        self.intersection_button['state'] = tk.NORMAL if (len(self.list_shapes) > 1) else tk.DISABLED
        self.save_image_button['state'] = tk.NORMAL if (len(self.list_shapes) > 1) else tk.DISABLED
        self.delete_button['state'] = tk.NORMAL if self.shape_list.selection() else tk.DISABLED
        self.edit_button['state'] = tk.NORMAL if self.shape_list.selection() else tk.DISABLED
    
    def calculate_intersections_v2(self):
        intersections = []
        for i, shape1 in enumerate(self.list_shapes):
            for shape2 in self.list_shapes[i+1:]:
                if isinstance(shape1, Shape3D) and isinstance(shape2, Shape3D):
                    x, y, z = find_intersection(shape1, shape2)
                    if x.size > 0 and y.size > 0 and z.size > 0:
                        intersections.append((x, y, z))
        return intersections

    def plot_results(self, intersections):
        self.clear_shapes()
        self.fig.clf()
        ax = self.fig.add_subplot(111, projection='3d')
        for x, y, z in intersections:
            ax.scatter(x, y, z, color='black', s=2)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        min_z = 0
        max_z = 0
        for _, _, z in intersections:
            min_z = min(min_z, z.min())
            max_z = max(max_z, z.max())
        if min_z != max_z:
            ax.set_zlim(min_z, max_z)
        else:
            ax.set_zlim(min_z-1, max_z+1)
        ax.set_title('Optical Flat Visualization')
        ax.grid(False)
        ax._axis3don = False
        ax.view_init(elev=90, azim=0)
        self.canvas.draw()

    def save_image(self):
        intersections = self.calculate_intersections_v2()
        if intersections:
            self.plot_results(intersections)
            filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filepath:
                self.fig.savefig(filepath, dpi=300, bbox_inches='tight', pad_inches=0.1)
                tk.messagebox.showinfo("Save Image", "Image saved successfully!")
            #self.fig, self.ax = self.init_canvas()

    def on_closing(self):
        """Handle the closing of the tab or application."""
        self.clear_shapes()  # Clearing any shapes if needed
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThreeDViewTab(root)
    root.mainloop()
