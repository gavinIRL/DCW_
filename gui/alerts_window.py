import tkinter as tk
import tkinter.font as tkFont


class AlertsWindow:
    def __init__(self, mainwindow, root):
        self.mainwindow = mainwindow
        self.root = root
        self.root.geometry("400x400+400+400")
        self.frame = tk.Frame(self.root)
        self.label = tk.Label(root, text=f"this is the alerts window")
        self.label.pack()
        self.frame.pack()
