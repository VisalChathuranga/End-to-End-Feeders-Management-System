class siplaceMaintenanceWindow:
    def __init__(self, root, machine_type):
        self.machine_type = machine_type
        self.check_vars = []

        self.siplace_window = ctk.CTkToplevel(root)
        self.siplace_window.title("Siplace Annual Maintenance")
        self.siplace_window.geometry('600x800')
        self.siplace_window.resizable(True, True)  # Allow resizing
        self.siplace_window.attributes("-topmost", 1)

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self.siplace_window)
        self.scrollbar = tk.Scrollbar(self.siplace_window, orient="vertical", command=self.canvas.yview)

        # Create a frame inside the canvas to contain all the widgets
        self.frame = ctk.CTkFrame(self.canvas)

        # Create a window in the canvas to hold the frame
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Configure scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack scrollbar and canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Set frame width to be the same as canvas width
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Bind mouse wheel event to scroll the canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Create the widgets
        self.create_widgets()

    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling."""
        if event.state == 0x0001:  # Check if Control key is held
            # On Windows, the event.delta is typically -120 or 120 for up/down
            delta = event.delta
        else:
            # On macOS, the event.delta is a bit different
            delta = event.delta * -1

        self.canvas.yview_scroll(int(-delta / 120), "units")