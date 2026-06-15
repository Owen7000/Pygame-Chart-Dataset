__author__ = "Owen Plimer"
__version__ = "0.1.0"

from typing import Deque
from collections import deque

type Number = int | float
"""A numeric type that accepts either integers or floating-point decimals"""

class Dataset:
    def __init__(self, dataset_name:str, max_data_length:int=10) -> None:
        """__init__ Creates a new instance of Dataset

        Creates a new dataset with a name, a max length, and an internal deque which is empty and has length 0.

        Args:
            dataset_name (str): The name that can be used to identify this dataset. This should not be changed after initialisation, as it will break the dataset manager
            max_data_length (int, optional): The maximum number of items the dataset can hold. Defaults to 10.
        """
        self._dataset_name = dataset_name
        self._max_length = max_data_length

        self._data: Deque[Number] = deque(maxlen=self._max_length)

    @property
    def data(self) -> list[Number]:
        """data Get the stored data as a list

        Examples:
            >>> from dataset import Dataset
            >>> Dataset("Dataset name").data
            []

        Returns:
            list[Number]: The data currently stored in the dataset
        """
        return list(self._data)

    @property
    def name(self) -> str:
        """name The name of the dataset

        Used to identify the dataset if you have multiple.
        This is used by the dataset manager class to access specific datasets

        Returns:
            str: The name you gave for the dataset
        """
        return self._dataset_name

    def append(self, value: Number) -> None:
        """append Add 1 piece of data to the set

        Append to the end of the dataset.
        If the data is at the maximum length, the first item will be removed and all other shifted left by one.

        Args:
            value (Number): The Number to add to the dataset
        """
        self._data.append(value)

    def clear(self) -> None:
        """clear Empty the dataset

        Removes all items from the internal deque
        """
        self._data.clear()

    def __len__(self) -> int:
        """__len__ Get the length of the stored data

        Returns the length of the internal data deque

        Examples:
            >>> from dataset import Dataset
            >>> ds1 =  Dataset("Dataset name")
            >>> len(ds1)
            0

        Returns:
            int: The length of the data deque
        """
        return len(self._data)

    def __repr__(self) -> str:
        return f"Dataset: {self._dataset_name}. Length: {len(self)}. Data: {self.data}"