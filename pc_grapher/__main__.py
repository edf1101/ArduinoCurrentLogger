"""
Main module for the pc_grapher package.

When the program is run, this module is executed first.
"""
# Pylint ignores
# pylint: disable=E0402
# pylint: disable=R0903

try:
    from gui import AppGUI
    from graphing import Grapher
    import data_components
except ImportError:
    from .gui import AppGUI
    from .graphing import Grapher
    from . import data_components


class Application:
    """
    This class is responsible for handling the main application logic.
    """

    def __init__(self):
        """
        This constructor creates instances of all important components of
        the application and runs it.
        """

        data_components.check_folder_exists()  # Check if the application folder is set up correctly

        self.__current_data = None
        self.__grapher = Grapher()
        self.__gui = AppGUI(main_app=self, grapher=self.__grapher)
        self.__gui.protocol("WM_DELETE_WINDOW", self.__shutdown)

        self.__gui.mainloop()

    def __shutdown(self) -> None:
        """
        Shuts down the app

        :return:None
        """

        self.__gui.quit()
        self.__gui.destroy()

    def on_file_selected(self, file_name: str) -> None:
        """
        This function is called when a file is selected in the GUI.
        It reads the data from the file and plots it.

        :param file_name: The name of the file selected.
        :return: None
        """

        self.__current_data = data_components.GraphData(file_name)
        data = self.__current_data.get_data()
        self.__grapher.clear()
        self.__grapher.set_value_label(self.__current_data.get_value_type())
        self.__grapher.plot(data[0], data[1], 'r')
        self.__gui.update_graph()


if __name__ == "__main__":
    Application()

# g = Grapher()
# ax, fig = g.get_axis(), g.get_fig()
# g.plot([ x for x in range(1, 1000)], [100* (1+math.sin(y/31.14)) for y in range(1, 1000)], 'r')
# fig.show()
