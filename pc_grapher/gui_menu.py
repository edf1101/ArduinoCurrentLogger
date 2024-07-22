"""
This file is responsible for creating the menu bar frame for the PC Grapher application.
"""

import tkinter as tk


class MenuGUI(tk.Frame):
    """
    This class is responsible for creating the menu bar for the PC Grapher application.
    It inherits from tk.Frame.
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor initialises the Frame object and creates the menu bar.
        """

        tk.Frame.__init__(self, *args, **kwargs)

        # create the subsections of the menubar: File select, File Edit, Board select, Credits
        self.columnconfigure(0, minsize=200, weight=1)
        self.columnconfigure(1, minsize=200, weight=1)
        self.columnconfigure(2, minsize=200, weight=1)
        self.columnconfigure(3, minsize=200, weight=1)
        self.rowconfigure(0, minsize=100, weight=1)

        self.__file_select = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__file_select.grid(row=0, column=0, sticky="nsew")
        self.__file_select.columnconfigure(0, minsize=200, weight=1)

        self.__file_edit = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__file_edit.grid(row=0, column=1, sticky="nsew")
        self.__file_edit.columnconfigure(0, minsize=200, weight=1)

        self.__board_select = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__board_select.grid(row=0, column=2, sticky="nsew")
        self.__board_select.columnconfigure(0, minsize=200, weight=1)

        self.__credits = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__credits.grid(row=0, column=3, sticky="nsew")
        self.__credits.columnconfigure(0, minsize=200, weight=1)

        # setup all the individual menus in the menu bar
        self.__setup_file_select()
        self.__setup_file_edit()
        self.__setup_board_select()
        self.__setup_credits()

    def __setup_file_select(self):
        """
        This function sets up the File select menu.
        """

        # draw a title at the top
        title = tk.Label(self.__file_select, text="File Select", font=("Arial", 16))
        title.grid(row=0, column=0, sticky="nsew")

    def __setup_file_edit(self):
        """
        This function sets up the File Edit menu.
        """

        # draw a title at the top
        title = tk.Label(self.__file_edit, text="File Edit", font=("Arial", 16))
        title.grid(row=0, column=0, sticky="nsew")

    def __setup_board_select(self):
        """
        This function sets up the Board select menu.
        """

        # draw a title at the top
        title = tk.Label(self.__board_select, text="Board Select", font=("Arial", 16))
        title.grid(row=0, column=0, sticky="nsew")

    def __setup_credits(self):
        """
        This function sets up the Credits menu.
        """

        # draw a title at the top
        title = tk.Label(self.__credits, text="Software Details", font=("Arial", 16))
        title.grid(row=0, column=0, sticky="nsew")
