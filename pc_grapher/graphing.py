"""
This module contains functions for graphing data.
"""

from sys import platform as sys_pf
from matplotlib import pyplot as plt
import matplotlib

# This fixes the issue with the matplotlib backend on macOS.
if sys_pf == 'darwin':
    matplotlib.use("TkAgg")


class Grapher:
    """
    A class for graphing the received data from the ESP32.
    """

    def __init__(self):
        """
        Initializes the Grapher object.
        """

        self.__fig, self.__ax = plt.subplots()
        self.__fig.set_size_inches(11, 6)
        self.__fig.subplots_adjust(left=0.05, right=0.99, top=0.98, bottom=0.1)
        self.__ax.set_xlabel("Time (s)")

    def get_axis(self) -> plt.Axes:
        """
        Returns the axis object of the graph.
        """

        return self.__ax

    def get_fig(self) -> plt.Figure:
        """
        Returns the figure object of the graph.
        """

        return self.__fig

    def plot(self, *args, **kwargs) -> None:
        """
        Plots the data on the graph.
        """
        self.__ax.set_xlabel("Time (s)")
        self.__ax.plot(*args, **kwargs)

    def clear(self) -> None:
        """
        Clears the graph.
        """

        self.__ax.clear()
        # self.__fig.clear()

    def set_value_label(self, label: str) -> None:
        """
        Sets the label for the y-axis.
        """

        self.__ax.set_ylabel(label)
