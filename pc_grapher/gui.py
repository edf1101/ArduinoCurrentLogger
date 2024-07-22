"""
This module contains the GUI for the PC Grapher application.
"""

import tkinter as tk
from tkinter import ttk
from tkscrollableframe import ScrolledFrame
from tkscrollableframe import ScrollbarsType

from gui_menu import MenuGUI
from gui_graph import GraphGUI


class AppGUI(tk.Tk):
    """
    This class is responsible for creating the GUI for the PC Grapher application.
    It inherits from Tk and creates a ScrolledFrame object to display the main content.
    """

    def __init__(self) -> None:
        """
        The constructor initialises the Tk object and creates a ScrolledFrame object to
        display the main content.
        """

        # Can calculate the width and height of the screen or just set it to a fixed value
        self.__width = 1200
        self.__height = 800

        tk.Tk.__init__(self)  # call the constructor of the parent class

        self.title("PC Grapher")  # set title of the window

        # set up the ScrolledFrame object
        self.__scroll_window = ScrolledFrame(self, scrollbars=ScrollbarsType.BOTH,
                                             width=self.__width, height=self.__height)
        self.__scroll_window.pack(side="top", expand=1, fill="both")
        self.__scroll_window.bind_scroll_wheel(self)

        # Create a frame within the ScrolledFrame and configure the layout
        self.__inner_frame = self.__scroll_window.display_widget(tk.Frame)
        self.__inner_frame.rowconfigure(0, minsize=200, weight=1)
        self.__inner_frame.rowconfigure(1, minsize=600, weight=3)
        self.__inner_frame.columnconfigure(0, minsize=self.__width, weight=1)

        self.__top_menu = MenuGUI(self.__inner_frame, relief=tk.RAISED, borderwidth=5)
        self.__top_menu.grid(row=0, column=0, sticky="nsew")

        self.__graph_area = GraphGUI(self.__inner_frame, relief=tk.RAISED, borderwidth=5)
        self.__graph_area.grid(row=1, column=0, sticky="nsew")

        # Function for removing focus from widgets once they have been clicked off
        self.bind_all("<Button-1>", self.__remove_entry_focus)

    def __remove_entry_focus(self, event) -> None:
        """
        This function removes focuses from widgets when they are clicked off

        :param event: The event that triggered this function
        :return: None
        """
        if not isinstance(event.widget, (tk.Entry, ttk.Entry)):
            self.focus()
