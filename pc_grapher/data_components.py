"""
This file contains functions and classes to handle and manipulate the graph data.
"""

import os
import appdirs


class GraphData:
    """
    This class is responsible for handling the data for the graph.
    """

    def __init__(self, file_name: str) -> None:
        """
        The constructor initialises the graph data.

        :return: None
        """

        self.__time_data: list[float] = []
        self.__value_data: [float | int] = []
        self.__value_type: str = ""  # eg CURRENT, VOLTAGE, etc
        self.__file_name: str = file_name

        self.__import_data(get_appdata_file_path(file_name))

    def __import_data(self, file_name: str) -> None:
        """
        Imports the data from the file.

        :param file_name: The name of the file to import (within appdirs path).
        :return: None (data is stored in the class)
        """

        # A file is stored as:
        # Line0: Value_type(eg Current), Time interval(in ms. eg 20ms)
        # Line1: Value 1, Value 2, Value 3, ..., Value n
        # It must also be .txt file

        with open(file_name, 'r', encoding='utf-8') as file:
            lines: list[str] = file.readlines()

            # Get the time interval
            time_interval: int = int(lines[0].split(',')[1])
            # get the value type
            self.__value_type: str = lines[0].split(',')[0].upper()

            # Get the values
            self.__value_data = [float(i) for i in lines[1].split(',')]
            # Get the time data
            self.__time_data = [i * (time_interval / 1000.0) for i in range(len(self.__value_data))]

    def get_data(self) -> tuple:
        """
        Returns the data for the graph.

        :return: A tuple containing the time and value data.
        """

        return self.__time_data, self.__value_data

    def get_value_type(self) -> str:
        """
        Returns the type of value data.

        :return: The type of value data.
        """

        return self.__value_type

    def get_file_name(self) -> str:
        """
        Returns the name of the file.

        :return: The name of the file.
        """

        return self.__file_name

    def get_max_value(self) -> float:
        """
        Returns the maximum value in the data.

        :return: The maximum value in the data.
        """

        return round(max(self.__value_data), 1)

    def get_average_value(self) -> float:
        """
        Returns the average value in the data.

        :return: The average value in the data.
        """

        return round(sum(self.__value_data) / len(self.__value_data), 1)

    def get_min_value(self) -> float:
        """
        Returns the minimum value in the data.

        :return: The minimum value in the data.
        """

        return round(min(self.__value_data), 1)

    def get_mah(self) -> float:
        """
        Returns the mAh of the data.

        :return: The mAh of the data.
        """

        if self.__value_type != "CURRENT":
            return 0

        return round(self.get_average_value() * self.__time_data[-1] / 3600.0, 1)

    def time_to_run_out(self, battery_capacity: float) -> float:
        """
        Returns the time to run out of the battery.

        :param battery_capacity: The capacity of the battery in mAh.
        :return: The time to run out of the battery.
        """

        if self.__value_type != "CURRENT":
            return 0

        return round(battery_capacity / self.get_average_value(), 3)


def is_valid_file(file_name: str) -> bool:
    """
    Checks if a file is a valid data file.

    :param file_name: The name of the file.
    :return: True if the file is a valid data file, False otherwise.
    """

    # check if file exists
    if not os.path.exists(get_appdata_file_path(file_name)):
        return False

    # check it is .txt file
    if not file_name.endswith('.txt'):
        return False

    # check contents of file
    with open(get_appdata_file_path(file_name), 'r', encoding='utf-8') as file:
        lines: list[str] = file.readlines()

        # Check if there are at least 2 lines
        if len(lines) < 2:
            return False

        # Check if the time interval is an integer
        try:
            int(lines[0].split(',')[1])
        except ValueError:
            return False

        # Check if the values are floats
        for value in lines[1].split(','):
            try:
                float(value)
            except ValueError:
                return False

    return True


def get_appdata_file_path(name: str) -> str:
    """
    Gets the persistent app data path for a file name. Doesn't check if the file exists.

    :param name: The end name. eg 'data.txt' NOT 'abc/data.txt'
    :return: The full absolute path to the file.
    """

    app_data_path = appdirs.user_data_dir("ArduinoCurrentLogger", 'edf1101')
    file_path = os.path.join(app_data_path, name)

    return file_path


def get_all_valid_files() -> list[str]:
    """
    Gets all the valid files in the app data directory.

    :return: A list of all the valid files in the app data directory.
    """

    app_data_path = appdirs.user_data_dir("ArduinoCurrentLogger", 'edf1101')
    files = os.listdir(app_data_path)

    return [file for file in files if is_valid_file(file)]


def check_folder_exists() -> None:
    """
    Checks if the app data directory exists. If not, it creates it.

    :return: None
    """

    app_data_path = appdirs.user_data_dir("ArduinoCurrentLogger", 'edf1101')

    if not os.path.exists(app_data_path):
        os.makedirs(app_data_path)
