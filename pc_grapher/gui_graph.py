"""
This file is responsible for creating the graph frame for the PC Grapher application.
"""

import tkinter as tk


class GraphGUI(tk.Frame):
    """
    This class is responsible for creating the graph frame for the PC Grapher application.
    It inherits from tk.Frame.
    """

    def __init__(self,  *args, **kwargs):
        """
        The constructor initialises the Frame object and creates the graph.
        """

        tk.Frame.__init__(self, *args, **kwargs)
