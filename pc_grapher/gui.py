"""
This module contains the GUI for the PC Grapher application.
"""

# Pylint ignores
# pylint: disable=E0402
# pylint: disable=R0902

import tkinter as tk
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # for importing figs to mpl
from tkscrollableframe import ScrolledFrame
from tkscrollableframe import ScrollbarsType

# import the modules in two ways to avoid import errors
try:
    from gui_menu import MenuGUI
    from graphing import Grapher
except ImportError:
    from .gui_menu import MenuGUI
    from .graphing import Grapher


class AppGUI(tk.Tk):
    """
    This class is responsible for creating the GUI for the PC Grapher application.
    It inherits from Tk and creates a ScrolledFrame object to display the main content.
    """

    def __init__(self,main_app, grapher: Grapher) -> None:
        """
        The constructor initialises the Tk object and creates a ScrolledFrame object to
        display the main content.
        """

        # Can calculate the width and height of the screen or just set it to a fixed value
        self.__width = 1400
        self.__height = 800
        self.__ridge_size = 5

        # self.__main_app = main_app

        tk.Tk.__init__(self)  # call the constructor of the parent class

        self.title("PC Grapher")  # set title of the window

        # set up the ScrolledFrame object
        self.__scroll_window = ScrolledFrame(self, scrollbars=ScrollbarsType.BOTH,
                                             width=self.__width, height=self.__height,
                                             use_scroll_wheel=False,
                                             use_arrow_keys=False)
        self.__scroll_window.pack(side="top", expand=1, fill="both")

        # Create a frame within the ScrolledFrame and configure the layout
        self.__inner_frame = self.__scroll_window.display_widget(tk.Frame)
        self.__inner_frame.rowconfigure(0, minsize=200, weight=1)
        self.__inner_frame.rowconfigure(1, minsize=600, weight=3)
        self.__inner_frame.columnconfigure(0, minsize=self.__width, weight=1)

        self.__top_menu = MenuGUI(main_app,self.__inner_frame, relief=tk.RAISED,
                                  borderwidth=self.__ridge_size)
        self.__top_menu.grid(row=0, column=0, sticky="nsew")

        self.__graph_area = tk.Frame(self.__inner_frame, relief=tk.RAISED,
                                     borderwidth=self.__ridge_size)
        self.__graph_area.grid(row=1, column=0, sticky="nsew")

        self.__canvas = FigureCanvasTkAgg(grapher.get_fig(), master=self.__graph_area)
        self.__map_widget = self.__canvas.get_tk_widget()
        self.update()
        self.__map_widget.config(width=self.__width - (2 * self.__ridge_size),
                                 height=self.__height - self.__top_menu.winfo_height() -
                                        (2 * self.__ridge_size))
        self.__map_widget.grid(row=0, column=1, sticky="nsew", padx=1, pady=1)
        self.__last_graph_update = 0

    def update_graph(self, force: bool = False) -> None:
        """
        This sets/ updates the mpl figure graph on the GUI

        :param force: whether to force an update regardless of whether it's too soon
        :return: None
        """

        if time.time() - self.__last_graph_update < 0.2 and not force:
            return
        self.__last_graph_update = time.time()

        self.__canvas.draw()
