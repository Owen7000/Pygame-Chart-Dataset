__author__ = "Owen Plimer"
__version__ = "0.1.0"

from typing import Deque
from collections import deque

type Number = int | float

class Dataset:
    def __init__(self, dataset_name:str, max_data_length:int=10) -> None:
        self._dataset_name = dataset_name
        self._max_length = max_data_length

        self._data: Deque[Number] = deque(maxlen=self._max_length)

    @property
    def data(self) -> list[Number]:
        return list(self._data)

    def append(self, value: Number) -> None:
        self._data.append(value)

    def clear(self) -> None:
        self._data.clear()

    def __len__(self) -> int:
        return len(self._data)