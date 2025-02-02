"""
This file is responsible for creating the menu bar frame for the PC Grapher application.
"""

import tkinter as tk

try:
    import data_components
except ImportError:
    from . import data_components


class MenuGUI(tk.Frame):
    """
    This class is responsible for creating the menu bar for the PC Grapher application.
    It inherits from tk.Frame.
    """

    def __init__(self, main_app, *args, **kwargs):
        """
        The constructor initialises the Frame object and creates the menu bar.
        """

        self.__main_app = main_app

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
        self.__file_listbox = None

        self.__file_data = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__file_data.grid(row=0, column=1, sticky="nsew")
        self.__file_data.columnconfigure(0, minsize=200, weight=1)
        self.__file_data_text = None

        self.__board_select = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__board_select.grid(row=0, column=2, sticky="nsew")
        self.__board_select.columnconfigure(0, minsize=200, weight=1)

        self.__credits = tk.Frame(self, relief=tk.RAISED, borderwidth=3)
        self.__credits.grid(row=0, column=3, sticky="nsew")
        self.__credits.columnconfigure(0, minsize=200, weight=1)

        # setup all the individual menus in the menu bar
        self.__setup_file_select()
        self.__setup_file_data()
        self.__setup_board_select()
        self.__setup_credits()

    def __setup_file_select(self):
        """
        This function sets up the File select menu.
        """

        # draw a title at the top
        title = tk.Label(self.__file_select, text="File Select", font=("Arial", 20, 'bold'))
        title.grid(row=0, column=0, sticky="nsew")

        scroll_frame = tk.Frame(self.__file_select)
        scroll_frame.grid(row=1, column=0, sticky="w")

        # Creating a Listbox and
        # attaching it to root window
        self.__file_listbox = tk.Listbox(scroll_frame)
        self.__file_listbox.bind('<<ListboxSelect>>', self.__on_file_select_change)
        self.__file_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar = tk.Scrollbar(scroll_frame)  # Adding Scrollbar
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)

        # Insert elements into the listbox
        self.__update_listbox_values()

        self.__file_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.__file_listbox.yview)

    def __update_listbox_values(self) -> None:
        """
        This function updates the listbox values if it is changed.

        :return: None
        """

        list_values = sorted(list(self.__file_listbox.get(0, tk.END)))
        current_values = sorted(list(data_components.get_all_valid_files()))
        if list_values != current_values:
            self.__file_listbox.delete(0, tk.END)
            for values in current_values:
                self.__file_listbox.insert(tk.END, values)

    def __on_file_select_change(self, _) -> None:
        """
        This function is called when the file listbox selection is changed.
        It updates the file data menu with the new file data.

        :param event: The event that triggered this function.
        :return: None
        """

        # get the selected file
        selected_file = self.__file_listbox.get(self.__file_listbox.curselection())
        self.__update_listbox_values()
        self.__main_app.on_file_selected(selected_file)

    def __setup_file_data(self):
        """
        This function sets up the File data menu.
        """

        # draw a title at the top
        title = tk.Label(self.__file_data, text="File Data", font=("Arial", 20, 'bold'))
        title.grid(row=0, column=0, sticky="nsew")
        self.__file_data.update()
        self.__file_data_text = tk.Text(self.__file_data, wrap=tk.WORD, font=("Arial", 12),
                                        width=1, height=8)
        self.__file_data_text.grid(row=1, column=0, sticky="nsew")

    def update_text_info_box(self, file_data: data_components.GraphData) -> None:
        """
        This function updates the text box with the file data.

        :param file_data: The file data to display.
        :return: None
        """

        units: str = ''
        match file_data.get_value_type():
            case "CURRENT":
                units = "mA"
            case "VOLTAGE":
                units = "V"
            case _:
                units = ''

        # get the selected file
        text: str = (f'File name: {file_data.get_file_name()}\n'
                     f'Value Type: {file_data.get_value_type()}\n'
                     f'Minimum Value: {file_data.get_min_value()}{units}\n'
                     f'Maximum Value: {file_data.get_max_value()}{units}\n'
                     f'Average Value: {file_data.get_average_value()}{units}\n')
        if file_data.get_value_type() == "CURRENT":
            text += (f'mAH used: {file_data.get_mah()}mAH\n'
                     f'Time to run out 2000 mAH cell: {file_data.time_to_run_out(2000)}h')

        self.__file_data_text.delete(1.0, tk.END)
        self.__file_data_text.insert(tk.END, text)

    def __setup_board_select(self):
        """
        This function sets up the Board select menu.
        """

        # draw a title at the top
        title = tk.Label(self.__board_select, text="Board Select", font=("Arial", 20, 'bold'))
        title.grid(row=0, column=0, sticky="nsew")

    def __setup_credits(self):
        """
        This function sets up the Credits menu.
        """

        # draw a title at the top
        title = tk.Label(self.__credits, text="Software Details", font=("Arial", 20, 'bold'))
        title.grid(row=0, column=0, sticky="nsew")

        # draw the credits
        line_1 = tk.Label(self.__credits,
                          text="This is the PC grapher for an Arduino Current measuring device",
                          font=("Arial", 14), wraplength=200, justify="left", anchor="w")
        line_1.grid(row=1, column=0, sticky="nsew")

        line_2 = tk.Label(self.__credits, text="Built by Ed F", font=("Arial", 14), wraplength=200,
                          justify="left", anchor="w")
        line_2.grid(row=2, column=0, sticky="nsew")

        line_3 = tk.Label(self.__credits,
                          text="Source: https://github.com/edf1101/ArduinoCurrentLogger",
                          font=("Arial", 14), wraplength=200, justify="left", anchor="w")
        line_3.grid(row=3, column=0, sticky="nsew")
