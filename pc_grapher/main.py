"""
Main module for the pc_grapher package.

When the program is run, this module is executed first.
"""

from gui import AppGUI


class Application:
    """
    This class is responsible for handling the main application logic.
    """

    def __init__(self):
        """
        This constructor creates instances of all important components of
        the application and runs it.
        """

        self.__gui = AppGUI()

        self.__gui.mainloop()


if __name__ == "__main__":
    Application()
