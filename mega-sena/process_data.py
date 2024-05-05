import re
import numpy as np
from pandas import DataFrame
from darts import TimeSeries


def load_file(path: str) -> str:
    with open(path) as file:
        return file.read()


def exclude_none(l: tuple) -> list:
    r = []
    for i in l:
        if not i is None:
            r.append(i)
    return r


def process_file_to_series(path: str) -> TimeSeries:

    file = load_file(path)

    regex = re.compile("(\d+) - (\d+\/\d+\/\d+) - (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)")

    array = []

    for mat in regex.finditer(file):
        f = mat.groups()
        it = f[0]
        date = f[1]
        numbers = exclude_none(f[2:])

        temp = [int(it)]
        temp.extend(numbers)

        array.append(temp)

    array.reverse()

    pd = DataFrame(
        array,
        columns=["it", "data0", "data1", "data2", "data3", "data4", "data5"],
        dtype=np.uint8,
    )

    return TimeSeries.from_dataframe(
        pd, "it", ["data0", "data1", "data2", "data3", "data4", "data5"]
    )


def process_file_to_dataframe(path: str) -> DataFrame:

    file = load_file(path)

    regex = re.compile("(\d+) - (\d+\/\d+\/\d+) - (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)")

    array = []

    for mat in regex.finditer(file):
        f = mat.groups()
        it = f[0]
        date = f[1]
        numbers = exclude_none(f[2:])

        temp = [int(it)]
        temp.extend(numbers)

        array.append(temp)

    array.reverse()

    return DataFrame(
        array,
        columns=["it", "data0", "data1", "data2", "data3", "data4", "data5"],
        dtype=np.uint8,
    )
